# Video 241: What is Information? -- Plan

## Metadata
- **Number:** 241
- **Topic:** What is Information?
- **Level:** Graduate (Information Theory)
- **Class:** Video241_WhatIsInformation
- **Script:** scripts/graduate/video-241-what-is-information.py
- **Builds on:** Probability (67-78), Measure Theory (151-161), Stochastic Processes (229-240)
- **Leads to:** Entropy and Data Compression (242)
- **Estimated duration:** 10-12 minutes

## Purpose
First video of the Information Theory playlist. Introduces the concept of information as a measurable, mathematical quantity. Covers the surprise/information function, the intuition behind measuring uncertainty, and motivates Shannon entropy.

## Scene Plan (7 scenes)

### Scene 1: Hook -- What Does "Information" Mean? (50s)
**Content budget:** intro + title + 3 items
**Narration (~25s):** "What is information? A single bit of data? A 500-page book? A DNA sequence? In everyday language, information means different things to different people. But in 1948, Claude Shannon gave information a precise mathematical definition that revolutionized communication, computing, and even physics."

- play_intro("What is Information?", "Information Theory")
- Title: "The Question"
- Items: "A coin flip tells you 1 bit", "A page of text has redundancy", "Shannon made it mathematical"

### Scene 2: The Intuition of Surprise (70s)
**Content budget:** title + formula + 2 items
**Narration (~35s):** "Think about surprise. If someone tells you the sun rose this morning, you learn nothing. If they tell you they won the lottery, you learn a lot. The amount of information in an event is proportional to how surprised you are by it. Rare events carry more information than common ones."

- Title: "Information as Surprise"
- Formula: I(x) = -log(p(x))
- Items: "Sunrise: high probability, low information", "Lottery win: low probability, high information"

### Scene 3: The Information Function (70s)
**Content budget:** title + formula + 3 properties
**Narration (~35s):** "Shannon's information function has three natural properties. First, it's always non-negative, since probabilities are at most one. Second, rarer events carry more information, so the function is decreasing in probability. Third, information from independent events adds up. These three properties force the logarithm as the only possible function, up to a constant factor."

- Title: "Properties of I(x)"
- Formula: I(x) = -log_2(p(x)) [bits]
- Properties: non-negativity, monotone decreasing, additive for independent events

### Scene 4: A Concrete Example (70s)
**Content budget:** title + 3 items with bits
**Narration (~35s):** "Let's compute. A fair coin has probability one-half, so each outcome carries minus log base 2 of one-half, which equals 1 bit. A fair die has probability one-sixth, giving about 2.58 bits per outcome. A biased coin with probability 0.9 for heads gives only 0.15 bits for heads but 3.32 bits for the rare tails outcome. Information quantifies uncertainty."

- Title: "Computing Information"
- Examples: coin = 1 bit, die = 2.58 bits, biased coin (0.9) = 0.15 / 3.32 bits

### Scene 5: From Information to Entropy (70s)
**Content budget:** title + formula + 2 items
**Narration (~35s):** "A single event tells you how much information that event carries. But what about a random variable with many possible outcomes? We take the expected value of the information function. This expectation is called Shannon entropy, denoted H of X. It measures the average uncertainty per observation."

- Title: "Average Information: Entropy"
- Formula: H(X) = E[I(X)] = -sum(p_i log p_i)
- Items: "Expected information = entropy", "Measures average uncertainty"

### Scene 6: Entropy Intuition (70s)
**Content budget:** title + 3 examples
**Narration (~35s):** "Entropy is highest when all outcomes are equally likely, and zero when one outcome is certain. A fair coin has entropy 1 bit. A fair die has entropy 2.58 bits. A coin that always lands heads has entropy 0. Entropy captures how hard it is to predict the outcome before you see it."

- Title: "What Does Entropy Measure?"
- Items: fair coin H=1, fair die H=2.58, certain event H=0

### Scene 7: Summary and What's Next (55s)
**Content budget:** title + 3 items + outro
**Narration (~28s):** "Today we defined information as surprise, quantified it with the negative log, and averaged it to get Shannon entropy. Entropy measures uncertainty. In the next video, we'll see how entropy leads to data compression, and why it sets a fundamental limit on how much we can compress any message."

- Title: "Key Takeaways"
- Items: "Information = -log(p(x))", "Entropy = expected information", "Entropy bounds compression"
- play_outro(next="Entropy and Data Compression", next_playlist="Information Theory")
