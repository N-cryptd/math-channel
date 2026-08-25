r"""
Video 240: Stochastic Differential Equations
Stochastic Processes playlist, video 12/12.

Covers: SDE definition, Ito SDEs, interpretation, existence/uniqueness,
applications (geometric Brownian motion, Ornstein-Uhlenbeck).

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-240-stochastic-differential-equations.py Video240_SDEs
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


class Video240_SDEs(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_interpretation()
        self.scene4_examples()
        self.scene5_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Ordinary differential equations describe deterministic evolution. "
            "Stochastic differential equations add random noise, modeling "
            "systems driven by uncertainty.",
            duration=10,
        )
        play_intro(self, "Stochastic Differential Equations", "Stochastic Processes")

        title = self.ly.title("ODEs with Random Noise")
        items = [
            Text("dX_t = mu(t,X_t) dt + sigma(t,X_t) dW_t",
                 font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("mu = drift (deterministic trend)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("sigma = diffusion (random fluctuation)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "An Ito SDE has the form dX equals mu dt plus sigma dW, "
            "where mu is the drift coefficient and sigma is the diffusion coefficient.",
            duration=8,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("The General Form")
        items = [
            Text("dX_t = mu(t, X_t) dt + sigma(t, X_t) dW_t",
                 font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("mu and sigma can depend on both time and the current state",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("W_t is a standard Brownian motion",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene3_interpretation(self):
        self.add_subcaption(
            "The integral form makes SDEs precise. Over small time steps, "
            "the change has a deterministic part and a random part.",
            duration=8,
        )
        self.ly.section_divider(2, "Integral Form")

        title = self.ly.title("Making SDEs Precise")
        items = [
            Text("X_t = X_0 + integral of mu ds + integral of sigma dW_s",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The second integral is an Ito integral",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Existence and uniqueness under Lipschitz conditions on mu and sigma",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene4_examples(self):
        self.add_subcaption(
            "Two classic SDEs: geometric Brownian motion models stock prices, "
            "and the Ornstein-Uhlenbeck process models mean-reverting behavior.",
            duration=9,
        )
        self.ly.section_divider(3, "Classic Models")

        title = self.ly.title("Geometric Brownian Motion")
        items = [
            Text("dS_t = mu S_t dt + sigma S_t dW_t (Black-Scholes model)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Solution: S_t = S_0 exp((mu - sigma^2/2)t + sigma W_t)",
                 font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Ornstein-Uhlenbeck Process")
        items2 = [
            Text("dX_t = theta(mu - X_t) dt + sigma dW_t",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Mean-reverting: pulled toward mu with strength theta",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene5_summary(self):
        self.add_subcaption(
            "This completes our Stochastic Processes playlist. We covered "
            "random walks, Markov chains, Poisson processes, Brownian motion, "
            "martingales, and stochastic calculus.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("SDEs: dX = mu dt + sigma dW (drift + diffusion)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Geometric BM for finance, OU for mean-reversion",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Ito's lemma is the essential tool for working with SDEs",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "", "Stochastic Processes")
