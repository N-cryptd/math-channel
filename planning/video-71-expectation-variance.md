# Video 71: Expectation and Variance

**Playlist:** Probability & Statistics (Video 5 of 12)
**Estimated duration:** 12-14 minutes
**Script file:** `scripts/undergraduate/video-71-expectation-variance.py`
**Class name:** `Video71_ExpectationVariance`
**Status:** PLANNING

## Competitive Analysis

### Key Channels and Their Approaches to Expectation and Variance

**jbstatistics — "Expected Value and Variance of Discrete Random Variables" (1.45M views)**
- Covers both E[X] and Var(X) in 8 minutes — rushes variance
- Die roll example: E(X) = 3.5, then Var(X) computation
- Very formula-focused, static whiteboard style
- Strength: Clear computation, good table format. Weakness: No visual engagement, too fast

**StatQuest — "Expected Values, Main Ideas!!!" (280K views)**
- Casino/lottery hook: "Why do casinos always make money?" — compelling opener
- Emphasizes E[X] is the long-run average, NOT a single predicted outcome
- Two examples: lottery (simple) and weighted die (complex)
- Strength: Best hook, notation breakdown. Weakness: Talking-head, no Manim, no variance

**Steve Brunton — "The Expected Value (Mean) of a Probability Distribution" (45K views)**
- Places E[X] in context of "moments" — first moment, second moment
- "Misleading expected values" — E[X] = 3.5 but you can't roll 3.5
- Distinguishes sample mean vs expected value
- Strength: Conceptual depth. Weakness: Academic tone, no animation, no variance

**Khan Academy — "Mean (expected value) of a discrete random variable" (457K views)**
- Traffic ticket example: compute E[fine]
- Very short (4:32), computation-only, no conceptual intuition
- Strength: Accessible. Weakness: Too formulaic, no visual understanding

### Competitive Gap Analysis
- **Gap:** No competitor combines (1) a compelling hook with (2) animated PMF bar chart showing the "balance point" geometrically, (3) clear definition and notation, (4) the "misleading expected value" insight, AND (5) variance with visual spread representation AND (6) linearity properties.
- **3B1B gap:** 3B1B has NO dedicated expectation/variance video — major opportunity. His CLT and binomial distribution videos assume viewers already know these concepts.
- **Our unique angle:** Animate the "balance point" of a PMF — bars with weights and a fulcrum finding E[X] visually. For variance, animate the "spread" by showing distance bars from the mean on the PMF. This geometric intuition is missing from ALL competitors.

### Our Approach (Synthesis)
- **Structure:** Hook (casino) → E[X] definition with notation → Die roll example → "Misleading" insight → Variance definition → Variance of die → Computational shortcut → Properties (linearity, constants) → Summary
- **Visual metaphors:** (1) PMF bar chart with animated fulcrum/balance point at E[X], (2) Variance as colored distance bars from the mean, (3) Weighted sum animation showing each x·p(x) contribution stacking up
- **Color scheme:** PRIMARY (#5BC0EB) for PMF bars, ACCENT (#FFD166) for E[X] marker/line, SECONDARY (#7BC950) for variance/distance bars, RED (#EF476F) for "impossible value" warnings

## Scene Breakdown

### Scene 1: Hook — The Casino Question (0:00-1:30, ~90s)
**Narration:** ~180 words
- "Imagine a simple casino game: you pay two dollars to play, and a wheel spins. You win ten dollars with probability one in ten, five dollars with probability three in ten, or nothing with probability six in ten. Should you play?"
- "The answer depends on the expected value. In the long run, how much does the casino pay you per game on average?"
- "This concept — the expected value of a random variable — is why casinos always profit. It is one of the most powerful ideas in all of probability."
- Connect: "Last time we defined random variables and their probability mass functions. Today we measure their center and their spread."
- **Content budget:** title + game wheel (3 outcomes) + "should you play?" question + key formula teaser
- **Animation:** Write title, wheel diagram FadeIn, outcomes highlighted, question appears

### Scene 2: Expected Value — Definition (1:30-3:30, ~120s)
**Narration:** ~240 words
- Section divider: "Expected Value"
- "The expected value of a discrete random variable X is the weighted average of all its possible values, weighted by their probabilities."
- Formal: E[X] = sum of x * p(x) for all x
- Break down notation: "E brackets X" means "the expected value of X", the sum symbol means "add up", each term is value times its probability
- "Think of it as the center of gravity of the probability mass function. If you built the PMF as physical bars, E[X] is where the fulcrum balances."
- Visual: PMF bar chart with animated fulcrum/balance point
- **Content budget:** definition box + notation breakdown + PMF balance visual (max 5 items)
- **Animation:** Section divider, definition Write, notation animated symbol-by-symbol, PMF bars with fulcrum

### Scene 3: Expected Value — Die Roll Example (3:30-5:30, ~120s)
**Narration:** ~240 words
- Section divider: "Example — Fair Die"
- "Let's compute E[X] for a fair six-sided die. X takes values 1 through 6, each with probability one sixth."
- Show PMF table: x values and p(x) values side by side
- Animated computation: E[X] = 1(1/6) + 2(1/6) + 3(1/6) + 4(1/6) + 5(1/6) + 6(1/6) = 21/6 = 3.5
- Visual: PMF bars with fulcrum settling at 3.5
- **Content budget:** PMF table + computation steps + result (max 5 items, progressive reveal)
- **Animation:** Table builds, computation terms highlight sequentially, result revealed, fulcrum animation

### Scene 4: The "Misleading" Insight (5:30-6:30, ~60s)
**Narration:** ~120 words
- "But wait. The expected value is 3.5. Can you roll a 3.5 on a die? No. Every individual roll gives an integer from 1 to 6."
- "E[X] is not a value that X will take. It is the LONG-RUN AVERAGE. If you roll the die thousands of times, the average approaches 3.5."
- "This is the single most common misconception about expected value. E[X] does not predict a single outcome."
- Visual: Animated die rolls showing running average converging to 3.5
- **Content budget:** warning text + die animation + running average line (max 4 items)
- **Animation:** Warning text in RED, die rolls, running average plot

### Scene 5: Variance — Definition (6:30-8:30, ~120s)
**Narration:** ~240 words
- Section divider: "Variance"
- "Expected value tells us the center. But two random variables can have the same mean yet behave very differently."
- Visual: Two PMFs side by side — one narrow (die), one wide (another distribution) — both centered at 3.5
- "Variance measures how spread out the values are around the mean. It is the average squared distance from E[X]."
- Formal: Var(X) = E[(X - mu)^2] = sum of (x - mu)^2 * p(x) for all x
- "We square the distance so positive and negative deviations don't cancel out."
- "The square root of the variance gives us the standard deviation, sigma, which has the same units as X."
- **Content budget:** two PMFs + definition box + formula + sigma note (max 5 items)
- **Animation:** Two PMFs, highlight distances from mean on one, definition Write

### Scene 6: Variance — Die Roll Example (8:30-10:30, ~120s)
**Narration:** ~240 words
- Section divider: "Example — Variance of a Die"
- "For our fair die with E[X] = 3.5, let's compute the variance."
- Show computation table: x, (x - 3.5), (x-3.5)^2, p(x), product
- Key rows shown progressively: x=1: (1-3.5)^2 * 1/6 = 6.25/6, x=6: (6-3.5)^2 * 1/6 = 6.25/6
- By symmetry (or direct computation): Var(X) = 35/12 ~ 2.917
- Standard deviation: sigma = sqrt(35/12) ~ 1.708
- Visual: PMF bars with distance markers from 3.5, colored in SECONDARY
- **Content budget:** computation table + PMF with distances (max 5 items)
- **Animation:** Table builds progressively, distances highlighted on PMF

### Scene 7: Computational Shortcut and Properties (10:30-12:00, ~90s)
**Narration:** ~180 words
- Section divider: "Shortcut and Properties"
- "Computing (x - mu)^2 for every value can be tedious. There is a useful shortcut:"
- Var(X) = E[X^2] - (E[X])^2
- "This is often easier because you compute E[X^2] directly from the PMF."
- Properties:
  1. Var(aX + b) = a^2 * Var(X) — scaling stretches variance by a^2, shifting does nothing
  2. E[aX + b] = aE[X] + b — linearity of expectation (simple form)
  3. Var(X) >= 0 always (squared distances)
  4. Var(X) = 0 iff X is constant (no spread)
- **Content budget:** shortcut formula + 2-3 properties (max 5 items)
- **Animation:** Shortcut formula Write, properties as progressive_reveal

### Scene 8: Summary and Outro (12:00-13:00, ~60s)
**Narration:** ~120 words
- Recap with progressive_reveal:
  1. Expected value E[X] = sum x*p(x) — the center / long-run average
  2. E[X] is NOT a predicted single outcome — it's an average
  3. Variance Var(X) = sum (x-mu)^2*p(x) — the spread
  4. Standard deviation sigma = sqrt(Var(X)) — same units as X
  5. Shortcut: Var(X) = E[X^2] - (E[X])^2
- Tease: "Next time — Common Distributions: the families of random variables that appear everywhere in science and engineering."
- play_outro()
- **Content budget:** 5 recap items + outro card

## Formulas to Render
1. E[X] = \sum_x x \cdot p(x) (expected value)
2. E[X] = 3.5 (die example result)
3. Var(X) = E[(X - \mu)^2] = \sum_x (x - \mu)^2 \cdot p(x) (variance definition)
4. \sigma = \sqrt{Var(X)} (standard deviation)
5. Var(X) = E[X^2] - (E[X])^2 (computational shortcut)
6. Var(aX + b) = a^2 Var(X) (scaling property)
7. E[aX + b] = aE[X] + b (linearity)

## Color Coding
- PRIMARY (#5BC0EB): PMF bars, probability values
- ACCENT (#FFD166): E[X] marker/line, key formulas
- SECONDARY (#7BC950): Variance bars, distance markers
- RED (#EF476F): Warnings ("E[X] is not a single outcome")
- DIM (#6B6B8D): Intermediate calculations, labels

## Technical Notes
- PMF bar chart: custom Rectangle objects, arranged on x-axis with height = p(x)
- Fulcrum animation: DashedLine at E[X] value, animated to "settle" with a wobble
- Distance bars: short colored segments from each bar center to E[X] line
- Running average: custom number line showing cumulative average approaching 3.5
- Two-column PMF comparison: side-by-side bar charts (narrow vs wide)
- Use single backslashes in raw strings for LaTeX
- Use ly.formula_box() for key results
