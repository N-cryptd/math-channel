"""Video 78: Regression Basics
Probability & Statistics -- Video 12 of 12 (Playlist Finale)

Covers: Scatter plots, line of best fit, least squares, residuals,
normal equations derivation, worked example, R-squared, prediction,
linear algebra connection (projection), summary.

Plan: planning/video-78-regression-basics.md

Render draft:  manim -ql scripts/undergraduate/video-78-regression-basics.py Video78_RegressionBasics
Render final:  manim -qh scripts/undergraduate/video-78-regression-basics.py Video78_RegressionBasics
"""

from manim import *
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


# Data for the worked example: (hours_studied, exam_score)
DATA_POINTS = [(1, 52), (2, 63), (3, 68), (4, 78), (5, 85)]
# Means
X_BAR = 3.0
Y_BAR = 69.2
# Slope components
SXX = 10.0  # sum (xi - x_bar)^2 = 4+1+0+1+4
SXY = 58.0  # sum (xi-x_bar)(yi-y_bar) = (-2)(-17.2)+(-1)(-6.2)+0+(1)(8.8)+(2)(15.8)
SLOPE = SXY / SXX  # 5.8
INTERCEPT = Y_BAR - SLOPE * X_BAR  # 69.2 - 17.4 = 51.8


class Video78_RegressionBasics(Scene):
    """Regression Basics -- scatter plots, least squares, residuals,
    R-squared, prediction, LA connection, summary."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_line_of_best_fit()
        self.scene3_least_squares_derivation()
        self.scene4_worked_example()
        self.scene5_r_squared()
        self.scene6_prediction()
        self.scene7_la_connection()
        self.scene8_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook — Predicting the Future (1:00)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Can we predict a student's exam score from hours studied? "
            "This is the question that regression answers. "
            "We collect data, plot it, and find the best line "
            "through the points.",
            duration=11,
        )
        play_intro(self, "Regression Basics", "Probability & Statistics")

        title = self.ly.title("Predicting from Data")

        # Create scatter plot axes
        axes = Axes(
            x_range=[0, 6, 1], y_range=[40, 100, 10],
            x_length=6, y_length=4.5,
            axis_config={"color": DIM, "stroke_width": 2},
            x_axis_config={"include_numbers": True, "font_size": LABEL_SIZE},
            y_axis_config={"include_numbers": True, "font_size": LABEL_SIZE},
        ).shift(DOWN * 0.3)
        ensure_fits(axes)

        x_label = Text("Hours Studied", font_size=SMALL_SIZE, color=DIM, font=SANS)
        x_label.next_to(axes.x_axis, RIGHT, buff=0.3)
        y_label = Text("Score", font_size=SMALL_SIZE, color=DIM, font=SANS)
        y_label.next_to(axes.y_axis, UP, buff=0.2)

        self.ly.safe_place(axes, direction=DOWN, anchor=title, buff=0.4)

        self.play(Create(axes), run_time=FAST)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=FAST)

        # Plot data points one by one
        dots = VGroup()
        for x, y in DATA_POINTS:
            dot = Dot(axes.c2p(x, y), radius=0.08, color=PRIMARY)
            dots.add(dot)
            self.play(FadeIn(dot), run_time=0.3)

        self.wait(1)
        question = Text(
            "What line fits these points best?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        question.next_to(axes, DOWN, buff=0.3)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: The Line of Best Fit (1:30)
    # ------------------------------------------------------------------
    def scene2_line_of_best_fit(self):
        self.add_subcaption(
            "The line of best fit minimizes the total error. "
            "For each data point, the error is the vertical distance "
            "from the point to the line, called a residual. "
            "We minimize the sum of squared residuals.",
            duration=13,
        )

        self.ly.section_divider(2, "The Line of Best Fit")

        title = self.ly.title("Minimizing Residuals")

        # Show the cost function
        cost_label = Text(
            "Cost function (Sum of Squared Residuals):",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(cost_label, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(cost_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        cost_formula = MathTex(
            r"S = \sum_{i=1}^{n} \left( y_i - (mx_i + b) \right)^2",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(cost_formula, direction=DOWN, anchor=cost_label, buff=0.5)
        self.play(Write(cost_formula), run_time=SLOW)
        self.wait(1)

        # Show residuals visually
        residuals_label = Text(
            "Residual = observed - predicted",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(residuals_label, direction=DOWN, anchor=cost_formula, buff=0.5)
        self.play(FadeIn(residuals_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        residual_formula = MathTex(
            r"e_i = y_i - \hat{y}_i",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(residual_formula, direction=DOWN, anchor=residuals_label, buff=0.5)
        self.play(Write(residual_formula), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Least Squares Derivation (1:30)
    # ------------------------------------------------------------------
    def scene3_least_squares_derivation(self):
        self.add_subcaption(
            "To minimize the sum of squared residuals, we take "
            "partial derivatives with respect to m and b, "
            "and set them equal to zero. This gives us the "
            "normal equations, whose solution yields the slope "
            "and intercept formulas.",
            duration=15,
        )

        self.ly.section_divider(3, "Least Squares Derivation")

        title = self.ly.title("Solving for the Best Line")

        items = [
            MathTex(
                r"\frac{\partial S}{\partial m} = 0",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\frac{\partial S}{\partial b} = 0",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "This gives the normal equations:",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

        # Show final formulas
        title2 = self.ly.title("Slope and Intercept Formulas")

        slope_formula = MathTex(
            r"m = \frac{S_{xy}}{S_{xx}} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(slope_formula, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(slope_formula), run_time=SLOW)
        self.wait(1)

        intercept_formula = MathTex(
            r"b = \bar{y} - m\bar{x}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(intercept_formula, direction=DOWN, anchor=slope_formula, buff=0.6)
        self.play(Write(intercept_formula), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Worked Example (2:00)
    # ------------------------------------------------------------------
    def scene4_worked_example(self):
        self.add_subcaption(
            "Let's work through an example. Five students study "
            "different hours and get these exam scores. We compute "
            "the means, then S-xx and S-xy, and finally "
            "the slope and intercept of our regression line.",
            duration=15,
        )

        self.ly.section_divider(4, "Worked Example")

        title = self.ly.title("Example: Study Hours vs. Score")

        # Show data
        data_text = Text(
            "Data: (1,52)  (2,63)  (3,68)  (4,78)  (5,85)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(data_text, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(data_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        means_text = Text(
            "x-bar = 3.0    y-bar = 69.2",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(means_text, direction=DOWN, anchor=data_text, buff=0.4)
        self.play(FadeIn(means_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        sxx_text = Text(
            "Sxx = 10.0    Sxy = 58.0",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(sxx_text, direction=DOWN, anchor=means_text, buff=0.4)
        self.play(FadeIn(sxx_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Result
        result = MathTex(
            r"\hat{y} = 5.8x + 51.8",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=sxx_text, buff=0.5)
        self.play(Write(result), run_time=SLOW)
        self.wait(2)

        self.ly.clear()

        # Plot the result
        title2 = self.ly.title("The Regression Line")

        axes = Axes(
            x_range=[0, 6, 1], y_range=[40, 100, 10],
            x_length=6, y_length=4.5,
            axis_config={"color": DIM, "stroke_width": 2},
            x_axis_config={"include_numbers": True, "font_size": LABEL_SIZE},
            y_axis_config={"include_numbers": True, "font_size": LABEL_SIZE},
        ).shift(DOWN * 0.3)
        ensure_fits(axes)
        self.ly.safe_place(axes, direction=DOWN, anchor=title2, buff=0.4)

        self.play(Create(axes), run_time=FAST)

        # Plot data points
        dots = VGroup()
        for x, y in DATA_POINTS:
            dot = Dot(axes.c2p(x, y), radius=0.08, color=PRIMARY)
            dots.add(dot)
        self.play(FadeIn(dots), run_time=NORMAL)

        # Draw regression line
        line = Line(
            axes.c2p(0.5, 5.8 * 0.5 + 51.8),
            axes.c2p(5.5, 5.8 * 5.5 + 51.8),
            color=SECONDARY, stroke_width=3,
        )
        self.play(Create(line), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: R-squared (1:30)
    # ------------------------------------------------------------------
    def scene5_r_squared(self):
        self.add_subcaption(
            "How well does our line fit the data? R-squared measures "
            "the proportion of variance explained. "
            "Total variation splits into variation explained by the "
            "regression line, plus unexplained residual variation. "
            "R-squared ranges from 0 to 1, higher is better.",
            duration=16,
        )

        self.ly.section_divider(5, "Goodness of Fit: R-squared")

        title = self.ly.title("How Well Does the Line Fit?")

        # SST = SSR + SSE decomposition
        sst = MathTex(
            r"SST = SSR + SSE",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(sst, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(sst), run_time=SLOW)
        self.wait(0.5)

        items = [
            MathTex(
                r"SST = \sum (y_i - \bar{y})^2",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"SSR = \sum (\hat{y}_i - \bar{y})^2",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"SSE = \sum (y_i - \hat{y}_i)^2",
                font_size=BODY_SIZE, color=RED,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=sst)
        self.wait(1)
        self.ly.clear()

        # R-squared formula
        title2 = self.ly.title("R-squared")

        rsq_formula = MathTex(
            r"R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(rsq_formula, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(rsq_formula), run_time=SLOW)
        self.wait(0.5)

        items2 = [
            Text(
                "R-squared = proportion of variance explained",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "R-squared = 1: perfect fit",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "R-squared = 0: line explains nothing",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items2, start_from=rsq_formula)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Prediction and Uncertainty (1:30)
    # ------------------------------------------------------------------
    def scene6_prediction(self):
        self.add_subcaption(
            "Once we have the regression line, we can make predictions. "
            "But every prediction has uncertainty. "
            "Points far from the mean are harder to predict accurately. "
            "This connects to the confidence intervals we learned earlier.",
            duration=15,
        )

        self.ly.section_divider(6, "Prediction")

        title = self.ly.title("Making Predictions")

        # Prediction formula
        pred_formula = MathTex(
            r"\hat{y} = 5.8x + 51.8",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(pred_formula, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(pred_formula), run_time=NORMAL)
        self.wait(0.5)

        items = [
            Text(
                "Predict for x = 4: y-hat = 5.8(4) + 51.8 = 75.0",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Actual was 78: residual = +3",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Predictions more uncertain far from x-bar",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=pred_formula)
        self.wait(1)

        self.ly.clear()

        # Warning about extrapolation
        title2 = self.ly.title("Caution: Extrapolation")

        items2 = [
            Text(
                "Predictions are only reliable within the data range",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Extrapolation: predicting outside observed x values",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Regression shows association, not causation",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Linear Algebra Connection (1:00)
    # ------------------------------------------------------------------
    def scene7_la_connection(self):
        self.add_subcaption(
            "There is a beautiful connection to linear algebra. "
            "Regression is equivalent to projecting the observation "
            "vector onto the column space of the design matrix. "
            "The normal equations become A-transpose-A times "
            "x-hat equals A-transpose-b.",
            duration=16,
        )

        self.ly.section_divider(7, "Linear Algebra Connection")

        title = self.ly.title("Regression as Projection")

        items = [
            Text(
                "Design matrix A: columns of x-values and ones",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Observation vector b: the y-values",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            MathTex(
                r"A^T A \hat{\beta} = A^T b",
                font_size=HEADING_SIZE, color=ACCENT,
            ),
            Text(
                "Same normal equations! (Videos 33-34)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary + Outro (1:00)
    # ------------------------------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "That completes our journey through probability and "
            "statistics. We covered probability spaces, conditional "
            "probability, random variables, distributions, "
            "estimation, hypothesis testing, and now regression. "
            "Thank you for watching this playlist!",
            duration=17,
        )

        title = self.ly.title("Regression Recap")

        items = [
            Text(
                "Scatter plot the data, find the linear trend",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Least squares: minimize sum of squared residuals",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "R-squared: how much variance the line explains",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Predict with caution: watch out for extrapolation",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Regression is projection (Linear Algebra connection)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

        # Outro — end of playlist
        play_outro(
            self,
            next_video="",
            next_playlist="",
        )

        # End-of-playlist message
        complete_text = Text(
            "Probability & Statistics — Complete!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.play(Write(complete_text), run_time=NORMAL)
        self.wait(1)

        topics_text = Text(
            "12 videos: from probability spaces to regression",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(topics_text, direction=DOWN, anchor=complete_text, buff=0.4)
        self.play(FadeIn(topics_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
