# Video 70: Random Variables

**Playlist:** Probability & Statistics (Video 4 of 12)
**Estimated duration:** 12-14 minutes
**Script file:** `scripts/undergraduate/video-70-random-variables.py`
**Class name:** `Video70_RandomVariables`
**Status:** PLANNING

## Competitive Analysis

### Key Channels and Their Approaches to Random Variables

**3Blue1Brown — "Probability spaces and the probability function" (probability playlist)**
- 3B1B doesn't have a dedicated random variable video, but his probability series builds toward them organically. His geometric/area model approach naturally leads into random variables as functions on sample spaces.
- Key insight: Random variables can be visualized as "measurements" on sample space outcomes.

**Khan Academy — "Random variables and probability distributions"**
- Approach: Defines random variable as "variable whose possible values are numerical outcomes of a random phenomenon." Starts with discrete examples (coin flips mapped to 0/1). Goes through PDF, PMF, CDF.
- Strength: Accessible, many examples. Weakness: Visually plain, no Manim animations.

**StatQuest (Josh Starmer) — "Random Variables and Probability Distributions"**
- Approach: Fast-paced, practical focus. "A random variable is a numerical summary of a random experiment." Shows dice, coin examples.
- Strength: Intuitive framing. "Think of it as a variable that varies randomly." Good for engineers.

**Dr. Trefor Bazett — "Random Variables"**
- Approach: Formal but accessible. X: Omega -> R. Shows sample space mapping diagram. Clean board-style visuals.
- Strength: The mapping diagram (Omega -> R) is the clearest visual for understanding what a random variable IS.

**jbstatistics — "Discrete random variables"**
- Approach: "A random variable is a numerical quantity whose value depends on chance." Covers indicator variables, types (discrete vs continuous).
- Strength: Very thorough. Weakness: Whiteboard only.

### Competitive Gap Analysis
- **Gap:** No existing video combines an intuitive introduction with a strong visual of the mapping X: Omega -> R, AND builds up to PMF naturally, AND connects to real-world examples (quiz scores, game outcomes).
- **Our unique angle:** Manim animation of the mapping from sample space to the real number line. Show outcomes "flowing" to their numerical values. This visualization is rare in the competitor space.
- **Structure advantage:** We can build from Video 69's Bayes/independence content, showing how random variables provide a "number layer" on top of the event framework.

### Our Approach (Synthesis)
- **Structure:** Hook (quiz score example) → What is a random variable? (mapping concept) → Discrete RVs → PMF → CDF → Continuous RVs introduction → Summary
- **Visual metaphors:** (1) Omega as a cloud of outcomes, arrows mapping to a number line below, (2) PMF as bar chart building up, (3) CDF as staircase function growing
- **Color scheme:** PRIMARY (#5BC0EB) for sample space/outcomes, SECONDARY (#7BC950) for the real number line/values, ACCENT (#FFD166) for key formulas/definitions, RED (#EF476F) for warnings/not-to-confuse

## Scene Breakdown

### Scene 1: Hook — The Quiz Score (0:00-1:30, ~90s)
**Narration:** ~180 words
- "Imagine you take a 10-question quiz, each worth 10 points, and you guess every answer randomly with four choices each. What can you say about your score?"
- "It's not fixed. It's a number that depends on chance. This is the essence of a random variable."
- Show: 10 question boxes, each randomly H or X (correct/wrong), total score computed
- Key: "Your score is a RANDOM VARIABLE — a number whose value is determined by a random process."
- Connect: "In the last video we studied events and probabilities. Now we're going to turn events into numbers."
- **Content budget:** title + 10 quiz boxes (as a grid) + score display + key definition text
- **Animation:** Write title, quiz grid FadeIn, random outcomes appear, score computed, definition with formula_box

### Scene 2: What is a Random Variable? (1:30-3:00, ~90s)
**Narration:** ~180 words
- Section divider: "Definition"
- "A random variable is a function X that assigns a real number to every outcome in the sample space."
- Formal: X: Omega -> R
- Visual: Omega cloud at top, arrows flowing down to number line at bottom
- Show concrete example: coin flip, X(H) = 1, X(T) = 0 (indicator variable)
- "X is random because the outcome is random. X is a variable because it takes different values."
- Key distinction: "A random variable is NOT a variable in the algebra sense. It's a MEASUREMENT function."
- **Content budget:** definition box + mapping diagram + indicator example (5 items max)
- **Animation:** Section divider, definition Write, mapping arrows animate down, indicator example replaces it

### Scene 3: Discrete Random Variables (3:00-5:00, ~120s)
**Narration:** ~240 words
- Section divider: "Discrete Random Variables"
- "A random variable is discrete if it takes values in a countable set."
- Examples with mappings:
  - Die roll: X(1)=1, X(2)=2, ..., X(6)=6 (identity map)
  - Sum of two dice: X((i,j)) = i+j, values {2,3,...,12}
  - Number of heads in 3 flips: X = 0,1,2,3
- Visual: Show Omega for each, arrows to values on number line
- "The key feature: you can LIST all possible values. Between any two values, there's a gap."
- **Content budget:** definition + 2 examples shown sequentially (max 5 items on screen)
- **Animation:** Section divider, definition, first example with mapping diagram, then second

### Scene 4: Probability Mass Function (5:00-7:30, ~150s)
**Narration:** ~300 words
- Section divider: "PMF"
- "The Probability Mass Function tells us the probability of each value a discrete RV takes."
- Formal: p_X(x) = P(X = x)
- Properties:
  1. p_X(x) >= 0 for all x
  2. Sum of p_X(x) over all x = 1
- Example: Number of heads in 3 fair coin flips
  - X = 0: P(TTT) = 1/8
  - X = 1: P(HTT, THT, TTH) = 3/8
  - X = 2: P(HHT, HTH, THH) = 3/8
  - X = 3: P(HHH) = 1/8
- Visual: PMF as a bar chart building up bar by bar
- "The PMF completely describes the behavior of a discrete random variable. Once you know p_X, you know everything."
- **Content budget:** definition + properties + bar chart (progressive reveal, max 5 items)
- **Animation:** Formula box, properties as bullet points, bar chart builds progressively

### Scene 5: Cumulative Distribution Function (7:30-9:30, ~120s)
**Narration:** ~240 words
- Section divider: "CDF"
- "The Cumulative Distribution Function gives the probability that X takes a value AT MOST x."
- Formal: F_X(x) = P(X <= x)
- Properties:
  1. 0 <= F_X(x) <= 1
  2. F_X is non-decreasing
  3. F_X(-inf) = 0, F_X(inf) = 1
- Continue the coin flip example:
  - F_X(0) = P(X<=0) = 1/8
  - F_X(1) = P(X<=1) = 4/8
  - F_X(2) = P(X<=2) = 7/8
  - F_X(3) = P(X<=3) = 8/8 = 1
- Visual: Staircase function drawn step by step
- Relationship to PMF: F_X(x) = sum of p_X(k) for k <= x
- **Content budget:** definition + properties (2-3 items) + staircase diagram (max 5 items)
- **Animation:** Section divider, formula box, staircase drawn progressively

### Scene 6: Continuous Random Variables — Introduction (9:30-11:00, ~90s)
**Narration:** ~180 words
- Section divider: "Continuous Random Variables"
- "Not all measurements are countable. What if X is the time until the next bus arrives? X can be 3.5 minutes, 3.51, 3.517, ... There are uncountably many values."
- "A random variable is continuous if it takes values in an interval (or union of intervals)."
- Key difference from discrete: P(X = x) = 0 for any specific x
- "Instead of a PMF, we use a Probability Density Function (PDF):"
- Formal: P(a <= X <= b) = integral from a to b of f_X(x) dx
- Visual: Smooth bell curve with shaded area representing probability
- "The total area under the curve must equal 1, just like the PMF sums to 1."
- **Content budget:** definition + bell curve with shaded area + key formula (4-5 items)
- **Animation:** Section divider, smooth curve created, area shaded, formula appears

### Scene 7: Discrete vs Continuous Comparison (11:00-12:00, ~60s)
**Narration:** ~120 words
- Section divider: "Comparison"
- Two columns:
  - LEFT: Discrete — countable values, PMF (bar chart), P(X=x) > 0, sum = 1
  - RIGHT: Continuous — uncountable values, PDF (curve), P(X=x) = 0, integral = 1
- "Both types describe uncertainty with numbers. The math is different, but the ideas are parallel."
- **Content budget:** Two-column comparison (max 5 items)
- **Animation:** Section divider, two columns FadeIn, key points revealed

### Scene 8: Summary and Outro (12:00-13:00, ~60s)
**Narration:** ~120 words
- Recap with progressive_reveal:
  1. Random variable X: Omega -> R — assigns a number to each outcome
  2. Discrete RVs take countable values; described by PMF
  3. PMF: p_X(x) = P(X=x), sums to 1
  4. CDF: F_X(x) = P(X<=x), non-decreasing staircase
  5. Continuous RVs: PDF replaces PMF, integrals replace sums
- Tease: "Next time — Expectation and Variance: measuring the center and spread of random variables"
- play_outro()
- **Content budget:** 5 recap items + outro card

## Formulas to Render
1. X: Omega -> R (random variable as function)
2. p_X(x) = P(X = x) (PMF)
3. p_X(x) >= 0, sum p_X(x) = 1 (PMF properties)
4. F_X(x) = P(X <= x) (CDF)
5. P(a <= X <= b) = integral from a to b of f_X(x) dx (PDF)

## Color Coding
- PRIMARY (#5BC0EB): Sample space outcomes, Omega, individual events
- SECONDARY (#7BC950): Real number line, X values, numerical outcomes
- ACCENT (#FFD166): Key formulas (PMF, CDF, PDF definitions)
- RED (#EF476F): Warnings (RV != algebra variable, P(X=x)=0 for continuous)
- DIM (#6B6B8D): Intermediate calculations, labels

## Technical Notes
- Mapping diagram: use CurvedArrow from sample space outcomes to number line positions
- Bar chart: use BarChart from manim or custom Rectangle + Text objects
- Staircase: use custom Line segments with jumps, or StepFunction approximation
- Bell curve: use ParametricFunction with gaussian equation
- Use single backslashes in raw strings for LaTeX
- Keep formulas clean — use ly.formula_box() for key results
