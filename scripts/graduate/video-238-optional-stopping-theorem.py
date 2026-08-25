r"""
Video 238: Optional Stopping Theorem
Stochastic Processes playlist, video 10/12.

Covers: OST statement, conditions (bounded, integrable, a.s. finite),
applications to gambler's ruin and Wald's equation.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-238-optional-stopping-theorem.py Video238_OST
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


class Video238_OST(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_statement()
        self.scene3_conditions()
        self.scene4_gamblers_ruin()
        self.scene5_wald()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "If a game is fair, can you quit at the right time and make a profit? "
            "The optional stopping theorem says: under the right conditions, no.",
            duration=10,
        )
        play_intro(self, "Optional Stopping Theorem", "Stochastic Processes")

        title = self.ly.title("Can You Beat a Fair Game?")
        items = [
            Text("You cannot guarantee a profit by choosing when to stop",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Under mild conditions, E[X_tau] = E[X_0]",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This is one of the most useful theorems in probability",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene2_statement(self):
        self.add_subcaption(
            "The optional stopping theorem states that for a martingale and "
            "a stopping time satisfying certain conditions, the expected value "
            "at the stopping time equals the initial expected value.",
            duration=10,
        )
        self.ly.section_divider(1, "The Theorem")

        title = self.ly.title("Optional Stopping Theorem")
        formula = MathTex(r"E[X_\tau] = E[X_0]",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Requirements")
        items = [
            Text("X_n is a martingale, tau is a stopping time",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("One of three conditions must hold",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene3_conditions(self):
        self.add_subcaption(
            "The three sufficient conditions are: tau is bounded, the martingale "
            "differences are bounded, or tau has finite expectation and the martingale "
            "increments have finite mean.",
            duration=10,
        )
        self.ly.section_divider(2, "Sufficient Conditions")

        title = self.ly.title("Three Conditions (Any One Suffices)")
        items = [
            Text("1. tau is bounded: tau <= N for some fixed N",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. X stopped at tau is bounded: |X_n^tau| <= C",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3. E[tau] < infinity and |X_n - X_{n-1}| <= C",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene4_gamblers_ruin(self):
        self.add_subcaption(
            "In gambler's ruin with fair coin, starting at k dollars, the OST "
            "immediately gives the probability of reaching N before 0.",
            duration=9,
        )
        self.ly.section_divider(3, "Application: Gambler's Ruin")

        title = self.ly.title("Fair Gambler's Ruin")
        items = [
            Text("Symmetric RW from k, stopping at 0 or N",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("S_n is a martingale, tau is bounded by N",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("E[S_tau] = E[S_0] = k gives P(reach N) = k/N",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene5_wald(self):
        self.add_subcaption(
            "Wald's equation gives the expected value of a sum of random "
            "variables evaluated at a stopping time.",
            duration=8,
        )
        self.ly.section_divider(4, "Wald's Equation")

        title = self.ly.title("Wald's Equation")
        formula = MathTex(r"E[\sum_{k=1}^{\tau} X_k] = E[\tau] \cdot E[X_1]",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Conditions")
        items = [
            Text("X_k are i.i.d. with finite mean",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("tau is a stopping time with E[tau] < infinity",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "The OST says fair games stay fair even with clever stopping. "
            "Next we apply these ideas to stochastic calculus via Ito's lemma.",
            duration=9,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("E[X_tau] = E[X_0] for martingales under mild conditions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Three sufficient conditions: bounded time, bounded process, finite expectation",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Applications: gambler's ruin, Wald's equation, many more",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Ito's Lemma", "Stochastic Processes")
