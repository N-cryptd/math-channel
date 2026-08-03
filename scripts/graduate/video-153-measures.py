"""
Video 153: Measures (the Measure Function) -- Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video153_Measures

Topics: Formal definition of measure, properties (null empty set,
        monotonicity, subadditivity), Lebesgue outer measure,
        Caratheodory extension.

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


class Video153_Measures(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_formal_definition()
        self.scene3_key_properties()
        self.scene4_countable_subadditivity()
        self.scene5_outer_measures()
        self.scene6_lebesgue_outer_measure()
        self.scene7_caratheodory()
        self.scene8_summary()

    # --- Scene 1: Hook -- "Assigning Sizes" ~50s ---

    def scene1_hook(self):
        self.add_subcaption(
            "Last time we built the sigma-algebra, the family of sets "
            "we are allowed to measure. Now we finally define the "
            "measure itself: the function that assigns a size to "
            "every measurable set. A measure is the bridge between "
            "the structure of measurable sets and the numbers we "
            "assign to them.",
            duration=50,
        )
        play_intro(self, "Measures", "Measure Theory")

        title = self.ly.title("Assigning Sizes", color=ACCENT)

        item1 = Text(
            "Sigma-algebra F: which sets are measurable",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Measure mu: assigns a number to each measurable set",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "The triple (X, F, mu) = a MEASURE SPACE",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.7, wait_time=1.5,
        )

        # Visual: measure function arrow
        mu_arrow = MathTex(
            r"\mu : \mathcal{F} \to [0, \infty]",
            font_size=HEADING_SIZE,
        )
        mu_arrow[0].set_color(ACCENT)
        ensure_fits(mu_arrow)
        self.ly.safe_place(mu_arrow, anchor=item3, buff=0.6)
        self.play(Write(mu_arrow), run_time=1.0)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Formal Definition of a Measure ~70s ---

    def scene2_formal_definition(self):
        self.add_subcaption(
            "Let X comma F be a measurable space. A measure mu "
            "is a function from F to the extended non-negative "
            "real numbers satisfying three axioms. One: the "
            "measure of the empty set is zero. Two: every set "
            "has non-negative measure. Three: countable "
            "additivity for pairwise disjoint sets. The triple "
            "X comma F comma mu is called a measure space.",
            duration=70,
        )
        self.ly.section_divider(1, "Definition of a Measure")

        title = self.ly.title("Definition of a Measure", color=PRIMARY)

        domain = MathTex(
            r"\mu : \mathcal{F} \to [0, \infty]",
            font_size=BODY_SIZE,
        )
        domain[0].set_color(ACCENT)
        ensure_fits(domain)
        self.ly.safe_place(domain, anchor=title, buff=0.6)
        self.play(Write(domain), run_time=1.0)
        self.wait(0.8)

        ax1 = MathTex(
            r"(1)", r"\;", r"\mu(\emptyset) = 0",
            font_size=BODY_SIZE,
        )
        ax1[0].set_color(PRIMARY)
        ax1[2].set_color(WHITE)
        ensure_fits(ax1)
        self.ly.safe_place(ax1, anchor=domain, buff=0.45)
        self.play(FadeIn(ax1, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        ax2 = MathTex(
            r"(2)", r"\;", r"\mu(A) \geq 0 \;\; \forall A \in \mathcal{F}",
            font_size=BODY_SIZE,
        )
        ax2[0].set_color(SECONDARY)
        ax2[2].set_color(WHITE)
        ensure_fits(ax2)
        self.ly.safe_place(ax2, anchor=ax1, buff=0.4)
        self.play(FadeIn(ax2, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        ax3 = MathTex(
            r"(3)", r"\;", r"\mu\!\left(\bigcup_{i=1}^{\infty} A_i\right) "
            r"= \sum_{i=1}^{\infty} \mu(A_i)",
            font_size=BODY_SIZE,
        )
        ax3[0].set_color(ACCENT)
        ax3[2].set_color(ACCENT)
        ensure_fits(ax3)
        self.ly.safe_place(ax3, anchor=ax2, buff=0.4)
        self.play(FadeIn(ax3, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.6)

        disjoint_note = Text(
            "when A_1, A_2, ... are pairwise disjoint",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(disjoint_note)
        self.ly.safe_place(disjoint_note, anchor=ax3, buff=0.3)
        self.play(FadeIn(disjoint_note), run_time=0.5)
        self.wait(1.0)

        # Replace axiom details with measure space definition
        self.play(
            *[FadeOut(m) for m in [ax1, ax2, ax3, disjoint_note]],
            run_time=0.6,
        )

        space_def = MathTex(
            r"(X, \mathcal{F}, \mu)",
            r"\text{ is a }",
            r"\textbf{measure space}",
            font_size=HEADING_SIZE,
        )
        space_def[0].set_color(PRIMARY)
        space_def[2].set_color(ACCENT)
        ensure_fits(space_def)
        self.ly.center_in_content(space_def)
        self.play(Write(space_def), run_time=0.8)
        self.wait(1.0)

        prob_note = Text(
            "Special case: mu(X) = 1 makes it a PROBABILITY measure",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(prob_note)
        self.ly.safe_place(prob_note, anchor=space_def, buff=0.5)
        self.play(FadeIn(prob_note, shift=LEFT * 0.15), run_time=0.6)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 3: Key Properties ~70s ---

    def scene3_key_properties(self):
        self.add_subcaption(
            "From the three axioms, many important properties "
            "follow. Finite additivity is immediate from countable "
            "additivity by padding with empty sets. Monotonicity "
            "says that if A is a subset of B, then mu of A is at "
            "most mu of B. There is also an inclusion-exclusion "
            "formula. And continuity from below: if sets grow "
            "and their union is A, then their measures converge "
            "to mu of A.",
            duration=70,
        )
        self.ly.section_divider(2, "Key Properties of Measures")

        title = self.ly.title("Key Properties of Measures", color=PRIMARY)

        # Property 1: Finite additivity
        p1 = MathTex(
            r"\mu(A \cup B) = \mu(A) + \mu(B)",
            font_size=BODY_SIZE,
        )
        p1_label = Text(
            "Finite additivity (when A, B disjoint)",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        p1_group = VGroup(p1, p1_label).arrange(DOWN, buff=0.25)
        p1_group[0].set_color(WHITE)
        ensure_fits(p1_group)
        self.ly.safe_place(p1_group, anchor=title, buff=0.5)
        self.play(Write(p1), FadeIn(p1_label, shift=LEFT * 0.15), run_time=0.8)
        self.wait(1.2)

        # Property 2: Monotonicity
        p2 = MathTex(
            r"A \subseteq B \implies \mu(A) \leq \mu(B)",
            font_size=BODY_SIZE,
        )
        p2.set_color(SECONDARY)
        ensure_fits(p2)
        self.ly.safe_place(p2, anchor=p1_group, buff=0.45)
        self.play(FadeIn(p2, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        # Proof sketch
        proof = Text(
            "Proof: B = A union (B \\ A), disjoint => mu(B) = mu(A) + mu(B\\A) >= mu(A)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(proof)
        self.ly.safe_place(proof, anchor=p2, buff=0.35)
        self.play(FadeIn(proof), run_time=0.5)
        self.wait(1.5)

        # Clear and show more properties
        self.play(
            *[FadeOut(m) for m in [p1, p1_label, p2, proof]],
            run_time=0.6,
        )

        # Inclusion-exclusion
        ie = MathTex(
            r"\mu(A \cup B) = \mu(A) + \mu(B) - \mu(A \cap B)",
            font_size=BODY_SIZE,
        )
        ie.set_color(ACCENT)
        ensure_fits(ie)
        self.ly.safe_place(ie, anchor=title, buff=0.5)
        self.play(Write(ie), run_time=0.8)
        self.wait(1.0)

        # Continuity from below
        cfb = MathTex(
            r"A_1 \subseteq A_2 \subseteq \cdots, \;\bigcup_n A_n = A "
            r"\implies \mu(A_n) \to \mu(A)",
            font_size=BODY_SIZE,
        )
        cfb.set_color(WHITE)
        ensure_fits(cfb)
        self.ly.safe_place(cfb, anchor=ie, buff=0.45)
        self.play(FadeIn(cfb, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 4: Countable Subadditivity ~60s ---

    def scene4_countable_subadditivity(self):
        self.add_subcaption(
            "One of the most useful properties is countable "
            "subadditivity. If A one, A two, and so on are "
            "measurable sets, not necessarily disjoint, then the "
            "measure of their union is at most the sum of their "
            "measures. The proof works by defining disjoint "
            "pieces and applying countable additivity. Equality "
            "holds when the sets are disjoint. This property is "
            "crucial for proving convergence theorems later.",
            duration=60,
        )
        self.ly.section_divider(3, "Countable Subadditivity")

        title = self.ly.title("Countable Subadditivity", color=PRIMARY)

        statement = MathTex(
            r"\mu\!\left(\bigcup_{i=1}^{\infty} A_i\right) "
            r"\leq \sum_{i=1}^{\infty} \mu(A_i)",
            font_size=HEADING_SIZE,
        )
        statement.set_color(ACCENT)
        statement_box = self.ly.formula_box(statement, color=ACCENT)
        ensure_fits(statement_box)
        self.ly.safe_place(statement_box, anchor=title, buff=0.6)
        self.play(Write(statement_box), run_time=1.0)
        self.wait(1.0)

        note = Text(
            "Sets need NOT be disjoint",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(note)
        self.ly.safe_place(note, anchor=statement, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=0.6)
        self.wait(1.0)

        # Proof sketch
        self.play(FadeOut(note), run_time=0.4)

        proof_step1 = MathTex(
            r"B_1 = A_1, \;\; B_n = A_n \setminus (A_1 \cup \cdots \cup A_{n-1})",
            font_size=BODY_SIZE,
        )
        proof_step1.set_color(WHITE)
        ensure_fits(proof_step1)
        self.ly.safe_place(proof_step1, anchor=statement, buff=0.5)
        self.play(Write(proof_step1), run_time=0.8)
        self.wait(0.8)

        proof_step2 = Text(
            "The B_n are disjoint and union B_n = union A_n",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        ensure_fits(proof_step2)
        self.ly.safe_place(proof_step2, anchor=proof_step1, buff=0.35)
        self.play(FadeIn(proof_step2), run_time=0.5)
        self.wait(0.8)

        proof_step3 = Text(
            "mu(union) = sum mu(B_n) <= sum mu(A_n) since B_n subset A_n",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(proof_step3)
        self.ly.safe_place(proof_step3, anchor=proof_step2, buff=0.3)
        self.play(FadeIn(proof_step3), run_time=0.5)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 5: Outer Measures ~70s ---

    def scene5_outer_measures(self):
        self.add_subcaption(
            "Here is a problem. What if we want to measure sets "
            "that are not in our sigma-algebra? The solution is "
            "to define an outer measure, a weaker notion that "
            "works on all subsets of X. An outer measure is "
            "defined on the full power set. It satisfies the "
            "null empty set property, monotonicity, and "
            "countable subadditivity. It is too weak to be a "
            "proper measure, but it is a starting point for "
            "constructing genuine measures.",
            duration=70,
        )
        self.ly.section_divider(4, "Outer Measures")

        title = self.ly.title("Outer Measures", color=PRIMARY)

        motivation = Text(
            "Problem: what about sets NOT in F?",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        ensure_fits(motivation)
        self.ly.safe_place(motivation, anchor=title, buff=0.5)
        self.play(Write(motivation), run_time=0.7)
        self.wait(0.8)

        solution = Text(
            "Solution: define a measure on ALL subsets first",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(solution)
        self.ly.safe_place(solution, anchor=motivation, buff=0.4)
        self.play(FadeIn(solution, shift=LEFT * 0.15), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(motivation), FadeOut(solution), run_time=0.5)

        # Formal definition
        defn_label = MathTex(
            r"\mu^* : \mathcal{P}(X) \to [0, \infty]",
            r"\text{ is an outer measure if:}",
            font_size=BODY_SIZE,
        )
        defn_label[0].set_color(ACCENT)
        defn_label[1].set_color(WHITE)
        ensure_fits(defn_label)
        self.ly.safe_place(defn_label, anchor=title, buff=0.5)
        self.play(Write(defn_label), run_time=0.8)
        self.wait(0.6)

        om1 = MathTex(
            r"(1)", r"\;", r"\mu^*(\emptyset) = 0",
            font_size=BODY_SIZE,
        )
        om1[0].set_color(PRIMARY)
        om1[2].set_color(WHITE)
        ensure_fits(om1)
        self.ly.safe_place(om1, anchor=defn_label, buff=0.4)
        self.play(FadeIn(om1, shift=LEFT * 0.15), run_time=0.5)
        self.wait(0.6)

        om2 = MathTex(
            r"(2)", r"\;", r"A \subseteq B \implies \mu^*(A) \leq \mu^*(B)",
            font_size=BODY_SIZE,
        )
        om2[0].set_color(SECONDARY)
        om2[2].set_color(WHITE)
        ensure_fits(om2)
        self.ly.safe_place(om2, anchor=om1, buff=0.35)
        self.play(FadeIn(om2, shift=LEFT * 0.15), run_time=0.5)
        self.wait(0.6)

        om3 = MathTex(
            r"(3)", r"\;", r"\mu^*\!\left(\bigcup_{i=1}^{\infty} A_i\right) "
            r"\leq \sum_{i=1}^{\infty} \mu^*(A_i)",
            font_size=BODY_SIZE,
        )
        om3[0].set_color(ACCENT)
        om3[2].set_color(ACCENT)
        ensure_fits(om3)
        self.ly.safe_place(om3, anchor=om2, buff=0.35)
        self.play(FadeIn(om3, shift=LEFT * 0.15), run_time=0.5)
        self.wait(1.0)

        note = Text(
            "Outer measure trades countable additivity for subadditivity",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(note)
        self.ly.safe_place(note, anchor=om3, buff=0.4)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 6: Lebesgue Outer Measure ~70s ---

    def scene6_lebesgue_outer_measure(self):
        self.add_subcaption(
            "The most important example of an outer measure is "
            "the Lebesgue outer measure on the real line. How "
            "long is an arbitrary subset of R? We cover the "
            "set with countably many open intervals and take the "
            "infimum of the total lengths. This gives the "
            "Lebesgue outer measure. An open interval has its "
            "expected length. Single points have zero measure. "
            "And the rationals in the unit interval have zero "
            "measure, even though they are dense.",
            duration=70,
        )
        self.ly.section_divider(5, "Lebesgue Outer Measure")

        title = self.ly.title("Lebesgue Outer Measure", color=PRIMARY)

        question = Text(
            "How long is an ARBITRARY subset of R?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(question)
        self.ly.safe_place(question, anchor=title, buff=0.6)
        self.play(Write(question), run_time=0.7)
        self.wait(1.0)

        self.play(FadeOut(question), run_time=0.4)

        # Definition
        defn = MathTex(
            r"m^*(A) = \inf \left\{ \sum_{i=1}^{\infty} (b_i - a_i) "
            r": A \subseteq \bigcup_{i=1}^{\infty} (a_i, b_i) \right\}",
            font_size=BODY_SIZE,
        )
        defn[0].set_color(ACCENT)
        defn_box = self.ly.formula_box(defn, color=PRIMARY)
        ensure_fits(defn_box)
        self.ly.safe_place(defn_box, anchor=title, buff=0.6)
        self.play(Write(defn_box), run_time=1.2)
        self.wait(1.0)

        explain = Text(
            "Cover A with countably many open intervals; take infimum of total length",
            font_size=LABEL_SIZE, color=WHITE, font=SANS,
        )
        ensure_fits(explain)
        self.ly.safe_place(explain, anchor=defn, buff=0.45)
        self.play(FadeIn(explain, shift=LEFT * 0.15), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(explain), run_time=0.4)

        # Key facts
        fact1 = MathTex(
            r"m^*((a,b)) = b - a",
            font_size=BODY_SIZE,
        )
        fact1.set_color(PRIMARY)
        ensure_fits(fact1)
        self.ly.safe_place(fact1, anchor=defn, buff=0.45)
        self.play(Write(fact1), run_time=0.6)
        self.wait(0.6)

        fact2 = MathTex(
            r"m^*(\{x\}) = 0",
            font_size=BODY_SIZE,
        )
        fact2.set_color(SECONDARY)
        ensure_fits(fact2)
        self.ly.safe_place(fact2, anchor=fact1, buff=0.35)
        self.play(FadeIn(fact2, shift=LEFT * 0.15), run_time=0.5)
        self.wait(0.6)

        fact3 = MathTex(
            r"m^*(\mathbb{Q} \cap [0,1]) = 0",
            font_size=BODY_SIZE,
        )
        fact3.set_color(ACCENT)
        ensure_fits(fact3)
        self.ly.safe_place(fact3, anchor=fact2, buff=0.35)
        self.play(FadeIn(fact3, shift=LEFT * 0.15), run_time=0.5)
        self.wait(0.6)

        fact3_note = Text(
            "Rationals are dense but have zero Lebesgue measure!",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        ensure_fits(fact3_note)
        self.ly.safe_place(fact3_note, anchor=fact3, buff=0.3)
        self.play(FadeIn(fact3_note), run_time=0.5)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 7: Caratheodory Extension ~70s ---

    def scene7_caratheodory(self):
        self.add_subcaption(
            "Now the magic. How do we go from an outer measure, "
            "defined on all subsets, to a proper measure, defined "
            "on a sigma-algebra? Caratheodory gives us a criterion. "
            "A set E is measurable if for every set A, the outer "
            "measure of A equals the sum of the outer measures "
            "of the part inside E and the part outside E. The "
            "measurable sets form a sigma-algebra, and the outer "
            "measure restricted to this sigma-algebra is a true "
            "measure. This theorem builds the Lebesgue measure "
            "from the Lebesgue outer measure.",
            duration=70,
        )
        self.ly.section_divider(6, "Caratheodory Extension")

        title = self.ly.title("Caratheodory Extension", color=PRIMARY)

        # The criterion
        criterion_label = Text(
            "Caratheodory's Criterion:",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(criterion_label)
        self.ly.safe_place(criterion_label, anchor=title, buff=0.5)
        self.play(Write(criterion_label), run_time=0.7)
        self.wait(0.5)

        criterion = MathTex(
            r"E \text{ is measurable if } \forall A:",
            font_size=BODY_SIZE,
        )
        criterion[0].set_color(WHITE)
        ensure_fits(criterion)
        self.ly.safe_place(criterion, anchor=criterion_label, buff=0.35)
        self.play(Write(criterion), run_time=0.6)
        self.wait(0.5)

        formula = MathTex(
            r"m^*(A) = m^*(A \cap E) + m^*(A \cap E^c)",
            font_size=HEADING_SIZE,
        )
        formula.set_color(ACCENT)
        formula_box = self.ly.formula_box(formula, color=ACCENT)
        ensure_fits(formula_box)
        self.ly.safe_place(formula_box, anchor=criterion, buff=0.4)
        self.play(Write(formula_box), run_time=0.8)
        self.wait(1.0)

        visual_note = Text(
            "A set E is measurable if it splits EVERY set A 'cleanly'",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(visual_note)
        self.ly.safe_place(visual_note, anchor=formula, buff=0.4)
        self.play(FadeIn(visual_note), run_time=0.5)
        self.wait(1.2)

        # Clear and show theorem result
        self.play(
            *[FadeOut(m) for m in [criterion_label, criterion, formula_box, visual_note]],
            run_time=0.6,
        )

        theorem1 = Text(
            "The measurable sets form a SIGMA-ALGEBRA",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        ensure_fits(theorem1)
        self.ly.safe_place(theorem1, anchor=title, buff=0.5)
        self.play(FadeIn(theorem1, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        theorem2 = Text(
            "m* restricted to this sigma-algebra is a TRUE MEASURE",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(theorem2)
        self.ly.safe_place(theorem2, anchor=theorem1, buff=0.4)
        self.play(FadeIn(theorem2, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        # Hierarchy
        hierarchy = MathTex(
            r"\mathcal{P}(\mathbb{R})",
            r"\supset",
            r"\mathcal{L}",
            r"\supset",
            r"\mathcal{B}(\mathbb{R})",
            font_size=HEADING_SIZE,
        )
        hierarchy[0].set_color(RED)
        hierarchy[2].set_color(ACCENT)
        hierarchy[4].set_color(PRIMARY)
        ensure_fits(hierarchy)
        self.ly.safe_place(hierarchy, anchor=theorem2, buff=0.5)
        self.play(Write(hierarchy), run_time=0.8)
        self.wait(0.5)

        h_labels = Text(
            "all subsets   >   Lebesgue measurable   >   Borel",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(h_labels)
        self.ly.safe_place(h_labels, anchor=hierarchy, buff=0.25)
        self.play(FadeIn(h_labels), run_time=0.4)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 8: Summary ~45s ---

    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap. A measure assigns a non-negative "
            "number to each measurable set, with countable "
            "additivity as the key axiom. Key properties "
            "include monotonicity, countable subadditivity, "
            "and continuity from below. An outer measure "
            "generalizes this to all subsets by replacing "
            "additivity with subadditivity. The Lebesgue "
            "outer measure extends length to arbitrary sets. "
            "And Caratheodory extension turns outer measures "
            "into proper measures on a sigma-algebra. Next "
            "video: the Lebesgue measure in detail.",
            duration=45,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Summary", color=ACCENT)

        items = [
            Text("Measure mu: F -> [0, inf] with countable additivity", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Properties: monotonicity, subadditivity, continuity", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Outer measure: defined on ALL subsets, subadditivity only", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Lebesgue outer measure: length generalized to arbitrary sets", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Caratheodory: outer measure -> true measure on sigma-algebra", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(1.0)

        self.ly.clear()
        play_outro(self)
