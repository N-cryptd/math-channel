r"""
Video 234: Continuous-Time Markov Chains
Stochastic Processes playlist, video 6/12.

Covers: transition rates, generator (Q) matrix, Kolmogorov equations,
embedded jump chain, stationary distributions.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render:  manim -ql scripts/graduate/video-234-continuous-time-markov-chains.py Video234_ContinuousTimeMarkovChains
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


class Video234_ContinuousTimeMarkovChains(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_discrete_to_continuous()
        self.scene3_generator_matrix()
        self.scene4_kolmogorov()
        self.scene5_jump_chain()
        self.scene6_stationary()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Discrete-time Markov chains move in fixed steps. But real systems "
            "like chemical reactions and queues evolve continuously in time.",
            duration=9,
        )
        play_intro(self, "Continuous-Time Markov Chains", "Stochastic Processes")

        title = self.ly.title("From Steps to Flows")
        items = [
            Text("Chemical reactions, epidemics, and queues happen at any moment",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("States are still discrete, but time is continuous",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The key: holding times are exponential (memoryless!)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene2_discrete_to_continuous(self):
        self.add_subcaption(
            "In discrete time we have a transition matrix P. In continuous time, "
            "transitions happen at random moments governed by rate parameters.",
            duration=9,
        )
        self.ly.section_divider(1, "Making Time Continuous")

        title = self.ly.title("The Key Difference")
        left = [
            Text("Discrete Time", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("P = transition matrix", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Steps at n = 0, 1, 2, ...",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        right = [
            Text("Continuous Time", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("Q = generator matrix", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Transitions at any real time t",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.two_columns(left, right, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Holding Times")
        items = [
            Text("Time in state i before jumping: Exponential(q_i)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("q_i = total rate of leaving state i",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Memoryless: no matter how long you waited, same distribution",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene3_generator_matrix(self):
        self.add_subcaption(
            "The generator matrix Q plays the role of P in continuous time. "
            "Off-diagonal entries are transition rates; diagonal entries are negative sums.",
            duration=10,
        )
        self.ly.section_divider(2, "The Generator Matrix Q")

        title = self.ly.title("Structure of Q")
        items = [
            Text("Q(i,j) = q_ij for i not equal to j (transition rates)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Q(i,i) = minus sum of all q_ij for j not equal to i",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Every row of Q sums to zero",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Transition Probabilities")
        formula = MathTex(r"P(t) = e^{Qt}",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

    def scene4_kolmogorov(self):
        self.add_subcaption(
            "The Kolmogorov forward and backward equations describe how "
            "transition probabilities evolve over time as systems of ODEs.",
            duration=9,
        )
        self.ly.section_divider(3, "Kolmogorov Equations")

        title = self.ly.title("Forward vs Backward")
        left = [
            Text("Forward", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("P'(t) = P(t) Q",
                 font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        right = [
            Text("Backward", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("P'(t) = Q P(t)",
                 font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        self.ly.two_columns(left, right, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene5_jump_chain(self):
        self.add_subcaption(
            "If we ignore the holding times and just look at the sequence of states, "
            "we get a discrete-time chain called the embedded jump chain.",
            duration=9,
        )
        self.ly.section_divider(4, "The Embedded Jump Chain")

        title = self.ly.title("Ignoring Time")
        items = [
            Text("Record only the sequence of states visited",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Jump probability: P(i,j) = q_ij / q_i for j not equal to i",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This is a standard discrete-time Markov chain",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene6_stationary(self):
        self.add_subcaption(
            "Stationary distributions for continuous-time chains satisfy a "
            "similar equation to the discrete case, but using Q instead of P.",
            duration=8,
        )
        self.ly.section_divider(5, "Long-Run Behavior")

        title = self.ly.title("Stationary Distribution")
        formula = MathTex(r"\pi Q = 0, \quad \sum_j \pi_j = 1",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Same Classification Ideas")
        items = [
            Text("Recurrent, transient, positive/null all carry over",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Irreducibility still means one communicating class",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "To recap: continuous-time Markov chains use the generator Q instead of P. "
            "Next we study Brownian motion, the most important continuous-state process.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("CTMC: discrete states, continuous time, exponential holding",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Generator Q: off-diagonal = rates, diagonal = negative sums",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("P(t) = exp(Qt), Kolmogorov forward and backward equations",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Embedded jump chain: discrete chain from state sequence",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Brownian Motion", "Stochastic Processes")
