# Video 84: Counting Principles
## Discrete Mathematics -- Video 6 of 12

**Predecessor:** Video 83 (Equivalence Relations)
**Next:** Video 85 (Pigeonhole Principle)

### Competitive Analysis

Analyzed 5 competitor videos on counting principles (2026-06-23):

- **Kimberly Brehm**: "Permutations and Combinations" (~350K views, 22 min, tablet whiteboard). Full textbook coverage, systematic. 5/10 overall. No binomial properties.
- **Neso Academy**: "Permutations & Combinations" (~1.2M views, slide-based). Split across videos. 5.5/10 overall. No visual intuition.
- **TrevTutor**: "Discrete Math: Counting" (~200K views, whiteboard). Fast, CS-focused. 4.4/10 overall.
- **Wrath of Math**: "Fundamental Counting Principle" (~150K views, 5-10 min). Good hook style. 5.4/10 overall.
- **Dr. Trefor Bazett**: "Combinatorics" (~200K views, iPad whiteboard). Energetic, good order/no-order distinction. 6/10 overall.

**MAJOR GAP:** No animated video covers the full arc: product rule -> permutations -> combinations -> binomial coefficients -> Pascal's identity. All competitors use static whiteboards/slides. We can make counting VISUAL with animated tree diagrams, arrangement animations, and Pascal's triangle building.

### Key Differentiators
1. **Animated tree diagrams** showing the multiplication principle branching out in real-time
2. **Visual arrangement animations**: colored objects moving into labeled slots for permutations
3. **Permutation-to-combination visual transform**: show a permutation arrangement, then highlight "forget the order" as groupings collapse
4. **Animated Pascal's triangle**: row-by-row build with color-coded entries showing C(n,k)
5. **Poker hand example**: animated card selection showing C(52,5) as a counting process
6. **Progressive arc**: simple product rule -> structured permutations -> efficient combinations -> elegant binomial properties

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Product rule / counting principle | PRIMARY | #5BC0EB |
| Permutations P(n,k) | PRIMARY | #5BC0EB |
| Combinations C(n,k) | SECONDARY | #7BC950 |
| Binomial coefficients / Pascal | ACCENT | #FFD166 |
| Formula boxes | ACCENT | #FFD166 |
| Examples / numbers | WHITE | #FFFFFF |
| Distinguish (order matters!) | RED | #EF476F |
| Tree diagrams / branches | PRIMARY | #5BC0EB |

### Structure (14 minutes, 10 scenes)

**Scene 1 -- Hook: How Many Ways? (1:30)**
- Last video: equivalence relations grouped elements into classes. Now we ask: HOW MANY elements are in those groups?
- Real-world counting problems: How many possible PIN codes? How many poker hands? How many ways to arrange books on a shelf?
- These all share a common mathematical structure -- counting principles
- Bridge: if we can count systematically, we can solve problems that seem impossibly large
- Content budget: 3 counting questions + "counting principles" concept intro

**Scene 2 -- Fundamental Counting Principle (1:30)**
- Section divider
- Statement: If task A has m outcomes and task B has n outcomes, then A followed by B has m x n outcomes
- Visual: animated tree diagram -- first branch (3 outcomes) then second branch (4 outcomes), showing 3 x 4 = 12 leaves
- Generalize: for k tasks with n_1, n_2, ..., n_k outcomes, total = n_1 x n_2 x ... x n_k
- Example: outfit choices -- 3 shirts x 4 pants x 2 shoes = 24 outfits (animated branching)
- Content budget: statement + tree diagram + generalization + outfit example

**Scene 3 -- Permutations: When Order Matters (1:30)**
- Section divider
- Motivation: from the counting principle, what if we select k items from n distinct items AND order matters?
- Visual: 4 colored objects A, B, C, D. Show arranging 3 of them into slots: _ _ _
- First slot: 4 choices. Second: 3 choices. Third: 2 choices. Total = 4 x 3 x 2 = 24
- Animated: objects sliding into slots one by one, counting choices at each step
- Formula: P(n, k) = n! / (n-k)!
- Special case: P(n, n) = n! (arrange ALL n items)
- Example: arranging 5 books on a shelf = 5! = 120 ways
- Content budget: motivation + slot animation + formula + special case + example

**Scene 4 -- Permutations: Worked Example (1:00)**
- Section divider
- Example: How many ways can 8 runners finish 1st, 2nd, 3rd? (podium arrangements)
- P(8, 3) = 8! / 5! = 8 x 7 x 6 = 336 ways
- Animated: show the formula computing step by step
- Example 2: How many 4-letter "words" from ALPHABET (26 letters, no repeats)?
- P(26, 4) = 26 x 25 x 24 x 23 = 358,800
- Content budget: 2 worked examples with animated computation

**Scene 5 -- Combinations: When Order Doesn't Matter (1:30)**
- Section divider
- Key insight: sometimes we SELECT but don't care about order
- Visual transition: show a permutation arrangement ABC, ACB, BAC, BCA, CAB, CBA -- then group them: "These all select the SAME SET {A, B, C}"
- Animated grouping/collapse: 6 permutations collapse into 1 combination
- Each k-element combination corresponds to k! permutations
- Formula: C(n, k) = P(n, k) / k! = n! / (k!(n-k)!)
- Example: choosing 3 friends from 5 for a committee = C(5, 3) = 10
- Content budget: visual transition + grouping animation + formula + committee example

**Scene 6 -- Combinations: Poker Hands (1:00)**
- Section divider
- Classic application: How many 5-card poker hands from a standard 52-card deck?
- C(52, 5) = 52! / (5! x 47!) = 2,598,960
- Animated: show the formula, then note why order doesn't matter (a hand is a SET of cards)
- Compare to permutations: P(52, 5) = 311,875,200 -- combinations are MUCH smaller because we divide by 5! = 120
- Content budget: poker hand count + permutation comparison + "why combinations" insight

**Scene 7 -- Binomial Coefficients and Pascal's Triangle (1:30)**
- Section divider
- C(n, k) is called the "binomial coefficient" -- appears in the binomial theorem, probability, algebra
- Key property: Symmetry -- C(n, k) = C(n, n-k)
- Visual: show Pascal's triangle row by row, color-code entries
- Row 0: 1. Row 1: 1 1. Row 2: 1 2 1. Row 3: 1 3 3 1. Row 4: 1 4 6 4 1.
- Each entry is C(n, k) -- show the connection
- Animated: rows appearing one by one, with C(n,k) labels appearing
- Content budget: definition + symmetry + Pascal's triangle animated build

**Scene 8 -- Pascal's Identity (1:00)**
- Section divider
- Pascal's identity: C(n, k) = C(n-1, k-1) + C(n-1, k)
- Visual: highlight a cell in Pascal's triangle, show it equals the sum of the two cells above it
- Animated: color a cell ACCENT, then highlight the two parent cells in PRIMARY and SECONDARY, show sum
- Proof intuition: an n-element subset either INCLUDES element n (then choose k-1 from remaining n-1) or EXCLUDES element n (then choose k from remaining n-1)
- Visual: element n highlighted, split into two paths
- Content budget: identity statement + triangle visual + proof intuition

**Scene 9 -- Applications Summary (1:00)**
- Section divider
- Quick-fire applications:
  - Lottery: C(49, 6) = 13,983,816 possible tickets (1 in ~14 million chance)
  - Bit strings: 2^n possible n-bit strings (each bit: 0 or 1)
  - Binary relations on an n-element set: 2^(n^2) possible relations
  - Bridge to Video 85: "What if we have MORE pigeons than holes?"
- Content budget: 3 quick applications + pigeonhole teaser

**Scene 10 -- Summary + Outro (0:30)**
- Recap: fundamental counting principle (product rule) for sequential tasks
- Permutations P(n, k) = n!/(n-k)! -- arrangements where order matters
- Combinations C(n, k) = n!/(k!(n-k)!) -- selections where order doesn't matter
- Binomial coefficients have beautiful structure: symmetry, Pascal's triangle, Pascal's identity
- Next video: Pigeonhole Principle -- when counting forces a conclusion
- Content budget: 4 summary items + next preview
