r"""
Video 236: Martingales
Stochastic Processes playlist, video 8/12.

Covers: martingale definition, examples, submartingales, supermartingales,
martingale transforms.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-236-martingales.py Video236_Martingales
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


class Video236_Martingales(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_sub_super()
        self.scene5_transforms()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Imagine a fair casino game. Your expected fortune after the next "
            "round equals your current fortune. This fairness property defines a martingale.",
            duration=10,
        )
        play_intro(self, "Martingales", "Stochastic Processes")

        title = self.ly.title("The Mathematics of Fair Games")
        items = [
            Text("A martingale models a process with no systematic drift",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The best prediction of tomorrow is today",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Foundational for modern probability and mathematical finance",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "A sequence X_n is a martingale if the conditional expectation of the "
            "next value given all past information equals the current value.",
            duration=9,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("The Martingale Property")
        formula = MathTex(r"E[X_{n+1} \mid \mathcal{F}_n] = X_n",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Intuition")
        items = [
            Text("F_n = information available up to time n (filtration)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Given everything you know, expected next value is what you have",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene3_examples(self):
        self.add_subcaption(
            "The simplest martingale is a symmetric random walk. Brownian motion "
            "is also a martingale, as are products of independent mean-one variables.",
            duration=10,
        )
        self.ly.section_divider(2, "Classic Examples")

        title = self.ly.title("Symmetric Random Walk")
        items = [
            Text("S_n = X_1 + X_2 + ... + X_n, each X_i = plus or minus 1",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("E[S_{n+1} | S_n] = S_n since E[X_{n+1}] = 0",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("More Examples")
        items2 = [
            Text("Brownian motion W(t) is a continuous-time martingale",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Product of i.i.d. random variables with mean 1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene4_sub_super(self):
        self.add_subcaption(
            "Submartingales tend to increase on average. Supermartingales tend to decrease. "
            "Both generalize the martingale concept.",
            duration=8,
        )
        self.ly.section_divider(3, "Submartingales and Supermartingales")

        title = self.ly.title("Weaker Properties")
        left = [
            Text("Submartingale", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("E[X_{n+1}|F_n] >= X_n", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Tends to increase", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        right = [
            Text("Supermartingale", font_size=HEADING_SIZE, color=RED, font=SANS),
            Text("E[X_{n+1}|F_n] <= X_n", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Tends to decrease", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.two_columns(left, right, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene5_transforms(self):
        self.add_subcaption(
            "If you bet on a martingale using only past information, your wealth "
            "is still a martingale. You cannot beat a fair game.",
            duration=8,
        )
        self.ly.section_divider(4, "Martingale Transforms")

        title = self.ly.title("You Cannot Beat a Fair Game")
        items = [
            Text("A predictable betting strategy applied to a martingale",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("produces another martingale",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("No betting system can produce a profit from a fair game",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "Martingales capture fairness in probability. Next we define "
            "stopping times and prove the optional stopping theorem.",
            duration=8,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Martingale: E[X_{n+1} | past] = X_n  (no drift)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Submartingale: upward drift, Supermartingale: downward drift",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Martingale transforms preserve the martingale property",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Stopping Times", "Stochastic Processes")
