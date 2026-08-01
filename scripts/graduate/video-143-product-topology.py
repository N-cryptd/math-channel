"""
Video 143: Product Topology -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 8 of 12)
Class: Video143_ProductTopology

Topics: Product spaces, product topology (finite and infinite),
         box vs product topology, projection maps, Tychonoff connection,
         key results (compact products, connected products).

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


class Video143_ProductTopology(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_product_space()
        self.scene3_product_topology()
        self.scene4_projections()
        self.scene5_box_vs_product()
        self.scene6_key_results()
        self.scene7_summary()

    # --- Scene 1: Hook ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "What happens when you combine two topological spaces to make "
            "a new one? The product construction takes two spaces X and Y "
            "and builds X times Y, the set of all ordered pairs. This gives "
            "us the plane from two copies of the real line, the torus from "
            "two circles, and much more. The product topology tells us "
            "exactly how to combine their open sets.",
            duration=50,
        )
        play_intro(self, "Product Topology", "Topology")

        # Visual: R x R from two number lines
        title = self.ly.title("Building New Spaces from Old", color=PRIMARY)
        self.wait(0.3)

        # X axis
        x_line = NumberLine(x_range=[-3, 3, 1], length=7, color=PRIMARY, include_numbers=False)
        x_label = Text("X", font_size=BODY_SIZE, color=PRIMARY, font=MONO)
        x_label.next_to(x_line, RIGHT, buff=0.2)
        x_group = VGroup(x_line, x_label)
        x_group.move_to(UP * 1.2)
        self.play(Create(x_line), FadeIn(x_label), run_time=FAST)
        self.wait(0.3)

        # Y axis
        y_line = NumberLine(x_range=[-3, 3, 1], length=7, color=SECONDARY, include_numbers=False, rotation=PI / 2)
        y_label = Text("Y", font_size=BODY_SIZE, color=SECONDARY, font=MONO)
        y_label.next_to(y_line, UP, buff=0.2)
        y_group = VGroup(y_line, y_label)
        y_group.move_to(LEFT * 3.2)
        self.play(Create(y_line), FadeIn(y_label), run_time=FAST)
        self.wait(0.5)

        # Result: 2D grid
        cross_sym = MathTex(r"\times", font_size=HEADING_SIZE, color=ACCENT)
        cross_sym.move_to(DOWN * 1.2)
        result = Text("= X x Y (a new topological space!)", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        result.next_to(cross_sym, RIGHT, buff=0.3)
        pair = VGroup(cross_sym, result)
        self.play(Write(cross_sym), FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: The Product Space ~60s

    def scene2_product_space(self):
        self.add_subcaption(
            "Given two sets X and Y, their Cartesian product X times Y is "
            "the set of all ordered pairs (x, y) with x in X and y in Y. "
            "If X and Y are topological spaces, we want to put a topology "
            "on X times Y. The natural choice is the product topology, "
            "which makes the projection maps continuous.",
            duration=60,
        )
        self.ly.section_divider("1", "The Product Space")

        self.ly.title("Cartesian Product", color=PRIMARY)
        defn = MathTex(
            r"X \times Y = \{(x, y) : x \in X, \; y \in Y\}",
        )
        defn.set_color(WHITE)
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Examples", color=SECONDARY)
        examples = [
            Text(r"R x R = R^2 (the plane)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text(r"S^1 x S^1 = torus", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text(r"[0,1] x [0,1] = unit square", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text(r"R x S^1 = infinite cylinder", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            examples, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 3: Product Topology -- Finite Products ~70s

    def scene3_product_topology(self):
        self.add_subcaption(
            "The product topology on X times Y is generated by open "
            "rectangles U times V, where U is open in X and V is open in Y. "
            "These form a basis. Every open set in the product topology is "
            "a union of such rectangles. In R squared, these are just "
            "ordinary open rectangles.",
            duration=70,
        )
        self.ly.section_divider("2", "Product Topology")

        self.ly.title("Product Topology (Finite)", color=PRIMARY)
        defn1 = Text("A basis for X x Y:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        defn2 = MathTex(
            r"\{U \times V : U \subseteq X \text{ open}, \; V \subseteq Y \text{ open}\}",
        )
        defn2.set_color(ACCENT)
        basis = VGroup(defn1, defn2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(basis)
        self.play(FadeIn(defn1, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(defn2), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Visual: open rectangles in R^2
        self.ly.title("Visual: Open Rectangles in R^2", color=SECONDARY)
        ax = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=7, y_length=5,
            axis_config={"color": DIM, "include_numbers": False},
        )
        self.ly.center_in_content(ax)
        self.play(Create(ax), run_time=FAST)
        self.wait(0.3)

        # Open rectangle
        rect = Rectangle(
            width=2.5, height=1.8, color=PRIMARY, fill_opacity=0.15, stroke_width=2,
        )
        rect.move_to(ax.c2p(0.5, 0.3))
        u_lbl = Text("U x V", font_size=LABEL_SIZE, color=PRIMARY, font=MONO)
        u_lbl.move_to(rect)
        self.play(FadeIn(rect), FadeIn(u_lbl), run_time=FAST)
        self.wait(0.5)

        # Another rectangle
        rect2 = Rectangle(
            width=1.5, height=2.0, color=SECONDARY, fill_opacity=0.12, stroke_width=2,
        )
        rect2.move_to(ax.c2p(-1.2, -0.5))
        v_lbl = Text("U' x V'", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        v_lbl.move_to(rect2)
        self.play(FadeIn(rect2), FadeIn(v_lbl), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: Projections ~50s

    def scene4_projections(self):
        self.add_subcaption(
            "The projection maps send a point (x, y) in X times Y to x in X "
            "or to y in Y. These are always continuous with respect to the "
            "product topology. In fact, the product topology is the coarsest "
            "topology making both projections continuous.",
            duration=50,
        )
        self.ly.section_divider("3", "Projection Maps")

        self.ly.title("Projection Maps", color=PRIMARY)
        proj_def = MathTex(
            r"\pi_X : X \times Y \to X, \; \pi_X(x, y) = x",
        )
        proj_def.set_color(PRIMARY)
        proj_def2 = MathTex(
            r"\pi_Y : X \times Y \to Y, \; \pi_Y(x, y) = y",
        )
        proj_def2.set_color(SECONDARY)
        projs = VGroup(proj_def, proj_def2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(projs)
        self.play(Write(proj_def), run_time=NORMAL)
        self.play(Write(proj_def2), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Key Property", color=ACCENT)
        key = Text("Product topology = COARSEST topology making", font_size=BODY_SIZE, color=WHITE, font=SANS)
        key2 = Text("both projections continuous", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        kg = VGroup(key, key2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(kg)
        self.play(FadeIn(key, shift=LEFT * 0.15), FadeIn(key2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: Box vs Product Topology ~70s

    def scene5_box_vs_product(self):
        self.add_subcaption(
            "For finite products, the box topology and the product topology "
            "coincide. But for infinite products, they differ. The box topology "
            "allows products of infinitely many open sets, creating too many "
            "open sets. The product topology restricts to finite supports, "
            "meaning only finitely many coordinates can be restricted at once.",
            duration=70,
        )
        self.ly.section_divider("4", "Box vs Product Topology")

        self.ly.title("Finite Products: Same Thing", color=SECONDARY)
        same = MathTex(
            r"X_1 \times \cdots \times X_n: \text{ box topology } = \text{ product topology}",
        )
        same.set_color(SECONDARY)
        self.ly.center_in_content(same)
        self.play(Write(same), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Infinite Products: Different!", color=RED)
        diff1 = Text("Box topology: allows U_1 x U_2 x U_3 x ...", font_size=BODY_SIZE, color=RED, font=SANS)
        diff2 = Text("(restricting ALL coordinates simultaneously)", font_size=BODY_SIZE, color=DIM, font=SANS)
        diff3 = Text("Product topology: only FINITELY many coordinates", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        diff4 = Text("can be restricted at once (finite support)", font_size=BODY_SIZE, color=DIM, font=SANS)
        diff5 = Text("=> Product topology is coarser (fewer open sets)", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        diffs = VGroup(diff1, diff2, diff3, diff4, diff5).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.center_in_content(diffs)
        self.ly.progressive_reveal(
            [diff1, diff2, diff3, diff4, diff5], start_from=None,
            reveal_anim=FadeIn, anim_kwargs={"shift": LEFT * 0.15},
            run_time=0.8, wait_time=0.8,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Key Results ~50s

    def scene6_key_results(self):
        self.add_subcaption(
            "The product topology preserves many important properties. "
            "The product of compact spaces is compact, by Tychonoff's "
            "theorem. The product of connected spaces is connected. "
            "And the product of path connected spaces is path connected. "
            "These results make product spaces extremely powerful.",
            duration=50,
        )
        self.ly.section_divider("5", "Key Results")

        self.ly.title("Products Preserve Structure", color=ACCENT)
        results = [
            Text("Compact x Compact = Compact (Tychonoff)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Connected x Connected = Connected", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Path-Connected x Path-Connected = Path-Connected", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Hausdorff x Hausdorff = Hausdorff", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("These hold for FINITE and INFINITE products", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(
            results, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 7: Summary ~40s

    def scene7_summary(self):
        self.add_subcaption(
            "The product topology is the standard way to combine topological "
            "spaces. It uses open rectangles as a basis. For finite products, "
            "the box topology agrees. For infinite products, the product "
            "topology uses finite supports, making it the right choice. "
            "Key properties like compactness, connectedness, and Hausdorff "
            "are preserved under products.",
            duration=40,
        )
        self.ly.section_divider("6", "Summary")

        self.ly.title("Product Topology Recap", color=ACCENT)
        recap = [
            Text("X x Y with basis {U x V : U, V open}", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Projections are continuous (by definition)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("For infinite products: finite support required", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Preserves: compact, connected, Hausdorff", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Quotient Topology", next_playlist="Topology")
