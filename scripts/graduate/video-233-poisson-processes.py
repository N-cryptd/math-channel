r"""
Video 233: Poisson Processes
Stochastic Processes playlist, video 5/12.

Covers: Poisson process definition, Poisson distribution, exponential inter-arrivals,
memoryless property, superposition and thinning.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render:  manim -ql scripts/graduate/video-233-poisson-processes.py Video233_PoissonProcesses
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


class Video233_PoissonProcesses(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_poisson_distribution()
        self.scene4_exponential_waiting()
        self.scene5_superposition_thinning()
        self.scene6_nonhomogeneous()
        self.scene7_summary()

    # -- Scene 1: Hook ------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "How many customers arrive at a store in an hour? How many emails "
            "do you receive in a day? These are counting processes, and the "
            "Poisson process is the most important model for them.",
            duration=10,
        )
        play_intro(self, "Poisson Processes", "Stochastic Processes")

        title = self.ly.title("Counting Random Events in Time")
        items = [
            Text("Events happen at random times: customers, calls, earthquakes",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("N(t) counts events in the interval from 0 to t",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The Poisson process is the simplest and most useful model",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 2: Definition ------------------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "A Poisson process is defined by three simple axioms about how "
            "events arrive: they start at zero, have independent increments, "
            "and the rate stays constant.",
            duration=9,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Three Axioms")
        items = [
            Text("N(0) = 0: no events at the start",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Independent increments: events in disjoint intervals are independent",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Stationary increments: distribution depends only on interval length",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Rate lambda: on average lambda events per unit time",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 3: Poisson Distribution --------------------------------
    def scene3_poisson_distribution(self):
        self.add_subcaption(
            "The number of events in any interval of length t follows "
            "a Poisson distribution with parameter lambda times t.",
            duration=7,
        )
        self.ly.section_divider(2, "The Poisson Distribution")

        title = self.ly.title("N(t) is Poisson")
        formula = MathTex(
            r"P(N(t) = k) = \frac{e^{-\lambda t} (\lambda t)^k}{k!}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Properties")
        items = [
            Text("Mean: E[N(t)] = lambda * t",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Variance: Var(N(t)] = lambda * t  (equal to mean!)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("lambda is the rate: events per unit time",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 4: Exponential Waiting Times ---------------------------
    def scene4_exponential_waiting(self):
        self.add_subcaption(
            "The time between consecutive events follows an exponential "
            "distribution. This gives the Poisson process its memoryless property.",
            duration=9,
        )
        self.ly.section_divider(3, "Waiting Times")

        title = self.ly.title("Inter-arrival Times")
        formula = MathTex(r"P(T > t) = e^{-\lambda t}",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("The Memoryless Property")
        formula2 = MathTex(
            r"P(T > s + t \mid T > s) = P(T > t)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.formula_box(formula2, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title3 = self.ly.title("What This Means")
        items = [
            Text("Waiting longer does not increase your chances",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The process restarts at every moment",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 5: Superposition and Thinning --------------------------
    def scene5_superposition_thinning(self):
        self.add_subcaption(
            "Two powerful operations: combining independent Poisson processes, "
            "or randomly keeping events from one. Both preserve the Poisson structure.",
            duration=10,
        )
        self.ly.section_divider(4, "Superposition and Thinning")

        title = self.ly.title("Superposition")
        items = [
            Text("Combine independent Poisson processes: still Poisson",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Rates add: new rate = lambda_1 + lambda_2 + ...",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Example: calls from two independent offices",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Thinning")
        items2 = [
            Text("Keep each event with probability p independently",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Result is Poisson with rate p times lambda",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Discarded events form Poisson with rate (1-p) times lambda",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 6: Non-homogeneous Poisson -----------------------------
    def scene6_nonhomogeneous(self):
        self.add_subcaption(
            "The rate lambda can vary with time. This is the non-homogeneous "
            "Poisson process, useful for modeling rush hours or seasonal patterns.",
            duration=9,
        )
        self.ly.section_divider(5, "Varying Rates")

        title = self.ly.title("Non-homogeneous Poisson Process")
        items = [
            Text("Rate depends on time: lambda(t)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Expected count = integral of lambda(t) from 0 to t",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Applications: traffic patterns, website visits, disease spread",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 7: Summary ---------------------------------------------
    def scene7_summary(self):
        self.add_subcaption(
            "To recap: the Poisson process counts random events in continuous time. "
            "Next we generalize to continuous-time Markov chains.",
            duration=8,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("N(t) ~ Poisson(lambda*t) with mean and variance lambda*t",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Inter-arrivals are Exponential(lambda) with memoryless property",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Superposition adds rates, thinning scales them",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Continuous-Time Markov Chains", "Stochastic Processes")
