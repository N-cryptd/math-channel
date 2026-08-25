r"""
Video 237: Stopping Times
Stochastic Processes playlist, video 9/12.

Covers: stopping time definition, examples, stopped processes,
Wald's equation preview.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-237-stopping-times.py Video237_StoppingTimes
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


class Video237_StoppingTimes(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_stopped_process()
        self.scene5_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "When should you stop playing a game? A stopping time is a random "
            "moment when you decide to quit, based only on what you have seen so far.",
            duration=10,
        )
        play_intro(self, "Stopping Times", "Stochastic Processes")

        title = self.ly.title("When to Stop?")
        items = [
            Text("A stopping time is a random variable for when to quit",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The decision uses only past information, not the future",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Foundation for the optional stopping theorem",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "Formally, tau is a stopping time if the event that tau equals n "
            "is determined by information up to time n.",
            duration=8,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Formal Definition")
        items = [
            Text("tau is a stopping time w.r.t. filtration F_n if",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("the event (tau = n) belongs to F_n for every n",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("You know whether to stop at time n using only info up to n",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene3_examples(self):
        self.add_subcaption(
            "Classic examples include first passage times and hitting times. "
            "A non-example would be stopping at the last time you are ahead.",
            duration=9,
        )
        self.ly.section_divider(2, "Examples and Non-Examples")

        title = self.ly.title("Valid Stopping Times")
        items = [
            Text("First time S_n reaches level 5: yes (depends only on path so far)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("First time S_n = 0: yes (hitting time of zero)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Not a Stopping Time")
        items2 = [
            Text("The LAST time S_n = 0: requires knowing the future",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene4_stopped_process(self):
        self.add_subcaption(
            "If you stop a martingale at a stopping time, the result is "
            "called the stopped process. It is itself a martingale.",
            duration=8,
        )
        self.ly.section_divider(3, "Stopped Processes")

        title = self.ly.title("Stopping Preserves Martingales")
        formula = MathTex(r"X_{n \wedge \tau} = X_{\min(n, \tau)}",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Key Result")
        items = [
            Text("The stopped process is a martingale if X is a martingale",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Preview: optional stopping theorem gives E[X_tau] = E[X_0]",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene5_summary(self):
        self.add_subcaption(
            "Stopping times model when to quit based on available information. "
            "Next we prove the optional stopping theorem.",
            duration=7,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Stopping time: decision based only on past information",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Hitting times are stopping times; last hitting times are not",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Stopped martingale is still a martingale",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Optional Stopping Theorem", "Stochastic Processes")
