"""
Video 209: Covering Spaces — Algebraic Topology
Covering maps, the exponential map, path lifting, and the connection to fundamental groups.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes

NARRATION TIMING (v2 fix):
- Duration set to ceil(words / 2.2) + 1 for natural TTS pace
- self.wait() added after animations to fill caption window
- No overlapping SRT segments — each next caption starts after previous ends
"""

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


class Video209_CoveringSpaces(Scene):
    """Covering Spaces: maps that locally look like projections."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_exponential_map()
        self.scene4_examples()
        self.scene5_path_lifting()
        self.scene6_homotopy_lifting()
        self.scene7_fundamental_group()
        self.scene8_monodromy()
        self.scene9_summary()

    # ── Scene 1: Hook — The Lifting Problem ──────────────────────────
    def scene1_hook(self):
        """Motivating hook: unwinding a loop on the circle."""
        # 33 words → duration=16
        self.add_subcaption(
            "Welcome back to Algebraic Topology! In the last video, we studied "
            "the fundamental group, which captures loops up to homotopy. Today we "
            "turn to one of the most powerful ideas in topology: covering spaces.",
            duration=16,
        )
        play_intro(self, "Covering Spaces", "Algebraic Topology")
        # play_intro ~6s, fill remaining ~10s
        self.wait(9)

        # 40 words → duration=19
        self.add_subcaption(
            "Imagine a loop of string wrapped once around a vertical pole. You cannot "
            "pull it free because the pole is in the way. But now imagine lifting the "
            "entire floor onto a spiral staircase. The loop unwinds into a straight path.",
            duration=19,
        )
        title = self.ly.title("The Lifting Problem")

        # Circle (base) with loop
        base_circle = Circle(radius=1.3, color=PRIMARY, stroke_width=3, fill_opacity=0.08)
        loop_on_circle = Circle(radius=1.0, color=RED, stroke_width=2.5)
        self.ly.safe_place(base_circle, LEFT, anchor=title, buff=0.8)
        self.play(Create(base_circle), Create(loop_on_circle), run_time=NORMAL)

        # Arrow label
        lbl_base = Text("Loop on S^1", font_size=LABEL_SIZE, color=RED, font=SANS)
        lbl_base.next_to(base_circle, DOWN, buff=0.2)
        self.play(FadeIn(lbl_base), run_time=FAST)

        # Line (cover) with path
        cover_line = NumberLine(x_range=[-3, 3, 1], length=4.5, color=PRIMARY, stroke_width=2)
        cover_path = Arrow(cover_line.n2p(-1), cover_line.n2p(1), color=SECONDARY,
                           stroke_width=2.5, buff=0)
        self.ly.safe_place(cover_line, RIGHT, anchor=title, buff=0.8)
        self.ly.safe_place(cover_path, DOWN, anchor=cover_line, buff=-0.2)
        self.play(Create(cover_line), Create(cover_path), run_time=NORMAL)

        lbl_cover = Text("Path in R", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        lbl_cover.next_to(cover_line, DOWN, buff=0.2)
        self.play(FadeIn(lbl_cover), run_time=FAST)
        # Animations ~4.8s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # 30 words → duration=15
        self.add_subcaption(
            "Covering spaces make this precise. They give us a way to lift paths, loops, "
            "and even entire homotopies from a complicated space up to a simpler one, "
            "where calculations become tractable.",
            duration=15,
        )
        title2 = self.ly.title("Why Covering Spaces?")
        items = [
            Text("Lift paths from complex spaces to simple ones", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Compute fundamental groups algebraically", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Bridge geometry and algebra", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        # Animations ~2s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

    # ── Scene 2: Definition of Covering Space ────────────────────────
    def scene2_definition(self):
        """Formal definition of a covering map."""
        # 26 words → duration=13
        self.add_subcaption(
            "A covering map is a continuous surjection from one space to another, "
            "where every small region in the base lifts to exact copies upstairs.",
            duration=13,
        )
        self.ly.section_divider(1, "Definition of Covering Space")

        title = self.ly.title("Covering Map")

        # 36 words → duration=17
        self.add_subcaption(
            "Formally, a map p from X-tilde to X is a covering map if every point "
            "x in X has an open neighborhood U, whose preimage is a disjoint union of "
            "open sets, each mapped homeomorphically onto U by p.",
            duration=17,
        )
        defn_map = MathTex(
            r"p : \widetilde{X} \to X",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_map = self.ly.formula_box(defn_map, color=PRIMARY)
        self.ly.safe_place(boxed_map, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_map), run_time=NORMAL)

        self.wait(14)
        self.ly.clear()

        # 33 words → duration=16
        self.add_subcaption(
            "Each component of the preimage is called a sheet, and the preimage of "
            "a point is called the fiber. For the exponential map, the fiber of any "
            "point consists of countably many copies, spaced evenly along the cover.",
            duration=16,
        )
        title2 = self.ly.title("Sheets and Fibers")
        terms = [
            Text("Every x has neighborhood U lifting to sheets", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Sheet: one component of the preimage", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fiber: p-inverse of x (the set of preimage points)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fiber can be finite or infinite", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(terms, start_from=title2)
        # Animations ~2.5s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

        # 30 words → duration=14
        self.add_subcaption(
            "A key property: covering maps are local homeomorphisms. Near any point "
            "upstairs, the map p looks exactly like a projection. But globally, the "
            "cover can have a very different topology than the base.",
            duration=14,
        )
        title3 = self.ly.title("Local vs Global Structure")
        local = MathTex(
            r"p|_{U_i} : U_i \xrightarrow{\cong} U",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(local, DOWN, anchor=title3, buff=0.5)
        self.play(Write(local), run_time=NORMAL)

        global_note = Text(
            "Locally a homeomorphism, globally different topology",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(global_note, DOWN, anchor=local, buff=0.5)
        self.play(FadeIn(global_note, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~12s
        self.wait(11)
        self.ly.clear()

    # ── Scene 3: The Exponential Map — R covers S^1 ──────────────────
    def scene3_exponential_map(self):
        """The canonical example: R covers S^1."""
        # 27 words → duration=13
        self.add_subcaption(
            "The most important covering map is the exponential map from the real "
            "line onto the circle. This is the example that motivates the entire theory.",
            duration=13,
        )
        self.ly.section_divider(2, "The Exponential Map")

        title = self.ly.title("R Covers S^1")

        # 34 words → duration=16
        self.add_subcaption(
            "The map sends a real number t to the point on the unit circle at angle "
            "two pi t. Each interval of length one wraps exactly once around the circle. "
            "As t increases, the image traces the circle over and over.",
            duration=16,
        )
        formula = MathTex(
            r"p(t) = e^{2\pi i\, t}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_formula = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed_formula, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_formula), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~14s
        self.wait(13)

        # Fiber
        # 28 words → duration=13
        self.add_subcaption(
            "The fiber of the point one is all integers. This means the real line wraps "
            "around the circle infinitely many times, with each integer landing on one.",
            duration=13,
        )
        fiber = MathTex(
            r"p^{-1}(1) = \mathbb{Z}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(fiber, DOWN, anchor=boxed_formula, buff=0.5)
        self.play(FadeIn(fiber), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~11s
        self.wait(10)
        self.ly.clear()

        # Visual: helix intuition
        # 35 words → duration=16
        self.add_subcaption(
            "Think of the real line as an infinite helix projecting down onto the circle. "
            "Each integer projects to the same point. A path that goes once around the "
            "circle lifts to a path that moves one unit along the real line.",
            duration=16,
        )
        title2 = self.ly.title("The Helix Picture")

        helix_items = [
            MathTex(r"t \mapsto t + 1", font_size=BODY_SIZE, color=PRIMARY),
            Text("Shift by one = one full rotation below", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Infinite cover: simply connected", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(helix_items, start_from=title2)
        # Animations ~2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # 30 words → duration=14
        self.add_subcaption(
            "This is called the universal cover because the real line is simply connected. "
            "Every loop in the circle lifts to a non-looping path in R, and the lift is "
            "unique once you choose a starting point.",
            duration=14,
        )
        title3 = self.ly.title("Universal Cover")
        universal = Text(
            "R is the universal cover of S^1",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(universal, DOWN, anchor=title3, buff=0.5)
        self.play(FadeIn(universal), run_time=NORMAL)

        why = Text(
            "Simply connected cover unwinds all loops",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(why, DOWN, anchor=universal, buff=0.5)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~12s
        self.wait(11)
        self.ly.clear()

    # ── Scene 4: More Examples ───────────────────────────────────────
    def scene4_examples(self):
        """More examples of covering spaces."""
        # 24 words → duration=12
        self.add_subcaption(
            "Let us see several more examples of covering spaces to build our "
            "intuition before we tackle the theory.",
            duration=12,
        )
        self.ly.section_divider(3, "More Examples")

        # Double cover
        # 34 words → duration=16
        self.add_subcaption(
            "The double cover sends each point on a circle to its square. Going around "
            "once in the cover means going around twice below. The fiber of every point "
            "has exactly two elements.",
            duration=16,
        )
        title = self.ly.title("The Double Cover")
        double = MathTex(
            r"S^1 \xrightarrow{z \mapsto z^2} S^1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(double, DOWN, anchor=title, buff=0.5)
        self.play(Write(double), run_time=NORMAL)

        double_note = Text(
            "Fiber of every point: exactly 2 elements",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(double_note, DOWN, anchor=double, buff=0.5)
        self.play(FadeIn(double_note, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # N-fold cover
        # 29 words → duration=14
        self.add_subcaption(
            "More generally, the map z to z to the power n gives an n-fold cover "
            "of the circle. Each point has exactly n preimages, evenly spaced "
            "around the circle above.",
            duration=14,
        )
        title2 = self.ly.title("n-Fold Covers")
        nfold = MathTex(
            r"S^1 \xrightarrow{z \mapsto z^n} S^1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(nfold, DOWN, anchor=title2, buff=0.5)
        self.play(Write(nfold), run_time=NORMAL)

        nfold_note = Text(
            "Fiber of every point: exactly n elements",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(nfold_note, DOWN, anchor=nfold, buff=0.5)
        self.play(FadeIn(nfold_note, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~12s
        self.wait(11)
        self.ly.clear()

        # Universal cover examples
        # 34 words → duration=16
        self.add_subcaption(
            "The figure-eight space has a universal cover that looks like an infinite "
            "tree, specifically the Cayley graph of the free group on two generators. "
            "Every loop lifts to a unique path in this tree.",
            duration=16,
        )
        title3 = self.ly.title("Universal Covers")
        items = [
            Text("Figure-eight: S^1 wedge S^1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Universal cover: infinite Cayley tree", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Simply connected: all loops unwind", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3)
        # Animations ~2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # 26 words → duration=12
        self.add_subcaption(
            "Every path-connected, locally path-connected space has a universal cover. "
            "It is unique up to isomorphism of covering spaces, and its deck "
            "transformation group is isomorphic to the fundamental group.",
            duration=12,
        )
        title4 = self.ly.title("Existence")
        existence = [
            Text("Every nice space has a universal cover", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Unique up to covering isomorphism", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Deck transformations: fundamental group", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(existence, start_from=title4)
        # Animations ~2s, fill remaining ~10s
        self.wait(9)
        self.ly.clear()

    # ── Scene 5: Path Lifting Property ───────────────────────────────
    def scene5_path_lifting(self):
        """The path lifting property."""
        # 25 words → duration=12
        self.add_subcaption(
            "One of the most powerful properties of covering spaces is the ability "
            "to lift paths from the base space up to the cover.",
            duration=12,
        )
        self.ly.section_divider(4, "Path Lifting")

        title = self.ly.title("The Path Lifting Theorem")

        # 39 words → duration=18
        self.add_subcaption(
            "Given a path gamma in the base space X starting at x naught, and a point "
            "x-tilde in the fiber over x naught, there exists a unique lifted path "
            "gamma-tilde in the cover such that p composed with gamma-tilde equals gamma, "
            "and gamma-tilde starts at x-tilde.",
            duration=18,
        )
        statement = MathTex(
            r"\gamma(0) = x_0, \; \tilde{x} \in p^{-1}(x_0)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~16s
        self.wait(15)

        # Lift equation
        # 30 words → duration=14
        self.add_subcaption(
            "The lift satisfies p composed with gamma-tilde equals gamma at every point, "
            "and gamma-tilde of zero equals x-tilde. The uniqueness is crucial: given the "
            "starting point, the lift is determined for the entire path.",
            duration=14,
        )
        lift = MathTex(
            r"p \circ \tilde{\gamma} = \gamma, \quad \tilde{\gamma}(0) = \tilde{x}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(lift, DOWN, anchor=statement, buff=0.5)
        self.play(FadeIn(lift), run_time=NORMAL)

        unique = Text(
            "Lift is unique given the starting point",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(unique, DOWN, anchor=lift, buff=0.5)
        self.play(FadeIn(unique, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~12s
        self.wait(11)
        self.ly.clear()

        # Intuition for uniqueness
        # 32 words → duration=15
        self.add_subcaption(
            "Why is the lift unique? Because locally, p is a homeomorphism. At each "
            "instant, the path is confined to a single sheet. There is no way to jump "
            "between sheets without leaving the image of p, which cannot happen.",
            duration=15,
        )
        title2 = self.ly.title("Why Unique?")
        intuition_items = [
            Text("Locally p is a homeomorphism", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Path stays on one sheet at each instant", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Cannot jump between sheets continuously", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(intuition_items, start_from=title2)
        # Animations ~2s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

    # ── Scene 6: Homotopy Lifting ───────────────────────────────────
    def scene6_homotopy_lifting(self):
        """The homotopy lifting property."""
        # 28 words → duration=13
        self.add_subcaption(
            "Even better than lifting individual paths, entire homotopies can be "
            "lifted. If two paths are homotopic in the base, their lifts are "
            "homotopic in the cover.",
            duration=13,
        )
        self.ly.section_divider(5, "Homotopy Lifting")

        title = self.ly.title("The Homotopy Lifting Property")

        # 31 words → duration=15
        self.add_subcaption(
            "Formally, given a homotopy H from gamma to sigma in the base space, "
            "and a lift of the initial path, there exists a unique lifted homotopy "
            "H-tilde in the cover.",
            duration=15,
        )
        hlift = MathTex(
            r"\gamma \simeq \sigma \implies \tilde{\gamma} \simeq \tilde{\sigma}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed_hlift = self.ly.formula_box(hlift, color=SECONDARY)
        self.ly.safe_place(boxed_hlift, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_hlift), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

        # Consequence for fundamental group
        # 36 words → duration=17
        self.add_subcaption(
            "This has a remarkable consequence: the projection map p induces a group "
            "homomorphism from the fundamental group of the cover to the fundamental "
            "group of the base. This homomorphism is injective when the cover is "
            "the universal cover.",
            duration=17,
        )
        title2 = self.ly.title("Induced Homomorphism")
        induced = MathTex(
            r"p_* : \pi_1(\widetilde{X}, \tilde{x}_0) \to \pi_1(X, x_0)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(induced, DOWN, anchor=title2, buff=0.5)
        self.play(Write(induced), run_time=NORMAL)

        injective = Text(
            "Injective for the universal cover",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(injective, DOWN, anchor=induced, buff=0.5)
        self.play(FadeIn(injective, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~15s
        self.wait(14)
        self.ly.clear()

    # ── Scene 7: Computing Fundamental Groups ────────────────────────
    def scene7_fundamental_group(self):
        """Connection between covering spaces and the fundamental group."""
        # 26 words → duration=12
        self.add_subcaption(
            "Covering spaces give us a powerful tool for computing fundamental "
            "groups. Let us see how the exponential map computes pi one of the circle.",
            duration=12,
        )
        self.ly.section_divider(6, "Computing Fundamental Groups")

        title = self.ly.title("The Fundamental Group of S^1")

        # 38 words → duration=18
        self.add_subcaption(
            "The covering map from R to S^1 lets us compute the fundamental group of "
            "the circle. Every loop on the circle lifts to a path in R starting at some "
            "integer. The endpoint of this lifted path is an integer, and this integer "
            "is the winding number of the loop.",
            duration=18,
        )
        theorem = MathTex(
            r"\pi_1(S^1) \cong \mathbb{Z}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_thm = self.ly.formula_box(theorem, color=PRIMARY)
        self.ly.safe_place(boxed_thm, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_thm), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~16s
        self.wait(15)

        # Winding number explanation
        # 35 words → duration=16
        self.add_subcaption(
            "The integer counts how many times the loop winds around the circle. "
            "This is the same result we stated in the last video, but now we see "
            "why: it comes directly from the covering space structure. The fundamental "
            "group is exactly the set of deck transformations.",
            duration=16,
        )
        winding_items = [
            Text("Endpoint of lift = winding number", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Homotopic loops have same winding number", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("pi_1(S^1) = Z follows from covering theory", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        title2 = self.ly.title("Why Z?")
        self.ly.progressive_reveal(winding_items, start_from=title2)
        # Animations ~2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # General method
        # 33 words → duration=16
        self.add_subcaption(
            "This technique generalizes. To compute the fundamental group of any space, "
            "find a simply connected cover and study the deck transformations. The group "
            "of deck transformations is isomorphic to the fundamental group of the base.",
            duration=16,
        )
        title3 = self.ly.title("The General Method")
        method = MathTex(
            r"\pi_1(X) \cong \text{Deck}(p) = \text{Aut}(\widetilde{X}/X)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(method, DOWN, anchor=title3, buff=0.5)
        self.play(Write(method), run_time=NORMAL)

        method_note = Text(
            "Deck transformations: cover automorphisms commuting with p",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(method_note, DOWN, anchor=method, buff=0.5)
        self.play(FadeIn(method_note, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

    # ── Scene 8: Monodromy and the Galois Correspondence ────────────
    def scene8_monodromy(self):
        """Monodromy action and the classification of covering spaces."""
        # 27 words → duration=13
        self.add_subcaption(
            "Covering spaces are classified by subgroups of the fundamental group. "
            "This classification is sometimes called the Galois correspondence "
            "of covering spaces.",
            duration=13,
        )
        self.ly.section_divider(7, "Classification of Covers")

        title = self.ly.title("The Galois Correspondence")

        # 33 words → duration=16
        self.add_subcaption(
            "More precisely, the fundamental group acts on the fiber by permuting the "
            "preimage points. This is called the monodromy action. A loop in the base "
            "space permutes the points above by lifting the loop to each sheet.",
            duration=16,
        )
        action = MathTex(
            r"\pi_1(X, x_0) \curvearrowright p^{-1}(x_0)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(action, DOWN, anchor=title, buff=0.5)
        self.play(Write(action), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # Subgroup correspondence
        # 34 words → duration=16
        self.add_subcaption(
            "Different covering spaces correspond to different subgroups of the "
            "fundamental group. The universal cover corresponds to the trivial subgroup. "
            "An n-fold cover corresponds to the subgroup of index n.",
            duration=16,
        )
        title2 = self.ly.title("Subgroups and Covers")
        subgroups = [
            Text("Universal cover: trivial subgroup", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("n-fold cover: subgroup of index n", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Intermediate covers: intermediate subgroups", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(subgroups, start_from=title2)
        # Animations ~2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # Normal covers
        # 30 words → duration=14
        self.add_subcaption(
            "When the corresponding subgroup is normal, the cover is called a regular "
            "or normal cover. In this case, the group of deck transformations acts "
            "transitively on the fiber, and the quotient is exactly the fundamental group.",
            duration=14,
        )
        title3 = self.ly.title("Regular Covers")
        normal_items = [
            Text("Subgroup is normal: regular cover", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Deck group acts transitively on fiber", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Quotient: fundamental group", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(normal_items, start_from=title3)
        # Animations ~2s, fill remaining ~12s
        self.wait(11)
        self.ly.clear()

    # ── Scene 9: Summary ──────────────────────────────────────────────
    def scene9_summary(self):
        """Summary and outro."""
        # 24 words → duration=12
        self.add_subcaption(
            "Let us summarize what we have learned about covering spaces and their "
            "deep connection to the fundamental group.",
            duration=12,
        )
        self.ly.section_divider(8, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("Covering map: local homeomorphism with discrete fibers", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Exponential map: R covers S^1, fiber is the integers", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Path and homotopy lifting: unique lifts", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Covering spaces compute fundamental groups", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        # Animations ~2.5s, fill remaining ~9s
        self.wait(8)
        self.ly.clear()

        # 33 words → duration=16
        self.add_subcaption(
            "The covering space framework is one of the most beautiful in all of "
            "topology. It connects local geometry to global algebra, and gives us "
            "concrete computational tools. The Galois correspondence tells us that "
            "understanding covering spaces is equivalent to understanding subgroups.",
            duration=16,
        )
        title2 = self.ly.title("The Big Picture")
        summary = self.ly.formula_box(
            MathTex(
                r"p : \widetilde{X} \to X, \quad "
                r"\pi_1(X) \cong \text{deck transformations}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            color=PRIMARY,
        )
        self.ly.safe_place(summary, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(summary), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # Outro
        # 28 words → duration=13
        self.add_subcaption(
            "In the next video, we will study simplicial complexes, which give us a "
            "combinatorial way to build and analyze topological spaces. Thank you for watching!",
            duration=13,
        )
        play_outro(self, "Simplicial Complexes", "Algebraic Topology")
