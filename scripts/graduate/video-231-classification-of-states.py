r"""
Video 231: Classification of States
Stochastic Processes playlist, video 3/12.

Covers: communicating states, recurrent vs transient, positive vs null recurrent,
periodicity, irreducible chains, and absorbing states.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render:  manim -ql scripts/graduate/video-231-classification-of-states.py Video231_ClassificationOfStates
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


class Video231_ClassificationOfStates(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_communicating()
        self.scene3_recurrent_transient()
        self.scene4_positive_null()
        self.scene5_periodicity()
        self.scene6_irreducible()
        self.scene7_absorbing()
        self.scene8_summary()

    # -- Scene 1: Hook ------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we built Markov chains and transition matrices. "
            "Now we ask a deeper question: do all states behave the same way?",
            duration=10,
        )
        play_intro(self, "Classification of States", "Stochastic Processes")

        title = self.ly.title("Do All States Behave the Same?")
        items = [
            Text("In a random walk, you might return to the origin infinitely often",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("In a different chain, some states might be visited only once",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Today we classify states into types that govern long-run behavior",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 2: Communicating States ---------------------------------
    def scene2_communicating(self):
        self.add_subcaption(
            "Two states communicate if you can go from one to the other, "
            "and back again, possibly through intermediate states.",
            duration=8,
        )
        self.ly.section_divider(1, "Communicating States")

        title = self.ly.title("Communication Between States")

        formula = MathTex(r"i 	o j 	ext{ if } P^n(i,j) > 0 	ext{ for some } n",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Equivalence Relation")
        items = [
            Text("Reflexive: every state communicates with itself",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Symmetric: i to j implies j to i",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Transitive: chains of communication link states",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Communicating classes partition the state space",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 3: Recurrent vs Transient -----------------------------
    def scene3_recurrent_transient(self):
        self.add_subcaption(
            "The most important distinction: starting from a state, "
            "will you definitely return to it, or might you never come back?",
            duration=9,
        )
        self.ly.section_divider(2, "Recurrent vs Transient")

        title = self.ly.title("Will You Return?")
        items = [
            Text("Let f_ii = probability of ever returning to state i",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)

        # Show the two types side by side
        title2 = self.ly.title("Two Types of States")
        left = [
            Text("Recurrent", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("f_ii = 1", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Guaranteed to return", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        right = [
            Text("Transient", font_size=HEADING_SIZE, color=RED, font=SANS),
            Text("f_ii < 1", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("May never return", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.two_columns(left, right, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

        title3 = self.ly.title("Key Fact")
        items2 = [
            Text("In a finite Markov chain, not all states can be transient",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("At least one state must be recurrent",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title3)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 4: Positive vs Null Recurrent --------------------------
    def scene4_positive_null(self):
        self.add_subcaption(
            "Among recurrent states, we distinguish by how long "
            "it takes to return on average. Some return quickly, "
            "others take forever in expectation.",
            duration=10,
        )
        self.ly.section_divider(3, "Positive and Null Recurrent")

        title = self.ly.title("Expected Return Time")
        formula = MathTex(r"m_i = E[T_i \mid X_0 = i] \quad \text{(expected return time)}",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Two Kinds of Recurrence")
        left = [
            Text("Positive Recurrent", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("m_i < infinity", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Returns quickly on average", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        right = [
            Text("Null Recurrent", font_size=HEADING_SIZE, color=RED, font=SANS),
            Text("m_i = infinity", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Returns, but takes forever on average", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.two_columns(left, right, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

        title3 = self.ly.title("Example from Video 229")
        items = [
            Text("1D symmetric random walk is null recurrent",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("It returns to the origin with probability 1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("But the expected return time is infinite",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 5: Periodicity ------------------------------------------
    def scene5_periodicity(self):
        self.add_subcaption(
            "Some states can only be revisited at regular intervals. "
            "We measure this with the period, the greatest common "
            "divisor of all possible return times.",
            duration=10,
        )
        self.ly.section_divider(4, "Periodicity")

        title = self.ly.title("Defining Period")
        formula = MathTex(r"d(i) = \gcd\{n \geq 1 : P^n(i,i) > 0\}",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Periodic vs Aperiodic")
        left = [
            Text("Periodic", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("d(i) > 1", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Returns at multiples of d", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        right = [
            Text("Aperiodic", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("d(i) = 1", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("No cyclic pattern", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.two_columns(left, right, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

        title3 = self.ly.title("Useful Fact")
        items = [
            Text("Any self-loop (P(i,i) > 0) makes state i aperiodic",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("A 2-state cycle alternating A, B, A, B has period 2",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 6: Irreducible Chains -----------------------------------
    def scene6_irreducible(self):
        self.add_subcaption(
            "When every state can reach every other state, the chain is "
            "called irreducible. This greatly simplifies analysis because "
            "all states share the same classification.",
            duration=10,
        )
        self.ly.section_divider(5, "Irreducible Chains")

        title = self.ly.title("One Class to Rule Them All")
        items = [
            Text("A chain is irreducible if all states communicate",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Equivalently: exactly one communicating class",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("All states share the same recurrence type",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("All states have the same period",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Why This Matters")
        items2 = [
            Text("For irreducible chains, check one state and you know all",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This is the foundation for stationary distributions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 7: Absorbing States ------------------------------------
    def scene7_absorbing(self):
        self.add_subcaption(
            "An absorbing state is a trap: once you enter it, you never leave. "
            "These appear in gambler's ruin, epidemiology, and many real models.",
            duration=10,
        )
        self.ly.section_divider(6, "Absorbing States")

        title = self.ly.title("The Trap States")
        formula = MathTex(r"P(i,i) = 1 \quad \Longrightarrow \quad i \text{ is absorbing}",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Properties")
        items = [
            Text("Once entered, the chain stays there forever",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Every absorbing state is positive recurrent",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Gambler's ruin: states 0 and N are absorbing",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 8: Summary ---------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap the full classification tree and preview "
            "what comes next. Stationary distributions will give us "
            "the long-run probabilities for each state.",
            duration=10,
        )
        title = self.ly.title("Classification Tree")
        items = [
            Text("Recurrent (f_ii = 1) vs Transient (f_ii < 1)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Recurrent splits: Positive (m_i finite) vs Null (m_i infinite)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Periodic (d > 1) vs Aperiodic (d = 1) applies to all states",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Irreducible chains: all states share the same classification",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Stationary Distributions", "Stochastic Processes")
