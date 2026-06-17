"""Video 72: Common Distributions (Discrete)
Probability & Statistics -- Video 6 of 12

Covers: Bernoulli, Binomial, Geometric, Negative Binomial,
Hypergeometric, and Poisson distributions with PMFs, E[X], Var(X).

Competitive analysis: 3B1B (2.58M binomial), jbstatistics (333-599K each),
StatQuest (608K), OCT (597K geometric), Primer (1.52M binomial), KA (553K).
Plan: planning/video-72-common-distributions-discrete.md

Render draft:  manim -ql scripts/undergraduate/video-72-common-distributions-discrete.py Video72_CommonDistributionsDiscrete
Render final:  manim -qh scripts/undergraduate/video-72-common-distributions-discrete.py Video72_CommonDistributionsDiscrete
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
BERNOULLI_COL = PRIMARY     # #5BC0EB
BINOMIAL_COL  = SECONDARY   # #7BC950
GEOMETRIC_COL = ACCENT      # #FFD166
NEGBIN_COL    = RED         # #EF476F
HYPERGEO_COL  = DIM         # #6B6B8D
POISSON_COL   = ORANGE      # #FF8C42


def _bar_chart_labels(title_str, x_vals, heights, bar_color, max_height=2.5):
    """Create a simple labeled bar chart VGroup for a PMF."""
    title_mob = Text(title_str, font_size=LABEL_SIZE, color=bar_color, font=SANS)
    bars = VGroup()
    labels = VGroup()
    bar_w = 0.35
    gap = 0.12
    total_w = len(x_vals) * (bar_w + gap) - gap

    for i, (x, h) in enumerate(zip(x_vals, heights)):
        bar_h = max(0.08, h * max_height)
        bar = Rectangle(
            width=bar_w, height=bar_h,
            fill_color=bar_color, fill_opacity=0.8,
            stroke_color=bar_color, stroke_width=1,
        )
        bar.move_to(UP * bar_h / 2)
        lbl = Text(str(x), font_size=SMALL_SIZE, color=WHITE, font=MONO)
        lbl.next_to(bar, DOWN, buff=0.05)
        bars.add(bar)
        labels.add(lbl)

    bars.arrange(RIGHT, buff=gap)
    labels.arrange(RIGHT, buff=gap)
    labels.next_to(bars, DOWN, buff=0.05)
    grp = VGroup(title_mob, bars, labels).arrange(DOWN, buff=0.2)
    return grp, bars


class Video72_CommonDistributionsDiscrete(Scene):
    """Full video: Common Discrete Distributions -- Bernoulli, Binomial,
    Geometric, Negative Binomial, Hypergeometric, Poisson."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_bernoulli()
        self.scene3_binomial()
        self.scene4_geometric()
        self.scene5_negative_binomial()
        self.scene6_hypergeometric()
        self.scene7_poisson()
        self.scene8_family_tree()
        self.scene9_reference_table()
        self.scene10_summary()

    # ── Scene 1: Hook ────────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "You have learned what random variables are and how to compute "
            "expectation and variance. Now the question is: which specific "
            "distributions do we actually use in practice?",
            duration=18,
        )
        play_intro(self, "Common Distributions (Discrete)", "Probability & Statistics")

        title = self.ly.title("The Discrete Distribution Zoo")

        dist_labels = [
            Text("Bernoulli", font_size=BODY_SIZE, color=BERNOULLI_COL, font=SANS),
            Text("Binomial", font_size=BODY_SIZE, color=BINOMIAL_COL, font=SANS),
            Text("Geometric", font_size=BODY_SIZE, color=GEOMETRIC_COL, font=SANS),
            Text("Neg. Binomial", font_size=BODY_SIZE, color=NEGBIN_COL, font=SANS),
            Text("Hypergeometric", font_size=BODY_SIZE, color=HYPERGEO_COL, font=SANS),
            Text("Poisson", font_size=BODY_SIZE, color=POISSON_COL, font=SANS),
        ]
        self.ly.progressive_reveal(dist_labels, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ── Scene 2: Bernoulli ───────────────────────────────────────────
    def scene2_bernoulli(self):
        self.ly.section_divider(1, "Bernoulli Distribution")

        self.add_subcaption(
            "The Bernoulli distribution is the simplest of all. It models "
            "a single trial with exactly two outcomes: success or failure. "
            "Think of flipping one coin.",
            duration=20,
        )
        title = self.ly.title("Bernoulli: The Simplest Trial", color=BERNOULLI_COL)

        items = [
            Text("One trial, two outcomes: success (1) or failure (0)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"P(X = 1) = p", color=BERNOULLI_COL),
            MathTex(r"P(X = 0) = 1 - p", color=BERNOULLI_COL),
            MathTex(r"E[X] = p", color=ACCENT),
            MathTex(r"\text{Var}(X) = p(1-p)", color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Bernoulli PMF bars
        self.add_subcaption(
            "Here is what the probability mass function looks like. "
            "Two bars, one at zero and one at one, whose heights sum to one.",
            duration=16,
        )
        title2 = self.ly.title("Bernoulli PMF", color=BERNOULLI_COL)
        chart, bars = _bar_chart_labels(
            "p = 0.3", [0, 1], [0.7, 0.3], BERNOULLI_COL
        )
        self.ly.safe_place(chart, DOWN, anchor=title2, buff=0.6)
        self.play(Create(bars), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 3: Binomial ────────────────────────────────────────────
    def scene3_binomial(self):
        self.ly.section_divider(2, "Binomial Distribution")

        self.add_subcaption(
            "If you repeat a Bernoulli trial n independent times and count "
            "the total number of successes, you get a Binomial distribution. "
            "This is one of the most important distributions in all of statistics.",
            duration=25,
        )
        title = self.ly.title("Binomial: Counting Successes", color=BINOMIAL_COL)

        items = [
            Text("n independent Bernoulli trials, each with prob. p", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"P(X=k) = \binom{n}{k}\, p^k\, (1-p)^{n-k}", color=BINOMIAL_COL),
            MathTex(r"E[X] = np", color=ACCENT),
            MathTex(r"\text{Var}(X) = np(1-p)", color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Binomial PMF example
        self.add_subcaption(
            "For example, with ten coin flips and a fair coin, the distribution "
            "of the number of heads forms a symmetric bell shape centered at five. "
            "The probability of exactly seven heads is about twelve percent.",
            duration=25,
        )
        title2 = self.ly.title("Example: n=10, p=0.5", color=BINOMIAL_COL)

        # Build binomial PMF bars manually for n=10, p=0.5
        from math import comb
        probs = [comb(10, k) * 0.5**10 for k in range(11)]
        bar_w = 0.4
        gap = 0.1
        bars = VGroup()
        max_p = max(probs)
        bar_h_scale = 2.5

        for k in range(11):
            bh = max(0.08, (probs[k] / max_p) * bar_h_scale)
            bar = Rectangle(
                width=bar_w, height=bh,
                fill_color=BINOMIAL_COL, fill_opacity=0.8,
                stroke_color=BINOMIAL_COL, stroke_width=1,
            )
            bar.move_to(UP * bh / 2 + LEFT * 0.1)
            lbl = Text(str(k), font_size=SMALL_SIZE - 2, color=DIM, font=MONO)
            lbl.next_to(bar, DOWN, buff=0.03)
            bars.add(VGroup(bar, lbl))

        bars.arrange(RIGHT, buff=gap)
        self.ly.safe_place(bars, DOWN, anchor=title2, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.08), run_time=2.5)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 4: Geometric ───────────────────────────────────────────
    def scene4_geometric(self):
        self.ly.section_divider(3, "Geometric Distribution")

        self.add_subcaption(
            "The Geometric distribution answers a different question: how many "
            "trials do I need until my first success? It produces an "
            "exponential decay shape, because waiting gets less likely over time.",
            duration=25,
        )
        title = self.ly.title("Geometric: Waiting for Success", color=GEOMETRIC_COL)

        items = [
            Text("Count trials until the FIRST success", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"P(X=k) = (1-p)^{k-1}\, p", color=GEOMETRIC_COL),
            MathTex(r"E[X] = \frac{1}{p}", color=ACCENT),
            MathTex(r"\text{Var}(X) = \frac{1-p}{p^2}", color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Geometric example
        self.add_subcaption(
            "For instance, if you roll a fair die until you get a six, the "
            "expected number of rolls is six. The probability mass function "
            "decays exponentially: five sixths chance of failing each roll.",
            duration=25,
        )
        title2 = self.ly.title("Example: Roll until 6 (p = 1/6)", color=GEOMETRIC_COL)

        # Exponential decay bars for geometric p=1/6
        p_geo = 1.0 / 6.0
        geo_vals = [p_geo * (1 - p_geo)**(k) for k in range(8)]
        max_g = max(geo_vals)
        bars_g = VGroup()
        bar_w = 0.5
        gap = 0.1

        for k in range(8):
            bh = max(0.08, (geo_vals[k] / max_g) * 2.5)
            bar = Rectangle(
                width=bar_w, height=bh,
                fill_color=GEOMETRIC_COL, fill_opacity=0.8,
                stroke_color=GEOMETRIC_COL, stroke_width=1,
            )
            bar.move_to(UP * bh / 2)
            lbl = Text(str(k + 1), font_size=SMALL_SIZE - 2, color=DIM, font=MONO)
            lbl.next_to(bar, DOWN, buff=0.03)
            bars_g.add(VGroup(bar, lbl))

        bars_g.arrange(RIGHT, buff=gap)
        self.ly.safe_place(bars_g, DOWN, anchor=title2, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in bars_g], lag_ratio=0.1), run_time=2)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 5: Negative Binomial ───────────────────────────────────
    def scene5_negative_binomial(self):
        self.ly.section_divider(4, "Negative Binomial Distribution")

        self.add_subcaption(
            "The Negative Binomial generalizes the Geometric distribution. "
            "Instead of waiting for one success, you count trials until the "
            "r-th success. When r equals one, it reduces to the Geometric.",
            duration=25,
        )
        title = self.ly.title("Negative Binomial: r-th Success", color=NEGBIN_COL)

        items = [
            Text("Count trials until the r-th success", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"P(X=k) = \binom{k-1}{r-1}\, p^r\, (1-p)^{k-r}", color=NEGBIN_COL),
            MathTex(r"E[X] = \frac{r}{p}", color=ACCENT),
            Text("r = 1 gives Geometric distribution", font_size=BODY_SIZE, color=GEOMETRIC_COL, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

    # ── Scene 6: Hypergeometric ───────────────────────────────────────
    def scene6_hypergeometric(self):
        self.ly.section_divider(5, "Hypergeometric Distribution")

        self.add_subcaption(
            "The Hypergeometric distribution models sampling WITHOUT replacement. "
            "Imagine drawing cards from a shuffled deck. Unlike the Binomial, "
            "each draw changes the probabilities of the next.",
            duration=25,
        )
        title = self.ly.title("Hypergeometric: No Replacement", color=HYPERGEO_COL)

        items = [
            Text("N total items, K successes, draw n items", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"P(X=k) = \frac{\binom{K}{k}\,\binom{N-K}{n-k}}{\binom{N}{n}}", color=HYPERGEO_COL),
            Text("Compare to Binomial (which assumes replacement)", font_size=BODY_SIZE, color=BINOMIAL_COL, font=SANS),
            Text("Use when N is small relative to n", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

    # ── Scene 7: Poisson ──────────────────────────────────────────────
    def scene7_poisson(self):
        self.ly.section_divider(6, "Poisson Distribution")

        self.add_subcaption(
            "The Poisson distribution models the number of events in a fixed "
            "interval, like emails per hour or radioactive decays per second. "
            "It arises as the limit of the Binomial when n goes to infinity "
            "and p goes to zero while their product lambda stays constant.",
            duration=30,
        )
        title = self.ly.title("Poisson: Rare Events in Time", color=POISSON_COL)

        items = [
            Text("Limit of Binomial: n → ∞, p → 0, λ = np", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"P(X=k) = \frac{\lambda^k\, e^{-\lambda}}{k!}", color=POISSON_COL),
            MathTex(r"E[X] = \lambda, \quad \text{Var}(X) = \lambda", color=ACCENT),
            Text("Approximation: n ≥ 20, np ≤ 5", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Poisson PMF bars
        self.add_subcaption(
            "Notice that the mean equals the variance for the Poisson. "
            "The shape is right-skewed for small lambda and becomes more "
            "symmetric as lambda grows. Here is the shape for lambda equal to three.",
            duration=20,
        )
        title2 = self.ly.title("Poisson PMF (λ = 3)", color=POISSON_COL)

        from math import factorial
        lam = 3.0
        pois_vals = [lam**k * math.exp(-lam) / factorial(k) for k in range(10)]
        max_pv = max(pois_vals)
        bars_p = VGroup()
        bar_w = 0.45
        gap = 0.1

        for k in range(10):
            bh = max(0.08, (pois_vals[k] / max_pv) * 2.5)
            bar = Rectangle(
                width=bar_w, height=bh,
                fill_color=POISSON_COL, fill_opacity=0.8,
                stroke_color=POISSON_COL, stroke_width=1,
            )
            bar.move_to(UP * bh / 2)
            lbl = Text(str(k), font_size=SMALL_SIZE - 2, color=DIM, font=MONO)
            lbl.next_to(bar, DOWN, buff=0.03)
            bars_p.add(VGroup(bar, lbl))

        bars_p.arrange(RIGHT, buff=gap)
        self.ly.safe_place(bars_p, DOWN, anchor=title2, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in bars_p], lag_ratio=0.08), run_time=2)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 8: Distribution Family Tree ───────────────────────────
    def scene8_family_tree(self):
        self.add_subcaption(
            "These distributions are not isolated. They form a family tree "
            "of relationships. Bernoulli is the root. Repeating it n times "
            "gives Binomial. Waiting for the first success gives Geometric. "
            "Letting the Binomial limit grow gives Poisson. This unified "
            "view is the key to choosing the right distribution.",
            duration=35,
        )
        title = self.ly.title("The Distribution Family Tree")

        # Build family tree as text-based diagram
        # Row 1: Bernoulli at top
        bern = Text("Bernoulli", font_size=HEADING_SIZE, color=BERNOULLI_COL, font=SANS)
        self.ly.center_in_content(bern)
        bern.shift(UP * 2.0)
        self.play(Write(bern), run_time=NORMAL)

        # Row 2: Binomial, Geometric
        binom = Text("Binomial", font_size=HEADING_SIZE, color=BINOMIAL_COL, font=SANS)
        geom = Text("Geometric", font_size=HEADING_SIZE, color=GEOMETRIC_COL, font=SANS)
        row2 = VGroup(binom, geom).arrange(RIGHT, buff=2.0)
        row2.shift(DOWN * 0.5)
        self.ly.center_in_content(row2)

        # Arrows from Bernoulli
        arr1 = Arrow(bern.get_bottom(), binom.get_top(), buff=0.15, color=PRIMARY, stroke_width=2)
        arr2 = Arrow(bern.get_bottom(), geom.get_top(), buff=0.15, color=PRIMARY, stroke_width=2)
        lbl_n = Text("n trials", font_size=SMALL_SIZE, color=DIM, font=SANS).next_to(arr1, RIGHT, buff=0.1)
        lbl_1st = Text("1st success", font_size=SMALL_SIZE, color=DIM, font=SANS).next_to(arr2, LEFT, buff=0.1)

        self.play(
            Create(arr1), Create(arr2),
            Write(binom), Write(geom),
            FadeIn(lbl_n, shift=LEFT * 0.1), FadeIn(lbl_1st, shift=LEFT * 0.1),
            run_time=1.5,
        )
        self.wait(0.5)

        # Row 3: NegBin, Hypergeometric, Poisson
        negb = Text("Neg. Binomial", font_size=HEADING_SIZE, color=NEGBIN_COL, font=SANS)
        hypg = Text("Hypergeometric", font_size=HEADING_SIZE, color=HYPERGEO_COL, font=SANS)
        pois = Text("Poisson", font_size=HEADING_SIZE, color=POISSON_COL, font=SANS)
        row3 = VGroup(negb, hypg, pois).arrange(RIGHT, buff=1.5)
        row3.shift(DOWN * 1.5)
        self.ly.center_in_content(row3)

        arr3 = Arrow(geom.get_bottom(), negb.get_top(), buff=0.15, color=GEOMETRIC_COL, stroke_width=2)
        arr4 = Arrow(binom.get_bottom(), hypg.get_top(), buff=0.15, color=BINOMIAL_COL, stroke_width=2)
        arr5 = Arrow(binom.get_bottom(), pois.get_top(), buff=0.15, color=BINOMIAL_COL, stroke_width=2)
        lbl_r = Text("r successes", font_size=SMALL_SIZE, color=DIM, font=SANS).next_to(arr3, RIGHT, buff=0.1)
        lbl_no = Text("no replacement", font_size=SMALL_SIZE, color=DIM, font=SANS).next_to(arr4, LEFT, buff=0.1)
        lbl_lim = Text("n → ∞", font_size=SMALL_SIZE, color=DIM, font=SANS).next_to(arr5, RIGHT, buff=0.1)

        self.play(
            Create(arr3), Create(arr4), Create(arr5),
            Write(negb), Write(hypg), Write(pois),
            FadeIn(lbl_r, shift=LEFT * 0.1),
            FadeIn(lbl_no, shift=LEFT * 0.1),
            FadeIn(lbl_lim, shift=LEFT * 0.1),
            run_time=2,
        )
        self.wait(2)
        self.ly.clear()

    # ── Scene 9: Quick Reference Table ──────────────────────────────
    def scene9_reference_table(self):
        self.add_subcaption(
            "Here is a quick reference table summarizing all six distributions. "
            "For each one you have the probability mass function, the expected "
            "value, and the variance. Keep this handy when solving problems.",
            duration=25,
        )
        title = self.ly.title("Quick Reference", color=PRIMARY)

        # Build rows progressively
        rows_data = [
            (BERNOULLI_COL, "Bernoulli", r"p^k(1\!-\!p)^{1-k}", r"p", r"p(1-p)"),
            (BINOMIAL_COL, "Binomial", r"\binom{n}{k}p^k(1\!-\!p)^{n-k}", r"np", r"np(1-p)"),
            (GEOMETRIC_COL, "Geometric", r"(1-p)^{k-1}p", r"\frac{1}{p}", r"\frac{1-p}{p^2}"),
            (NEGBIN_COL, "Neg. Binomial", r"\binom{k\!-\!1}{r\!-\!1}p^r(1\!-\!p)^{k-r}", r"\frac{r}{p}", r"\frac{r(1-p)}{p^2}"),
            (HYPERGEO_COL, "Hypergeometric", r"\frac{\binom{K}{k}\binom{N\!-\!K}{n-k}}{\binom{N}{n}}", r"n\frac{K}{N}", r"n\frac{K}{N}\frac{N\!-\!K}{N}\frac{N\!-\!n}{N\!-\!1}"),
            (POISSON_COL, "Poisson", r"\frac{\lambda^k e^{-\lambda}}{k!}", r"\lambda", r"\lambda"),
        ]

        all_rows = []
        for col, name, pmf, ex, vr in rows_data:
            row = VGroup(
                Text(name, font_size=SMALL_SIZE, color=col, font=MONO),
                MathTex(pmf, color=WHITE, font_size=22),
                MathTex(ex, color=ACCENT, font_size=22),
                MathTex(vr, color=ACCENT, font_size=22),
            ).arrange(RIGHT, buff=0.3)
            all_rows.append(row)

        # Show header
        header = VGroup(
            Text("Dist.", font_size=SMALL_SIZE, color=DIM, font=MONO),
            Text("PMF", font_size=SMALL_SIZE, color=DIM, font=MONO),
            Text("E[X]", font_size=SMALL_SIZE, color=DIM, font=MONO),
            Text("Var(X)", font_size=SMALL_SIZE, color=DIM, font=MONO),
        ).arrange(RIGHT, buff=0.3)
        header.next_to(title, DOWN, buff=0.5)
        ensure_fits(header)
        self.play(FadeIn(header, shift=LEFT * 0.15), run_time=FAST)

        # Reveal rows one by one, remove oldest when budget hit
        visible = []
        for i, row in enumerate(all_rows):
            ensure_fits(row)
            row.next_to(header, DOWN, buff=0.25 * (i + 1))
            self.play(FadeIn(row, shift=LEFT * 0.15), run_time=FAST)
            visible.append(row)
            if len(visible) > 4:
                old = visible.pop(0)
                self.play(FadeOut(old), run_time=FAST)
            self.wait(0.3)

        self.wait(1.5)
        self.ly.clear()

    # ── Scene 10: Summary + Outro ────────────────────────────────────
    def scene10_summary(self):
        self.add_subcaption(
            "These six distributions cover most of the discrete random "
            "variables you will encounter. Bernoulli is the foundation, "
            "Binomial is the workhorse, and Poisson handles rare events. "
            "Next time we will explore continuous distributions.",
            duration=25,
        )

        title = self.ly.title("Summary")

        items = [
            Text("Bernoulli: the building block (one trial)", font_size=BODY_SIZE, color=BERNOULLI_COL, font=SANS),
            Text("Binomial: count successes in n trials", font_size=BODY_SIZE, color=BINOMIAL_COL, font=SANS),
            Text("Geometric: wait for first success", font_size=BODY_SIZE, color=GEOMETRIC_COL, font=SANS),
            Text("Poisson: model rare events over time", font_size=BODY_SIZE, color=POISSON_COL, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)
        play_outro(self, "Common Distributions (Continuous)", "Probability & Statistics")
        self.ly.clear()
