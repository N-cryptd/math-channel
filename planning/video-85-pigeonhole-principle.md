# Video 85: Pigeonhole Principle
## Discrete Mathematics -- Video 7 of 12

**Predecessor:** Video 84 (Counting Principles)
**Next:** Video 86 (Graph Theory Basics)

### Competitive Analysis

Analyzed 6 competitor videos (2026-06-24):

- **Spanning Tree**: "What Is the Pigeonhole Principle?" (~3.5M views, 8:23). Clean animated explainer with 3D pigeons. Hook: hairy twins puzzle. 8/10 overall. No generalized PHP.
- **Mathologer**: "7 gorgeous proofs" (~191K views, 33:32). Deep dive into 7 diverse applications. 9/10 content, but 33 min is too long for introduction.
- **Up and Atom**: "Simple Principle Solves IMPOSSIBLE Math Problems" (~237K views, 15:50). Conversational, connects to CS compression. 8/10 overall.
- **Kimberly Brehm**: Discrete Math II lecture (~122K views, 14:23). Tablet whiteboard, covers basic + generalized PHP. 5/10 — no animations.
- **Eddie Woo**: "Pigeonhole Principle (1 of 2)" (~32K views, 10:12). Live classroom. 6/10 — whiteboard only.
- **Prime Newtons**: "First Pigeonhole Principle" (~9K views). Short, focused. 5/10.

**MAJOR GAP:** No high-quality Manim-animated video covers PHP systematically. Spanning Tree uses 3D (not Manim), Mathologer uses 2D graphics, all others use whiteboards. We can be the first to cover PHP with Manim animations: animated pigeons flying into holes, visual overflow demonstrations, and progressive abstraction.

### Key Differentiators
1. **Animated pigeon/box visuals**: circles (pigeons) moving into rectangles (holes) with color coding — literal then abstract
2. **Progressive arc**: intuitive examples (birthdays, socks) → formal statement → proof sketch → generalized PHP → surprising applications
3. **Generalized PHP with visual proof**: most competitors skip this entirely
4. **Surprise application as finale**: recurring decimals or party handshakes — something that makes viewers go "wow"
5. **Manim-first approach**: the only channel doing PHP with proper mathematical animations

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Pigeons / items to place | PRIMARY | #5BC0EB |
| Holes / containers | SECONDARY | #7BC950 |
| The match / forced conclusion | ACCENT | #FFD166 |
| Impossible / contradiction | RED | #EF476F |
| Formal statements / boxes | ACCENT | #FFD166 |
| Examples / numbers | WHITE | #FFFFFF |

### Structure (12 minutes, 10 scenes)

**Scene 1 -- Hook: The Hairy Twins (1:30)**
- Last video: counting principles told us HOW MANY. This video: a principle that FORCES a conclusion with almost no counting at all.
- "In this room right now, there are two people with the same number of hairs on their heads." This sounds impossible — but the pigeonhole principle makes it certain.
- Visual: crowd of stick figures, count arrows to hair counts, two highlighted in ACCENT
- Bridge: this is the power of the pigeonhole principle — sometimes quantity alone forces structure
- Content budget: 3 setup lines + "impossible claim" + reveal + bridge

**Scene 2 -- Statement of the PHP (1:00)**
- Section divider
- "If you put n+1 pigeons into n pigeonholes, then at least one hole contains at least two pigeons."
- Visual: animated PRIMARY circles (pigeons) flying into SECONDARY rectangles (holes) — one hole gets two
- Formal: "If |A| > |B|, any function f: A → B is not injective"
- This is deceptively simple — its applications are deep
- Content budget: informal statement + animation + formal version

**Scene 3 -- Simple Examples (1:30)**
- Section divider
- Example 1: Birthdays — in a group of 367 people, at least two share a birthday (366 days + leap year)
  - Animated: 367 tiny circles flowing into 366 boxes; one box overflows
- Example 2: Socks in a drawer — 6 pairs (6 black, 6 blue = 12 socks). How many to pull for a matching pair? Answer: 3 (only 2 colors)
  - Animated: pulling socks from drawer, 3rd sock guaranteed to match one already pulled
- Example 3: 13 people in a room — at least 2 born in the same month (12 months, 13 people)
- Content budget: 3 examples with animations

**Scene 4 -- Proof via Contradiction (1:00)**
- Section divider
- "Proof: Suppose every hole has at most one pigeon. Then the total pigeons ≤ the number of holes. But we have n+1 pigeons in n holes — contradiction."
- Visual: show holes each with at most 1 pigeon, then count them up, get n — but we need n+1 — RED flash
- "This is why it works: the only way to avoid two in a hole is impossible."
- Content budget: proof statement + visual contradiction + concluding remark

**Scene 5 -- Generalized Pigeonhole Principle (1:30)**
- Section divider
- "If we put n pigeons into k holes, then at least one hole has at least ⌈n/k⌉ pigeons."
- Visual: distribute items evenly, show the ceiling forcing one extra
- Example: 17 socks, 3 colors → at least ⌈17/3⌉ = 6 of one color
- "This is stronger: it tells you not just that a collision exists, but how many items must pile up."
- Content budget: statement + animation + worked example

**Scene 6 -- Application: Recurring Decimals (1:30)**
- Section divider
- "When you compute 1/7 by long division, the remainders repeat. Why?"
- The remainder at each step is between 1 and 6. After 7 steps, by PHP, some remainder repeats → the decimal recurs
- Visual: long division of 1/7, showing remainders cycling
- "This is why every rational number has a recurring (or terminating) decimal expansion"
- Content budget: setup + long division visual + PHP connection + generalization

**Scene 7 -- Application: Party Handshakes / Friends (1:00)**
- Section divider
- "At a party of n ≥ 2 people, there are always at least two people with the same number of friends at the party."
- Possible friend counts: 0, 1, 2, ..., n-1 (n possibilities for n people)
- But if someone has 0 friends, no one has n-1 friends (and vice versa) — so at most n-1 distinct values for n people
- By PHP: two people must have the same count
- Visual: graph with vertices and edges, highlight two vertices with same degree in ACCENT
- Content budget: statement + friend count analysis + PHP application

**Scene 8 -- Application: Sequences and Subsequences (1:00)**
- Section divider
- "Any sequence of n² + 1 distinct real numbers contains either an increasing subsequence of length n+1 or a decreasing subsequence of length n+1."
- For each position, record (i, d) where i = length of longest increasing subsequence ending here, d = length of longest decreasing subsequence ending here
- Both i and d are between 1 and n — so only n² possible pairs
- With n² + 1 positions, by PHP, two positions share the same (i, d) pair — contradiction (distinct numbers can't both be longest)
- So either some i ≥ n+1 or some d ≥ n+1
- Visual: sequence of numbers, highlight an increasing subsequence in PRIMARY, decreasing in RED
- "This is the Erdős–Szekeres theorem — a deep result from a simple principle"
- Content budget: theorem statement + pigeon labeling + contradiction argument

**Scene 9 -- Summary of Power (0:30)**
- Section divider
- Quick recap of what PHP gives us:
  - Certainty from quantity alone
  - The generalized form: ⌈n/k⌉ guarantee
  - Applications across number theory, graph theory, sequences
- Bridge to Video 86: "Graph theory is built on connections — and the pigeonhole principle will appear again"
- Content budget: 3 summary items + graph theory teaser

**Scene 10 -- Summary + Outro (0:30)**
- Recap: PHP says n+1 pigeons in n holes forces a collision
- Generalized: n items in k holes → at least ⌈n/k⌉ per hole
- Proof by contradiction: assume uniformity, derive impossibility
- Applications: birthdays, recurring decimals, friend counts, subsequences
- Next video: Graph Theory Basics — vertices, edges, and connections
- Content budget: 4 summary items + next preview
