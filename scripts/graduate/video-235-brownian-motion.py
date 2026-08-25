r"""
Video 235: Brownian Motion
Stochastic Processes playlist, video 7/12.

Covers: definition, properties (mean, variance, covariance, self-similarity),
random walk limit, nowhere differentiability, heat equation connection.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render:  manim -ql scripts/graduate/video-235-brownian-motion.py Video235_BrownianMotion
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


class Video235_BrownianMotion(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_properties()
        self.scene4_self_similar()
        self.scene5_random_walk_limit()
        self.scene6_heat_equation()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "In 1827, Robert Brown noticed pollen grains jiggling in water. "
            "Einstein explained this in 1905 as molecular bombardment. "
            "The mathematical model is Brownian motion.",
            duration=11,
        )
        play_intro(self, "Brownian Motion", "Stochastic Processes")

        title = self.ly.title("The Jittering Pollen Grain")
        items = [
            Text("Pollen grains in water move unpredictably",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Einstein: caused by countless molecular collisions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Brownian motion is the continuous limit of random walks",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "Formally, Brownian motion W(t) is defined by three properties: "
            "it starts at zero, has independent increments, and each increment "
            "is normally distributed with variance equal to the time gap.",
            duration=12,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("The Wiener Process W(t)")
        items = [
            Text("W(0) = 0: the process starts at the origin",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Independent increments: non-overlapping changes are independent",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("W(t) - W(s) is Normal with mean 0 and variance t minus s",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sample paths are continuous (no jumps)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene3_properties(self):
        self.add_subcaption(
            "From the definition, we can derive the mean, variance, and "
            "covariance structure of Brownian motion. The variance grows "
            "linearly with time, which is the hallmark of diffusive behavior.",
            duration=12,
        )
        self.ly.section_divider(2, "Key Properties")

        title = self.ly.title("First and Second Moments")
        formula1 = MathTex(r"E[W(t)] = 0",
                           font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula1, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Variance Grows Linearly")
        formula2 = MathTex(r"Var[W(t)] = t",
                           font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula2, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title3 = self.ly.title("Covariance Structure")
        formula3 = MathTex(r"Cov[W(s), W(t)] = \min(s, t)",
                           font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula3, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

    def scene4_self_similar(self):
        self.add_subcaption(
            "Brownian motion is self-similar: if you zoom in on a path, it looks "
            "statistically the same at every scale. This fractal property is related "
            "to the fact that Brownian paths are nowhere differentiable.",
            duration=12,
        )
        self.ly.section_divider(3, "Self-Similarity")

        title = self.ly.title("Scale Invariance")
        formula = MathTex(r"W(ct) \stackrel{d}{=} \sqrt{c} \, W(t)",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Nowhere Differentiable")
        items = [
            Text("Brownian paths have no derivative at any point",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The path oscillates infinitely at every scale",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This makes stochastic calculus necessary",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene5_random_walk_limit(self):
        self.add_subcaption(
            "Brownian motion arises as the limit of scaled random walks. "
            "Shrink step sizes and speed up time, and the jagged walk "
            "smooths into continuous Brownian motion.",
            duration=11,
        )
        self.ly.section_divider(4, "From Random Walks")

        title = self.ly.title("Donsker's Theorem")
        items = [
            Text("Take a random walk with step size 1/sqrt(n)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Speed up time by factor n",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("As n goes to infinity, the walk converges to Brownian motion",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    def scene6_heat_equation(self):
        self.add_subcaption(
            "The probability density of Brownian motion satisfies the heat equation. "
            "This creates a deep bridge between probability theory and partial differential equations.",
            duration=11,
        )
        self.ly.section_divider(5, "Connection to Physics")

        title = self.ly.title("The Heat Equation")
        formula = MathTex(r"\frac{\partial u}{\partial t} = \frac{1}{2} \frac{\partial^2 u}{\partial x^2}",
                          font_size=BODY_SIZE, color=ACCENT)
        self.ly.formula_box(formula, ACCENT)
        self.wait(NORMAL)
        self.ly.clear()

        title2 = self.ly.title("Probability Meets PDEs")
        items = [
            Text("u(t,x) = probability density of W(t) at position x",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Expected values can be computed by solving PDEs",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(NORMAL)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Brownian motion: continuous paths, independent normal increments, "
            "linearly growing variance. Next we study martingales, which capture "
            "the idea of a fair game in probability.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("W(0) = 0, independent normal increments, continuous paths",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("E[W(t)] = 0, Var[W(t)] = t, Cov = min(s,t)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Self-similar and nowhere differentiable",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Limit of scaled random walks, connects to the heat equation",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

        play_outro(self, "Martingales", "Stochastic Processes")
