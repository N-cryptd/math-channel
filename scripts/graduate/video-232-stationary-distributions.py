r"""
Video 232: Stationary Distributions
Stochastic Processes playlist, video 4/12.

Covers: stationary distribution definition, computing stationary distributions,
existence and uniqueness, detailed balance, convergence theorem.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render:  manim -ql scripts/graduate/video-232-stationary-distributions.py Video232_StationaryDistributions
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


class Video232_StationaryDistributions(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_computing()
        self.scene4_existence()
        self.scene5_detailed_balance()
        self.scene6_convergence()
        self.scene7_summary()

    # -- Scene 1: Hook ------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "If you run a Markov chain for a very long time, does it settle down? "
            "Does the fraction of time spent in each state converge?",
            duration=9,
        )
        play_intro(self, "Stationary Distributions", "Stochastic Processes")

        title = self.ly.title("Does the Chain Settle Down?")
        items = [
            Text("Run a weather model for 10,000 days",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("What fraction of days are sunny in the long run?",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The answer is the stationary distribution",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 2: Definition ------------------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "A stationary distribution is a probability vector pi such that "
            "if the chain starts in pi, it remains in pi forever.",
            duration=8,
        )
        self.ly.section_divider(1, "What is a Stationary Distribution?")

        title = self.ly.title("The Stationary Equation")
        formula = MathTex(r"\pi P = \pi, \quad \sum_j \pi_j = 1",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Interpretation")
        items = [
            Text("pi_j = long-run fraction of time in state j",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("If X_0 has distribution pi, then so does X_n for all n",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("pi is a left eigenvector of P with eigenvalue 1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 3: Computing -------------------------------------------
    def scene3_computing(self):
        self.add_subcaption(
            "To find the stationary distribution, solve the linear system "
            "pi P equals pi, together with the normalization constraint.",
            duration=8,
        )
        self.ly.section_divider(2, "Finding the Stationary Distribution")

        title = self.ly.title("The Linear System")
        items = [
            Text("Solve: pi P = pi  (n equations)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("With constraint: sum of all pi_j = 1",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Replace one redundant equation with normalization",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Weather Example")
        items2 = [
            Text("Sunny, Cloudy, Rainy with transition matrix P",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Solve the 3x3 system to get pi",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("pi gives long-run probabilities for each weather state",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 4: Existence and Uniqueness ----------------------------
    def scene4_existence(self):
        self.add_subcaption(
            "Not every Markov chain has a stationary distribution. "
            "For finite chains, irreducibility guarantees existence and uniqueness.",
            duration=9,
        )
        self.ly.section_divider(3, "When Does It Exist?")

        title = self.ly.title("Main Theorem")
        items = [
            Text("A finite irreducible Markov chain has a unique stationary distribution",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("For infinite chains, need positive recurrence",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Connection to Video 231: irreducible + positive recurrent = unique pi",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 5: Detailed Balance ------------------------------------
    def scene5_detailed_balance(self):
        self.add_subcaption(
            "Detailed balance is a stronger condition that implies stationarity. "
            "It says the flow from i to j equals the flow from j to i.",
            duration=9,
        )
        self.ly.section_divider(4, "Detailed Balance")

        title = self.ly.title("The Detailed Balance Equation")
        formula = MathTex(r"\pi_i \, P(i,j) = \pi_j \, P(j,i)",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Key Properties")
        items = [
            Text("Detailed balance implies stationarity (but not vice versa)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Chains satisfying detailed balance are called reversible",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Random walk on an undirected graph is reversible",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 6: Convergence -----------------------------------------
    def scene6_convergence(self):
        self.add_subcaption(
            "For irreducible, aperiodic chains, the probability of being in any "
            "state converges to the stationary probability, regardless of where you start.",
            duration=10,
        )
        self.ly.section_divider(5, "Convergence to Stationarity")

        title = self.ly.title("The Convergence Theorem")
        formula = MathTex(r"\lim_{n \to \infty} P^n(i,j) = \pi_j \quad \text{for all } i",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Conditions")
        items = [
            Text("Chain must be: irreducible, aperiodic, positive recurrent",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Independent of starting state i",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Mixing time: how many steps until close to pi",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 7: Summary ---------------------------------------------
    def scene7_summary(self):
        self.add_subcaption(
            "To recap: stationary distributions describe the long-run behavior "
            "of Markov chains. Next we move to continuous time with Poisson processes.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Stationary distribution: pi P = pi, sum = 1",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Exists and is unique for finite irreducible chains",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Convergence requires aperiodicity too",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Detailed balance is a sufficient condition for reversibility",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Poisson Processes", "Stochastic Processes")
