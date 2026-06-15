# Video 68: Conditional Probability

**Playlist:** Probability & Statistics (Video 2 of 12)
**Duration target:** 10-12 minutes
**Plan date:** 2026-06-15

## Competitive Analysis Reference
- See `channel-analysis/improvements.md` "2026-06-15 — Conditional Probability"
- Key adopt: 3B1B's area/rectangle model, puzzle-first motivation
- Key avoid: Trefor Bazett's formula-first dry approach

## Scene Plan

### Scene 1: Hook — The Medical Test Puzzle (0:00-2:00, ~30s)
**Narration:** ~60 words, 30s
- Open with a compelling puzzle: "A test for a disease is 99% accurate. You test positive. What's the probability you actually have the disease?"
- Most people say 99%. The real answer depends on how rare the disease is.
- This is conditional probability — the probability of having the disease GIVEN a positive test.
- **Content budget:** Title + 2 text items + question formula
- Items: [title] → [question text] → [answer reveal "it depends on prevalence"]
- **Animation:** Title Write, question FadeIn, answer Transform

### Scene 2: Motivating Example — The Coin Bag (2:00-4:00, ~60s)
**Narration:** ~120 words, 60s
- Two bags of coins. Bag A: 3 gold, 1 silver. Bag B: 1 gold, 3 silver.
- You pick a bag at random, then draw a gold coin.
- What's the probability you picked Bag A?
- This naturally leads to the idea: "probability of A given that gold was drawn"
- Show the setup visually: two rectangles representing bags, coins inside
- **Content budget:** 4 items max on screen at once
- Items: [bag A rect] → [bag B rect] → [gold coin highlight] → [question "P(A | gold)?"]
- **Animation:** Rectangles Create, coins FadeIn, highlight Indicate

### Scene 3: Formal Definition (4:00-6:00, ~60s)
**Narration:** ~120 words, 60s
- Section divider: "Conditional Probability"
- Definition: P(A|B) = P(A ∩ B) / P(B), where P(B) > 0
- Intuition: "What fraction of B is also in A?"
- Visual: Venn diagram with two circles A and B, intersection highlighted
- Show the area model: Omega as unit square, A and B as overlapping regions
- P(A|B) = area of overlap ÷ area of B
- **Content budget:** formula box + Venn diagram (2 main elements)
- Items: [section divider] → [Venn diagram] → [formula box] → [intuition text]
- **Animation:** Section divider, Venn Create, formula Write, text FadeIn

### Scene 4: Worked Example — Dice (6:00-8:30, ~90s)
**Narration:** ~180 words, 90s
- Roll a fair die. Let A = "even number", B = "at least 4"
- Find P(A|B) — probability it's even given it's at least 4
- Step 1: What is B? {4, 5, 6} → P(B) = 3/6 = 1/2
- Step 2: What is A ∩ B? {4, 6} → P(A ∩ B) = 2/6 = 1/3
- Step 3: P(A|B) = P(A ∩ B) / P(B) = (1/3) / (1/2) = 2/3
- Verify by counting: given B = {4,5,6}, the evens are {4,6}, so 2 out of 3
- Show both the formula method and the counting method
- **Content budget:** 5 items max
- Items progress: [problem statement] → [B set] → [A∩B set] → [formula] → [answer]

### Scene 5: Contingency Table Example (8:30-10:00, ~60s)
**Narration:** ~120 words, 60s
- Adopted from StatQuest's approach: start with data, then compute
- Table: 100 students, 60 like math, 40 don't. Of math-likers, 30 also like physics. Of non-math-likers, 10 like physics.
- Question: P(likes physics | likes math)?
- Fill in the table step by step
- P(physics | math) = 30/60 = 1/2
- Compare: P(physics | not math) = 10/40 = 1/4
- **Content budget:** table + formula + answer (3 items)
- **Animation:** Table fills progressively, formula appears, answer highlighted

### Scene 6: Key Properties (10:00-11:00, ~40s)
**Narration:** ~80 words, 40s
- Property 1: P(A|B) is NOT the same as P(B|A) — common mistake!
  - Example: P(rain | clouds) ≠ P(clouds | rain)
- Property 2: If A ⊆ B, then P(A|B) = P(A)/P(B)
- Property 3: Law of total probability (teaser for Bayes): P(A) = P(A|B₁)P(B₁) + P(A|B₂)P(B₂)
- **Content budget:** 3 properties shown one at a time with progressive reveal
- Items: [prop 1] → [example] → [prop 2] → [prop 3 + teaser]
- **Animation:** Each property FadeIn, then FadeOut before next

### Scene 7: Summary and Teaser (11:00-12:00, ~40s)
**Narration:** ~80 words, 40s
- Recap: Conditional probability asks "given B, what's the probability of A?"
- Formula: P(A|B) = P(A ∩ B) / P(B)
- Key insight: It rescales probability relative to the new information B
- Tease: "Next time — Independence and Bayes' Theorem: how to update beliefs with evidence"
- **Content budget:** 3 recap items + outro
- **Animation:** Recap items progressive reveal, then play_outro()

## Color Coding
- PRIMARY (#5BC0EB): Events, sets, conditional probability notation
- SECONDARY (#7BC950): Sample space Omega, favorable outcomes
- ACCENT (#FFD166): Formulas, key results
- RED (#EF476F): Warnings, common mistakes (P(A|B) ≠ P(B|A))

## Formulas to Render
1. P(A|B) = P(A ∩ B) / P(B)
2. P(A|B) = |A ∩ B| / |B| (counting version)
3. P(A) = Σ P(A|Bᵢ) P(Bᵢ) (law of total probability teaser)
