"""Video 73: Common Distributions (Continuous)
Probability & Statistics -- Video 7 of 12

Covers: Uniform, Exponential, and Normal distributions with PDFs, E[X], Var(X).
Smooth PDF curve animations, color-coded distributions, family tree bridge
from Video 72's discrete distributions.

Competitive analysis: 3B1B (7M+ CLT/Normal), jbstatistics (350K Normal, slide-based),
StatQuest (600K Normal), KA (fragmented), OCT (whiteboard, no animation).
Gap: No Manim-animated video covers Normal + Exponential + Uniform together.

Plan: planning/video-73-common-distributions-continuous.md

Render draft:  manim -ql scripts/undergraduate/video-73-common-distributions-continuous.py Video73_CommonDistributionsContinuous
Render final:  manim -qh scripts/undergraduate/video-73-common-distributions-continuous.py Video73_CommonDistributionsContinuous
"""

from manim import *
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits

# Distribution color palette (unique per distribution)
UNIFORM_COL     = ACCENT      # #FFD166
EXPONENTIAL_COL = SECONDARY   # #7BC950
NORMAL_COL      = PRIMARY      # #5BC0EB

ORANGE = "#FF8C42"


def _plot_pdf_curve(
    title_str,
    func,
    x_range,
    y_range,
    color,
    param_label="",
):
    """Create a labeled PDF curve plot VGroup."""
    title_mob = Text(title_str, font_size=LABEL_SIZE, color=color, font=SANS)

    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        axis_config={
            "color": DIM,
            "stroke_width": 1.5,
            "include_numbers": False,
            "font_size": SMALL_SIZE,
        },
        x_length=5.0,
        y_length=2.5,
    ).set_opacity(0.7)

    curve = axes.plot(func, color=color, stroke_width=3)

    grp = VGroup(title_mob, axes, curve)
    grp.arrange(DOWN, buff=0.25)
    if param_label:
        plbl = Text(param_label, font_size=SMALL_SIZE, color=DIM, font=MONO)
        plbl.next_to(axes, RIGHT, buff=0.15)
        grp.add(plbl)

    return grp, axes, curve


def _uniform_pdf(x, a=0, b=4):
    """Uniform PDF on [a, b]."""
    val = np.zeros_like(x)
    mask = (x >= a) & (x <= b)
    val[mask] = 1.0 / (b - a)
    return val


def _exponential_pdf(x, lam=1.0):
    """Exponential PDF with rate lambda."""
    return lam * np.exp(-lam * x)


def _normal_pdf(x, mu=0, sigma=1):
    """Normal PDF."""
    return (1.0 / (sigma * math.sqrt(2 * math.pi))) * np.exp(
        -0.5 * ((x - mu) / sigma) ** 2
    )


class Video73_CommonDistributionsContinuous(Scene):
    """Full video: Common Continuous Distributions -- Uniform, Exponential,
    Normal with PDFs, E[X], Var(X), family tree, and reference table."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_uniform()
        self.scene3_exponential()
        self.scene4_normal()
        self.scene5_family_tree()
        self.scene6_comparison()
        self.scene7_reference_table()
        self.scene8_summary()

    # ── Scene 1: Hook ────────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we explored the discrete distribution zoo: Bernoulli, "
            "Binomial, Geometric, and more. Now we cross over to the continuous "
            "world. Instead of counting outcomes, we measure them. Instead of "
            "probability mass functions, we work with probability density functions.",
            duration=20,
        )
        play_intro(self, "Common Distributions (Continuous)", "Probability & Statistics")

        title = self.ly.title("The Continuous Distribution Trio")

        dist_labels = [
            Text("Uniform", font_size=BODY_SIZE, color=UNIFORM_COL, font=SANS),
            Text("Exponential", font_size=BODY_SIZE, color=EXPONENTIAL_COL, font=SANS),
            Text("Normal", font_size=BODY_SIZE, color=NORMAL_COL, font=SANS),
        ]
        self.ly.progressive_reveal(dist_labels, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ── Scene 2: Uniform Distribution ────────────────────────────────
    def scene2_uniform(self):
        self.ly.section_divider(1, "Uniform Distribution")

        self.add_subcaption(
            "The Uniform distribution is the simplest continuous distribution, "
            "just as Bernoulli was the simplest discrete one. Every value in "
            "an interval is equally likely. Think of waiting for a bus that "
            "could arrive at any time within the next ten minutes.",
            duration=25,
        )
        title = self.ly.title("Uniform: Every Value Equally Likely", color=UNIFORM_COL)

        items = [
            Text("All outcomes in [a, b] equally likely", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"f(x) = \frac{1}{b-a}, \quad a \le x \le b", color=UNIFORM_COL),
            MathTex(r"E[X] = \frac{a+b}{2}", color=ACCENT),
            MathTex(r"\text{Var}(X) = \frac{(b-a)^2}{12}", color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Uniform PDF visualization
        self.add_subcaption(
            "The probability density function is a flat rectangle. The height "
            "equals one over the width, so the total area under the curve is "
            "exactly one. As the interval grows wider, the density shrinks lower.",
            duration=20,
        )
        title2 = self.ly.title("Uniform PDF", color=UNIFORM_COL)

        grp, axes, curve = _plot_pdf_curve(
            "a = 0, b = 4",
            lambda x: _uniform_pdf(x, 0, 4),
            x_range=[-1, 6, 1],
            y_range=[0, 0.4, 0.1],
            color=UNIFORM_COL,
        )
        self.ly.safe_place(grp, DOWN, anchor=title2, buff=0.5)
        self.play(Create(axes), run_time=FAST)
        self.play(Create(curve), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 3: Exponential Distribution ────────────────────────────
    def scene3_exponential(self):
        self.ly.section_divider(2, "Exponential Distribution")

        self.add_subcaption(
            "The Exponential distribution models waiting time. If events "
            "occur according to a Poisson process, then the time between "
            "consecutive events follows an Exponential distribution. A "
            "higher lambda means shorter average waits.",
            duration=25,
        )
        title = self.ly.title("Exponential: The Waiting Time", color=EXPONENTIAL_COL)

        items = [
            Text("Time between Poisson events (rate \u03bb)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"f(x) = \lambda\, e^{-\lambda x}, \quad x \ge 0", color=EXPONENTIAL_COL),
            MathTex(r"E[X] = \frac{1}{\lambda}", color=ACCENT),
            MathTex(r"\text{Var}(X) = \frac{1}{\lambda^2}", color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Exponential PDF visualization
        self.add_subcaption(
            "The curve starts at lambda when x is zero and decays "
            "exponentially. A small lambda gives a gentle, spread-out "
            "decay. A large lambda gives a steep, concentrated peak. "
            "This distribution has the memoryless property: the past "
            "does not affect the future.",
            duration=25,
        )
        title2 = self.ly.title("Exponential PDF (\u03bb = 1)", color=EXPONENTIAL_COL)

        grp, axes, curve = _plot_pdf_curve(
            "",
            lambda x: _exponential_pdf(x, 1.0),
            x_range=[-0.5, 5, 1],
            y_range=[0, 1.2, 0.3],
            color=EXPONENTIAL_COL,
            param_label="\u03bb = 1",
        )
        self.ly.safe_place(grp, DOWN, anchor=title2, buff=0.5)
        self.play(Create(axes), run_time=FAST)
        self.play(Create(curve), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Memoryless property
        self.add_subcaption(
            "A beautiful property: if you have already waited s units of time, "
            "the remaining wait has the same distribution as if you had just "
            "started. This is called the memoryless property, and the "
            "Exponential distribution is the ONLY continuous distribution "
            "with this feature.",
            duration=25,
        )
        title3 = self.ly.title("Memoryless Property", color=EXPONENTIAL_COL)
        items2 = [
            MathTex(r"P(X > s + t \mid X > s) = P(X > t)", color=EXPONENTIAL_COL),
            Text("The past does not affect the remaining wait", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title3)
        self.wait(1)
        self.ly.clear()

    # ── Scene 4: Normal Distribution ───────────────────────────────
    def scene4_normal(self):
        self.ly.section_divider(3, "Normal Distribution")

        self.add_subcaption(
            "The Normal distribution is the most important distribution in "
            "all of statistics. It appears everywhere: heights, measurement "
            "errors, stock returns. Two parameters completely describe it: "
            "mu controls the center and sigma controls the spread.",
            duration=25,
        )
        title = self.ly.title("Normal: The Bell Curve", color=NORMAL_COL)

        items = [
            Text("Two parameters: \u03bc (center) and \u03c3 (spread)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}", color=NORMAL_COL),
            MathTex(r"E[X] = \mu, \quad \text{Var}(X) = \sigma^2", color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Normal PDF visualization
        self.add_subcaption(
            "The classic bell curve. Here is the standard normal with "
            "mu equals zero and sigma equals one. Notice how most of the "
            "area is concentrated near the center. The curve never touches "
            "the horizontal axis, extending to infinity in both directions.",
            duration=20,
        )
        title2 = self.ly.title("Standard Normal: \u03bc=0, \u03c3=1", color=NORMAL_COL)

        grp, axes, curve = _plot_pdf_curve(
            "",
            lambda x: _normal_pdf(x, 0, 1),
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            color=NORMAL_COL,
            param_label="\u03bc=0, \u03c3=1",
        )
        self.ly.safe_place(grp, DOWN, anchor=title2, buff=0.5)
        self.play(Create(axes), run_time=FAST)
        self.play(Create(curve), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # 68-95-99.7 Rule
        self.add_subcaption(
            "The empirical rule tells us that approximately sixty-eight "
            "percent of the data falls within one sigma, ninety-five percent "
            "within two sigma, and ninety-nine point seven percent within "
            "three sigma. This is one of the most useful facts in statistics.",
            duration=25,
        )
        title3 = self.ly.title("The 68-95-99.7 Rule", color=NORMAL_COL)

        grp2, axes2, curve2 = _plot_pdf_curve(
            "",
            lambda x: _normal_pdf(x, 0, 1),
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            color=NORMAL_COL,
        )

        # Shade the sigma regions
        sigma_regions = VGroup()
        for lo, hi, alpha, col in [
            (-1, 1, 0.3, NORMAL_COL),
            (-2, 2, 0.15, SECONDARY),
            (-3, 3, 0.08, ACCENT),
        ]:
            region = axes2.get_area(
                curve2, x_range=[lo, hi],
                color=col, opacity=alpha,
            )
            sigma_regions.add(region)

        labels_vg = VGroup()
        for y_off, lbl_text in [
            (0.15, "68%"),
            (0.05, "95%"),
            (-0.05, "99.7%"),
        ]:
            lbl = Text(lbl_text, font_size=SMALL_SIZE, color=WHITE, font=MONO)
            lbl.move_to(axes2.c2p(0, y_off))
            labels_vg.add(lbl)

        self.ly.safe_place(grp2, DOWN, anchor=title3, buff=0.4)
        self.play(Create(axes2), run_time=FAST)
        self.play(Create(curve2), run_time=NORMAL)
        self.play(
            FadeIn(sigma_regions[0]),
            FadeIn(labels_vg[0]),
            run_time=1.0,
        )
        self.wait(0.3)
        self.play(
            FadeIn(sigma_regions[1]),
            FadeIn(labels_vg[1]),
            run_time=0.8,
        )
        self.wait(0.3)
        self.play(
            FadeIn(sigma_regions[2]),
            FadeIn(labels_vg[2]),
            run_time=0.8,
        )
        self.wait(1.5)
        self.ly.clear()

        # Standardization
        self.add_subcaption(
            "Any Normal distribution can be standardized by subtracting mu "
            "and dividing by sigma. The result is the standard normal Z with "
            "mean zero and variance one. This trick lets us use a single "
            "table for all Normal distributions.",
            duration=20,
        )
        title4 = self.ly.title("Standardization", color=NORMAL_COL)
        items3 = [
            MathTex(r"Z = \frac{X - \mu}{\sigma}", color=NORMAL_COL),
            Text("Z ~ N(0, 1)", font_size=BODY_SIZE, color=WHITE, font=MONO),
            Text("Use one table for all Normal distributions", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items3, start_from=title4)
        self.wait(1)
        self.ly.clear()

    # ── Scene 5: Continuous Family Tree ─────────────────────────────
    def scene5_family_tree(self):
        self.add_subcaption(
            "Just as the discrete distributions form a family tree, so do "
            "the continuous ones. The Uniform is the simplest, like Bernoulli "
            "was. Poisson events give birth to Exponential waiting times. "
            "The Central Limit Theorem makes the Normal appear everywhere. "
            "And these two worlds, discrete and continuous, are deeply connected.",
            duration=35,
        )
        title = self.ly.title("The Continuous Family Tree")

        # Top row: Uniform (simplest)
        unif = Text("Uniform", font_size=HEADING_SIZE, color=UNIFORM_COL, font=SANS)
        self.ly.center_in_content(unif)
        unif.shift(UP * 2.5)
        self.play(Write(unif), run_time=NORMAL)

        lbl_simple = Text("simplest continuous", font_size=SMALL_SIZE, color=DIM, font=SANS)
        lbl_simple.next_to(unif, DOWN, buff=0.1)
        self.play(FadeIn(lbl_simple, shift=UP * 0.1), run_time=FAST)

        # Middle row: Exponential, Normal
        expo = Text("Exponential", font_size=HEADING_SIZE, color=EXPONENTIAL_COL, font=SANS)
        norm = Text("Normal", font_size=HEADING_SIZE, color=NORMAL_COL, font=SANS)
        row2 = VGroup(expo, norm).arrange(RIGHT, buff=3.0)
        row2.shift(DOWN * 0.3)
        self.ly.center_in_content(row2)

        self.play(Write(expo), Write(norm), run_time=NORMAL)

        # Arrows from Uniform
        arr_e = Arrow(unif.get_bottom(), expo.get_top(), buff=0.15, color=EXPONENTIAL_COL, stroke_width=2)
        arr_n = Arrow(unif.get_bottom(), norm.get_top(), buff=0.15, color=NORMAL_COL, stroke_width=2)
        lbl_e = Text("Poisson gaps", font_size=SMALL_SIZE, color=DIM, font=SANS).next_to(arr_e, LEFT, buff=0.1)
        lbl_n = Text("CLT limit", font_size=SMALL_SIZE, color=DIM, font=SANS).next_to(arr_n, RIGHT, buff=0.1)

        self.play(
            Create(arr_e), Create(arr_n),
            FadeIn(lbl_e, shift=LEFT * 0.1), FadeIn(lbl_n, shift=LEFT * 0.1),
            run_time=1.5,
        )
        self.wait(0.5)

        # Bridge to Video 72's discrete tree
        bridge_title = Text("Discrete \u2192 Continuous Bridge", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        bridge_row = VGroup(
            Text("Poisson \u2192 Exponential", font_size=SMALL_SIZE, color=EXPONENTIAL_COL, font=MONO),
            Text("Binomial \u2192 Normal (CLT)", font_size=SMALL_SIZE, color=NORMAL_COL, font=MONO),
            Text("Bernoulli \u2248 Uniform (simplest)", font_size=SMALL_SIZE, color=UNIFORM_COL, font=MONO),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        bridge_grp = VGroup(bridge_title, bridge_row).arrange(DOWN, buff=0.3)
        bridge_grp.shift(DOWN * 1.8)
        self.ly.center_in_content(bridge_grp)

        self.play(Write(bridge_title), run_time=FAST)
        self.play(
            *[FadeIn(r, shift=LEFT * 0.1) for r in bridge_row],
            run_time=1.5,
            lag_ratio=0.3,
        )
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Side-by-Side Comparison ──────────────────────────────
    def scene6_comparison(self):
        self.add_subcaption(
            "Let us compare all three distributions side by side. "
            "The Uniform is flat, the Exponential decays from left to right, "
            "and the Normal is symmetric. Each has a different support: "
            "finite, half-infinite, and infinite.",
            duration=25,
        )
        title = self.ly.title("Side-by-Side Comparison")

        # Shared axes for all three curves
        comp_axes = Axes(
            x_range=[-4, 6, 1],
            y_range=[0, 0.55, 0.1],
            axis_config={
                "color": DIM,
                "stroke_width": 1.5,
                "include_numbers": False,
                "font_size": SMALL_SIZE,
            },
            x_length=7.5,
            y_length=3.0,
        ).set_opacity(0.7)

        norm_curve = comp_axes.plot(
            lambda x: _normal_pdf(x, 0, 1),
            color=NORMAL_COL, stroke_width=3,
        )
        expo_curve = comp_axes.plot(
            lambda x: np.where(x >= 0, _exponential_pdf(x, 1.0), 0),
            color=EXPONENTIAL_COL, stroke_width=3,
        )
        unif_curve = comp_axes.plot(
            lambda x: _uniform_pdf(x, 1, 3),
            color=UNIFORM_COL, stroke_width=3,
        )

        # Legend
        legend = VGroup(
            VGroup(
                Line(LEFT * 0.4, RIGHT * 0.4, color=NORMAL_COL, stroke_width=3),
                Text("Normal", font_size=SMALL_SIZE, color=NORMAL_COL, font=MONO),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Line(LEFT * 0.4, RIGHT * 0.4, color=EXPONENTIAL_COL, stroke_width=3),
                Text("Exponential", font_size=SMALL_SIZE, color=EXPONENTIAL_COL, font=MONO),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Line(LEFT * 0.4, RIGHT * 0.4, color=UNIFORM_COL, stroke_width=3),
                Text("Uniform", font_size=SMALL_SIZE, color=UNIFORM_COL, font=MONO),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        comp_grp = VGroup(comp_axes, legend).arrange(RIGHT, buff=0.6)
        self.ly.safe_place(comp_grp, DOWN, anchor=title, buff=0.4)

        self.play(Create(comp_axes), run_time=FAST)
        self.play(Create(norm_curve), run_time=NORMAL)
        self.wait(0.3)
        self.play(Create(expo_curve), run_time=NORMAL)
        self.wait(0.3)
        self.play(Create(unif_curve), run_time=NORMAL)
        self.play(FadeIn(legend, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)
        self.ly.clear()

    # ── Scene 7: Quick Reference Table ──────────────────────────────
    def scene7_reference_table(self):
        self.add_subcaption(
            "Here is your quick reference for all three continuous "
            "distributions. For each one you have the probability density "
            "function, the expected value, the variance, and the support. "
            "Keep this alongside the discrete reference from last time.",
            duration=25,
        )
        title = self.ly.title("Quick Reference", color=PRIMARY)

        # Build rows progressively
        rows_data = [
            (UNIFORM_COL, "Uniform", r"\frac{1}{b-a}", r"\frac{a+b}{2}", r"\frac{(b-a)^2}{12}", "[a, b]"),
            (EXPONENTIAL_COL, "Exponential", r"\lambda e^{-\lambda x}", r"\frac{1}{\lambda}", r"\frac{1}{\lambda^2}", "[0, \infty)"),
            (NORMAL_COL, "Normal", r"\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}", r"\mu", r"\sigma^2", r"(-\infty, \infty)"),
        ]

        all_rows = []
        for col, name, pdf, ex, vr, sup in rows_data:
            row = VGroup(
                Text(name, font_size=SMALL_SIZE, color=col, font=MONO),
                MathTex(pdf, color=WHITE, font_size=18),
                MathTex(ex, color=ACCENT, font_size=18),
                MathTex(vr, color=ACCENT, font_size=18),
                Text(sup, font_size=SMALL_SIZE, color=DIM, font=MONO),
            ).arrange(RIGHT, buff=0.25)
            all_rows.append(row)

        # Show header
        header = VGroup(
            Text("Dist.", font_size=SMALL_SIZE, color=DIM, font=MONO),
            Text("PDF", font_size=SMALL_SIZE, color=DIM, font=MONO),
            Text("E[X]", font_size=SMALL_SIZE, color=DIM, font=MONO),
            Text("Var(X)", font_size=SMALL_SIZE, color=DIM, font=MONO),
            Text("Support", font_size=SMALL_SIZE, color=DIM, font=MONO),
        ).arrange(RIGHT, buff=0.25)
        header.next_to(title, DOWN, buff=0.5)
        ensure_fits(header)
        self.play(FadeIn(header, shift=LEFT * 0.15), run_time=FAST)

        # Reveal rows one by one
        for i, row in enumerate(all_rows):
            ensure_fits(row)
            row.next_to(header, DOWN, buff=0.3 * (i + 1))
            self.play(FadeIn(row, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(0.3)

        self.wait(1.5)
        self.ly.clear()

    # ── Scene 8: Summary + Outro ────────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "These three distributions cover most of the continuous random "
            "variables you will encounter. Uniform for equally likely intervals, "
            "Exponential for waiting times, and Normal for natural phenomena. "
            "Together with the six discrete distributions from last time, you "
            "now have a complete toolkit for modelling randomness.",
            duration=25,
        )

        title = self.ly.title("Summary")

        items = [
            Text("Uniform: flat, finite interval, simplest continuous", font_size=BODY_SIZE, color=UNIFORM_COL, font=SANS),
            Text("Exponential: waiting times, memoryless, right-skewed", font_size=BODY_SIZE, color=EXPONENTIAL_COL, font=SANS),
            Text("Normal: the bell curve, central limit theorem, everywhere", font_size=BODY_SIZE, color=NORMAL_COL, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)
        play_outro(self, "Joint Distributions", "Probability & Statistics")
        self.ly.clear()
