"""
Video 230: Markov Chains
Stochastic Processes playlist, video 2/12.

Covers: Markov property, state diagrams, transition matrices,
Chapman-Kolmogorov equations, and stationary distributions preview.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render:  manim -ql scripts/graduate/video-230-markov-chains.py Video230_MarkovChains
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


class Video230_MarkovChains(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_markov_property()
        self.scene3_state_diagram()
        self.scene4_transition_matrix()
        self.scene5_chapman_kolmogorov()
        self.scene6_stationary_preview()
        self.scene7_weather_example()
        self.scene8_summary()

    # -- Scene 1: Hook ------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we studied random walks, where each step is "
            "independent of everything before it. Now we ask: what if "
            "the next step depends on where you are right now?",
            duration=10,
        )
        play_intro(self, "Markov Chains", "Stochastic Processes")

        title = self.ly.title("From Random Walks to Markov Chains")
        items = [
            Text("A Markov chain remembers its current state, not its history",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The future depends only on the present, not on the past",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Models weather, board games, search algorithms, genetics",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 2: Markov property ------------------------------------
    def scene2_markov_property(self):
        self.add_subcaption(
            "The defining feature of a Markov chain is the Markov property. "
            "Given the present state, the future is independent of the past.",
            duration=8,
        )
        self.ly.section_divider(1, "The Markov Property")

        title = self.ly.title("Memoryless Transitions")
        items = [
            Text("Let X sub n be the state at time n",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)

        self.add_subcaption(
            "Formally, the probability of moving to state j at the next "
            "step depends only on the current state i, not on earlier states.",
            duration=8,
        )

        formula = MathTex(
            r"P(X_{n+1}=j \mid X_n=i, X_{n-1},\ldots,X_0) "
            r"= P(X_{n+1}=j \mid X_n=i)",
            font_size=28, color=WHITE,
        )
        formula_box = self.ly.formula_box(formula, color=ACCENT)
        self.ly.safe_place(formula_box, DOWN, anchor=items[-1])
        self.wait(NORMAL)

        self.add_subcaption(
            "This is the Markov property, or memorylessness. "
            "The chain forgets everything except where it is right now.",
            duration=8,
        )

        markov = Text(
            "The past is irrelevant given the present",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(markov, DOWN, anchor=formula_box)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 3: State diagram --------------------------------------
    def scene3_state_diagram(self):
        self.add_subcaption(
            "A finite Markov chain can be drawn as a state diagram. "
            "Each node is a state, each arrow is a transition with probability.",
            duration=9,
        )
        self.ly.section_divider(2, "State Diagrams")

        title = self.ly.title("Visualizing Transitions")
        self.wait(FAST)

        state_a = Circle(radius=0.45, color=PRIMARY, stroke_width=3)
        label_a = Text("Sunny", font_size=LABEL_SIZE, color=WHITE, font=SANS)
        node_a = VGroup(state_a, label_a).move_to(LEFT * 3 + UP * 1.2)

        state_b = Circle(radius=0.45, color=SECONDARY, stroke_width=3)
        label_b = Text("Cloudy", font_size=LABEL_SIZE, color=WHITE, font=SANS)
        node_b = VGroup(state_b, label_b).move_to(RIGHT * 3 + UP * 1.2)

        state_c = Circle(radius=0.45, color=ACCENT, stroke_width=3)
        label_c = Text("Rainy", font_size=LABEL_SIZE, color=WHITE, font=SANS)
        node_c = VGroup(state_c, label_c).move_to(DOWN * 1.5)

        self.play(FadeIn(node_a), FadeIn(node_b), FadeIn(node_c),
                  run_time=NORMAL)
        self.wait(FAST)

        self.add_subcaption(
            "We have three weather states: Sunny, Cloudy, and Rainy. "
            "Each arrow is labeled with the transition probability.",
            duration=7,
        )

        arrow_aa = CurvedArrow(
            node_a.get_top() + RIGHT * 0.15,
            node_a.get_top() + LEFT * 0.15,
            angle=-TAU / 4, color=DIM, stroke_width=2,
        )
        prob_aa = MathTex(r"0.7", font_size=LABEL_SIZE, color=WHITE)
        prob_aa.next_to(arrow_aa, UP, buff=0.05)

        arrow_ab = Arrow(node_a.get_right(), node_b.get_left(),
                         buff=0.15, color=DIM, stroke_width=2)
        prob_ab = MathTex(r"0.3", font_size=LABEL_SIZE, color=WHITE)
        prob_ab.next_to(arrow_ab, UP, buff=0.05)

        self.play(Create(arrow_aa), FadeIn(prob_aa), run_time=FAST)
        self.play(Create(arrow_ab), FadeIn(prob_ab), run_time=FAST)
        self.wait(FAST)

        self.add_subcaption(
            "From Sunny, there is a 70 percent chance of staying Sunny "
            "and a 30 percent chance of becoming Cloudy.",
            duration=7,
        )

        arrow_ba = Arrow(node_b.get_bottom(), node_a.get_right(),
                         buff=0.15, color=DIM, stroke_width=2, path_arc=0.5)
        prob_ba = MathTex(r"0.6", font_size=LABEL_SIZE, color=WHITE)
        prob_ba.next_to(arrow_ba, UP, buff=0.05)

        arrow_bc = Arrow(node_b.get_left(), node_c.get_top(),
                         buff=0.15, color=DIM, stroke_width=2, path_arc=0.5)
        prob_bc = MathTex(r"0.4", font_size=LABEL_SIZE, color=WHITE)
        prob_bc.next_to(arrow_bc, RIGHT, buff=0.05)

        self.play(Create(arrow_ba), FadeIn(prob_ba), run_time=FAST)
        self.play(Create(arrow_bc), FadeIn(prob_bc), run_time=FAST)
        self.wait(FAST)

        self.add_subcaption(
            "From Cloudy, there is a 60 percent chance of returning to Sunny "
            "and a 40 percent chance of becoming Rainy.",
            duration=7,
        )

        arrow_ca = Arrow(node_c.get_top() + LEFT * 0.2, node_a.get_bottom(),
                         buff=0.15, color=DIM, stroke_width=2, path_arc=-0.5)
        prob_ca = MathTex(r"0.5", font_size=LABEL_SIZE, color=WHITE)
        prob_ca.next_to(arrow_ca, LEFT, buff=0.05)

        arrow_cc = CurvedArrow(
            node_c.get_left(), node_c.get_bottom(),
            angle=-TAU / 4, color=DIM, stroke_width=2,
        )
        prob_cc = MathTex(r"0.5", font_size=LABEL_SIZE, color=WHITE)
        prob_cc.next_to(arrow_cc, DOWN, buff=0.05)

        self.play(Create(arrow_ca), FadeIn(prob_ca), run_time=FAST)
        self.play(Create(arrow_cc), FadeIn(prob_cc), run_time=FAST)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 4: Transition matrix ----------------------------------
    def scene4_transition_matrix(self):
        self.add_subcaption(
            "Every finite Markov chain has a transition matrix P. "
            "Entry P i j is the probability of moving from i to j.",
            duration=8,
        )
        self.ly.section_divider(3, "Transition Matrices")

        title = self.ly.title("The Transition Matrix")

        mat = MathTex(
            r"P = \begin{pmatrix}"
            r"0.7 & 0.3 & 0 \\"
            r"0.6 & 0.0 & 0.4 \\"
            r"0.5 & 0.0 & 0.5"
            r"\end{pmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(mat)
        self.play(Write(mat), run_time=NORMAL)
        self.wait(NORMAL)

        self.add_subcaption(
            "Each row sums to one. From any state you must go somewhere. "
            "Rows are probability distributions over the next state.",
            duration=8,
        )

        row_sum = MathTex(
            r"\sum_j P_{ij} = 1 \quad \text{for all } i",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        row_sum_box = self.ly.formula_box(row_sum, color=ACCENT)
        self.ly.safe_place(row_sum_box, DOWN, anchor=mat)
        self.wait(NORMAL)

        self.add_subcaption(
            "A matrix with non-negative entries and rows summing to one "
            "is called a stochastic matrix, the algebraic backbone "
            "of the entire theory.",
            duration=9,
        )

        stochastic = Text(
            "Such a matrix is called a stochastic matrix",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(stochastic, DOWN, anchor=row_sum_box)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 5: Chapman-Kolmogorov ---------------------------------
    def scene5_chapman_kolmogorov(self):
        self.add_subcaption(
            "If P gives one-step transition probabilities, what about "
            "two steps or ten? The Chapman-Kolmogorov equations show "
            "that multi-step transitions are just matrix powers.",
            duration=11,
        )
        self.ly.section_divider(4, "Chapman-Kolmogorov")

        title = self.ly.title("Multi-Step Transitions")
        items = [
            MathTex(r"P^{(n)} = P^n",
                    font_size=BODY_SIZE, color=WHITE),
            Text("The n-step transition matrix is P to the power n",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)

        self.add_subcaption(
            "The key equation: going from i to j in n plus m steps "
            "equals summing over all intermediate states k after n steps.",
            duration=9,
        )

        ck_formula = MathTex(
            r"P_{ij}^{(n+m)} = \sum_k P_{ik}^{(n)} \cdot P_{kj}^{(m)}",
            font_size=BODY_SIZE, color=WHITE,
        )
        ck_box = self.ly.formula_box(ck_formula, color=ACCENT)
        self.ly.safe_place(ck_box, DOWN, anchor=items[-1])
        self.wait(NORMAL)

        self.add_subcaption(
            "In matrix language, this is simply P to the n times m "
            "equals P to the n times P to the m. Matrix multiplication "
            "chains the probabilities through intermediate states.",
            duration=10,
        )

        matrix_form = MathTex(
            r"P^{(n+m)} = P^{(n)} \cdot P^{(m)}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(matrix_form, DOWN, anchor=ck_box)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 6: Stationary distributions preview -------------------
    def scene6_stationary_preview(self):
        self.add_subcaption(
            "A natural question: does the chain settle into a long-run behavior? "
            "If we start in any state and wait long enough, does the "
            "distribution over states converge?",
            duration=11,
        )
        self.ly.section_divider(5, "Stationary Distributions")

        title = self.ly.title("The Long-Run Behavior")
        items = [
            Text("A distribution pi is stationary if applying P "
                 "leaves it unchanged",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)

        self.add_subcaption(
            "Formally, pi is a row vector satisfying pi P equals pi. "
            "It is a left eigenvector of P with eigenvalue one.",
            duration=9,
        )

        stat_formula = MathTex(
            r"\pi P = \pi, \quad \sum_i \pi_i = 1",
            font_size=BODY_SIZE, color=WHITE,
        )
        stat_box = self.ly.formula_box(stat_formula, color=ACCENT)
        self.ly.safe_place(stat_box, DOWN, anchor=items[-1])
        self.wait(NORMAL)

        self.add_subcaption(
            "Under mild conditions, a finite Markov chain has a unique "
            "stationary distribution, and P to the n converges to a matrix "
            "whose rows are all equal to pi.",
            duration=10,
        )

        converge = Text(
            "P to the n converges: all rows approach the same distribution",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(converge, DOWN, anchor=stat_box)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 7: Weather example (2-step) ---------------------------
    def scene7_weather_example(self):
        self.add_subcaption(
            "Let us compute P squared for our weather chain. "
            "This gives the two-step transition probabilities.",
            duration=8,
        )
        self.ly.section_divider(6, "Worked Example")

        title = self.ly.title("Two-Step Weather Transitions")

        mat_p = MathTex(
            r"P = \begin{pmatrix}"
            r"0.7 & 0.3 & 0 \\"
            r"0.6 & 0 & 0.4 \\"
            r"0.5 & 0 & 0.5"
            r"\end{pmatrix}",
            font_size=28, color=WHITE,
        )
        self.ly.center_in_content(mat_p)
        self.play(Write(mat_p), run_time=NORMAL)
        self.wait(FAST)

        self.add_subcaption(
            "The top-left entry of P squared is 0.7 times 0.7 plus 0.3 times 0.6. "
            "This is the probability of Sunny then Sunny, plus Sunny then Cloudy then Sunny.",
            duration=11,
        )

        # Highlight: the (1,1) entry calculation
        calc = MathTex(
            r"(P^2)_{11} = 0.7 \cdot 0.7 + 0.3 \cdot 0.6 = 0.67",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        calc_box = self.ly.formula_box(calc, color=ACCENT)
        self.ly.safe_place(calc_box, DOWN, anchor=mat_p)
        self.play(FadeIn(calc_box), run_time=NORMAL)
        self.wait(NORMAL)

        self.add_subcaption(
            "Already after two steps, the chance of being Sunny from Sunny "
            "dropped from 70 to 67 percent. The chain is mixing.",
            duration=9,
        )

        insight = Text(
            "The chain is mixing: probabilities are smoothing out",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=calc_box)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 8: Summary ---------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "To summarize: a Markov chain is a sequence of random states "
            "where the next state depends only on the current one. "
            "The transition matrix encodes all one-step probabilities. "
            "Multi-step transitions come from matrix powers via Chapman-Kolmogorov. "
            "Stationary distributions describe the long-run behavior. "
            "Next time, we will study stationary distributions in depth and prove convergence.",
            duration=20,
        )
        title = self.ly.title("Summary")
        items = [
            Text("Markov property: future depends only on the present",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Transition matrix P encodes all one-step probabilities",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"P^{(n)} = P^n",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("Stationary distribution pi: pi P equals pi",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)
        play_outro(self, "Stationary Distributions", "Stochastic Processes")
        self.ly.clear()

