r"""
Video 239: Ito's Lemma
Stochastic Processes playlist, video 11/12.

Covers: why ordinary calculus fails for Brownian motion, quadratic variation,
Ito's formula statement, and applications.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-239-itos-lemma.py Video239_ItosLemma
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


class Video239_ItosLemma(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_why_ordinary_fails()
        self.scene3_quadratic_variation()
        self.scene4_formula()
        self.scene5_examples()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Ordinary calculus breaks down for Brownian motion because its paths "
            "are nowhere differentiable. We need a new chain rule: Ito's lemma.",
            duration=10,
        )
        play_intro(self, "Ito's Lemma", "Stochastic Processes")

        title = self.ly.title("The Chain Rule of Stochastic Calculus")
        items = [
            Text("Brownian motion has no derivative, so df/dt makes no sense",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("But (dW)^2 = dt in a precise sense",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This extra term is the key to Ito's lemma",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene2_why_ordinary_fails(self):
        self.add_subcaption(
            "In ordinary calculus, d(f(x)) equals f prime times dx. For Brownian "
            "motion, there is an additional second-order term from the quadratic variation.",
            duration=9,
        )
        self.ly.section_divider(1, "Why Ordinary Calculus Fails")

        title = self.ly.title("The Extra Term")
        left = [
            Text("Ordinary", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("df = f'(x) dx", font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        right = [
            Text("Stochastic", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("df = f' dW + (1/2) f'' dt", font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        self.ly.two_columns(left, right, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene3_quadratic_variation(self):
        self.add_subcaption(
            "The quadratic variation of Brownian motion over interval 0 to t is exactly t. "
            "This is why the second-order term matters.",
            duration=9,
        )
        self.ly.section_divider(2, "Quadratic Variation")

        title = self.ly.title("(dW)^2 = dt")
        items = [
            Text("Sum of squared increments converges to t",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("This is the quadratic variation of Brownian motion",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Forces a second-order term in the Taylor expansion",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene4_formula(self):
        self.add_subcaption(
            "Ito's lemma gives the differential of a function of Brownian motion "
            "as a sum of drift and diffusion terms plus a correction.",
            duration=9,
        )
        self.ly.section_divider(3, "Ito's Formula")

        title = self.ly.title("The Formula")
        items = [
            Text("df(t, W_t) = f_t dt + f_x dW_t + (1/2) f_xx dt",
                 font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("First term: ordinary time derivative (drift)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Second term: Brownian derivative (diffusion)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Third term: Ito correction from (dW)^2 = dt",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene5_examples(self):
        self.add_subcaption(
            "Apply Ito's lemma to f(x) = x^2. We get d(W_t^2) = 2 W_t dW_t + dt.",
            duration=7,
        )
        self.ly.section_divider(4, "Example")

        title = self.ly.title("f(x) = x squared")
        items = [
            Text("f' = 2x and f'' = 2",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("d(W_t)^2 = 2 W_t dW_t + dt",
                 font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Integrating: W_t^2 = 2 integral W_s dW_s + t",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "Ito's lemma is the stochastic chain rule. Next we use it to define "
            "stochastic differential equations.",
            duration=8,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Ordinary chain rule fails because (dW)^2 = dt, not 0",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Ito's lemma adds a (1/2) f'' dt correction term",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Foundation for stochastic differential equations",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Stochastic Differential Equations", "Stochastic Processes")
