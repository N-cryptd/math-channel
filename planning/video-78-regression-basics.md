# Video 78: Regression Basics
## Probability & Statistics — Video 12 of 12 (Playlist Finale)

**Predecessor:** Video 77 (Hypothesis Testing)
**Next:** End of Probability & Statistics playlist. Next playlist TBD.

### Competitive Analysis

**Competitor landscape:**
- 3Blue1Brown: NO dedicated regression video. Has Bayesian statistics content but nothing on least-squares regression.
- StatQuest (Josh Starmer): "Linear Regression, Clearly Explained!!" (~1M views) — whiteboard, 20+ min, covers cost function, gradient descent, correlation. Practical, no visual animation, but excellent pedagogical flow.
- Khan Academy: "Regression line example" videos in statistics playlist (~100K-500K views). Traditional lecture + 2D graph. Covers residuals, r-squared, prediction.
- Dr. Trefor Bazett: Has regression in stats playlist, clean Manim style but shorter and formula-focused.
- jbstatistics: Regression in full-lecture format (30+ min), thorough but dry whiteboard.

**Common structure:** Correlation → scatter plot → line of best fit → residuals → R-squared. Most start abstract and end with a worked example.

**Key gaps to differentiate:**
1. Animated scatter plot with data points appearing one by one, then the regression line "finding" its optimal position (nobody animates the optimization intuitively)
2. Visual residuals — show perpendicular distances shrinking as the line adjusts (StatQuest explains residuals but doesn't animate them)
3. Connect to variance concepts from earlier videos (SSR, SSE, SST decomposition)
4. Geometric interpretation: regression as projection onto the column space (connect back to Linear Algebra playlist — Videos 33-34)
5. Show the normal equations derivation visually, not just present the formula
6. Prediction and uncertainty (CI for predictions)

### Key Differentiators
1. Animated scatter plot → line slides into optimal position
2. Residual visualization: perpendicular lines from points to regression line
3. Geometric connection to linear algebra (projection)
4. SSR/SSE/SST decomposition shown visually with areas
5. R-squared as a proportion of variance explained — animated pie/area
6. Prediction interval vs. confidence interval distinction
7. Color coding consistent with rest of playlist

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Data Points | PRIMARY | #5BC0EB |
| Regression Line | SECONDARY | #7BC950 |
| Residuals | RED | #EF476F |
| Predictions | ACCENT | #FFD166 |
| Formulas | WHITE | #FFFFFF |
| R-squared | ACCENT | #FFD166 |

### Structure (12 minutes, 8 scenes)

**Scene 1 — Hook: Predicting the Future (1:00)**
- Motivating question: "Can we predict a student's exam score from hours studied?"
- Show a scatter plot with data points (hours vs. score)
- Ask: "How do we find the best line through these points?"
- Tease the regression concept
- Content budget: scatter plot + question

**Scene 2 — The Line of Best Fit (1:30)**
- Section divider
- Concept: we want the line y = mx + b that minimizes the total error
- Show residuals as vertical distances from points to a candidate line
- The line "slides" to minimize sum of squared residuals
- Key formula: minimize Σ(yᵢ - (mxᵢ + b))²
- Content budget: formula + 3 visual elements

**Scene 3 — Least Squares Derivation (1:30)**
- Set up the cost function (sum of squared residuals)
- Show partial derivatives ∂/∂m = 0 and ∂/∂b = 0
- Normal equations: the system that gives us m and b
- Key formulas for slope: m = Sxy / Sxx
- Content budget: 2-3 formulas, progressive reveal

**Scene 4 — Worked Example (2:00)**
- Concrete data: 5 points (hours studied, exam scores)
- Calculate means, Sxx, Sxy
- Compute slope and intercept
- Plot the regression line through the data
- Content budget: data table + formulas + graph

**Scene 5 — Interpreting the Line (1:30)**
- Slope meaning: "each additional hour of study predicts +5 points"
- Intercept: "base score with zero study"
- R-squared: proportion of variance explained
- SST = SSR + SSE decomposition
- Visual: colored areas showing explained vs. unexplained variance
- Content budget: 3 items + formula

**Scene 6 — Prediction and Uncertainty (1:30)**
- Making predictions: plug x into the line
- Point estimate vs. prediction interval
- Wider interval for x values far from the mean
- Connect to confidence intervals from Video 76
- Content budget: prediction visualization + 2 items

**Scene 7 — Linear Algebra Connection (1:00)**
- Quick connection: regression as projection onto column space
- The normal equations as AᵀAx = Aᵀb
- Connect to Videos 27, 33 from Linear Algebra playlist
- Content budget: 2-3 formulas, geometric diagram

**Scene 8 — Summary + Outro (1:00)**
- Recap: scatter plot → least squares → residuals → R-squared → prediction
- The probability and statistics playlist is complete!
- Outro with next steps teaser
- Content budget: 3 summary items
