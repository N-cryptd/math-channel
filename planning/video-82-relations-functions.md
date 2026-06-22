# Video 82: Relations and Functions
## Discrete Mathematics — Video 4 of 12

**Predecessor:** Video 81 (Sets and Operations)
**Next:** Video 83 (Equivalence Relations)

### Competitive Analysis

YouTube metadata API returned minimal data (2026-06-22). Analysis based on known competitor content:

- **TrevTutor**: "Discrete Math 8 — Relations" (~660K views, screen whiteboard, 14 min). Covers relation definition, directed graphs, properties (reflexive, symmetric, antisymmetric, transitive), partial/total orders. Low production quality, covers properties mechanically without visual intuition. 4.5/10.
- **Dr. Trefor Bazett**: "Relations" in discrete math playlist (~200K views, iPad whiteboard, 12 min). Clean lecture style, covers relation definition, directed graphs, properties. No animations. 6.5/10.
- **Khan Academy**: "Relations and functions" module. Multiple short videos. No Manim animations, basic graphics only.
- **Organic Chemistry Tutor**: No discrete math relations content.
- **3Blue1Brown**: No discrete math content.

**MAJOR GAP:** No high-quality Manim-animated video covers relations and functions in discrete math. TrevTutor's screen whiteboard is the most-viewed resource but lacks visual sophistication. We continue our unique position as the only Manim-animated discrete math series.

### Key Differentiators
1. Animated directed graphs: nodes with colored arrows showing relation pairs
2. Color-coded relation properties: reflexive loops (PRIMARY), symmetric pairs (SECONDARY), transitive chains (ACCENT)
3. Visual mapping diagrams: domain → codomain arrows for functions
4. Animated injective/surjective/bijective proofs on mapping diagrams
5. Bridge from Video 81: relations are built from Cartesian products
6. Connection to upcoming Video 83 (Equivalence Relations): preview the payoff

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Domain / source set | PRIMARY | #5BC0EB |
| Codomain / target set | SECONDARY | #7BC950 |
| Relation arrows | ACCENT | #FFD166 |
| Reflexive loops | PRIMARY | #5BC0EB |
| Symmetric pairs | SECONDARY | #7BC950 |
| Transitive chains | ACCENT | #FFD166 |
| Functions (well-defined) | WHITE | #FFFFFF |
| Not a function (violations) | RED | #EF476F |

### Structure (12 minutes, 10 scenes)

**Scene 1 — Hook: From Sets to Relationships (1:00)**
- Last video (81): we learned about sets — collections of objects
- But in math, we care about how objects relate to each other
- Examples: "is less than", "is a friend of", "divides evenly"
- These aren't just properties of single objects — they're CONNECTIONS between pairs
- A relation is a way to capture these connections mathematically
- Content budget: 4 motivating examples + the concept of connections

**Scene 2 — What is a Relation? (1:00)**
- Section divider
- Definition: A relation R from set A to set B is a subset of A × B (Cartesian product)
- Visual: show two small sets A = {1, 2, 3}, B = {a, b}, then A × B as a grid
- Highlight selected cells of the grid = the relation R
- Arrow diagram: elements of A on left, B on right, arrows for each pair in R
- If A = B, it's a "relation on A"
- Content budget: definition + grid visual + arrow diagram (3 items)

**Scene 3 — Directed Graphs (1:00)**
- Section divider
- A relation on a set can be drawn as a directed graph (digraph)
- Elements = vertices, ordered pairs = directed arrows
- Example: R = {(1,2), (2,3), (1,1)} on {1,2,3} — draw the digraph
- Loop arrow at 1 for (1,1)
- Content budget: digraph definition + animated example

**Scene 4 — Reflexive Relations (1:00)**
- Section divider
- Definition: R is reflexive if (a, a) ∈ R for every a ∈ A
- Visual: every vertex has a loop — PRIMARY color loops
- Example: "≤" on real numbers is reflexive (every number ≤ itself)
- Non-example: "<" on real numbers (no element is < itself)
- Content budget: definition + reflexive digraph + example pair

**Scene 5 — Symmetric Relations (1:00)**
- Section divider
- Definition: R is symmetric if (a,b) ∈ R implies (b,a) ∈ R
- Visual: every arrow has a return arrow — SECONDARY color pair
- Example: "is a sibling of" is symmetric
- Non-example: "is less than" (if a < b, not b < a)
- Content budget: definition + symmetric digraph + example pair

**Scene 6 — Transitive Relations (1:00)**
- Section divider
- Definition: R is transitive if (a,b) ∈ R and (b,c) ∈ R implies (a,c) ∈ R
- Visual: chain of arrows a→b→c implies a→c must exist — ACCENT color
- Example: "≤" is transitive (a≤b and b≤c → a≤c)
- Non-example: "is a friend of" (a knows b, b knows c, doesn't mean a knows c)
- Content budget: definition + transitive chain animation + example pair

**Scene 7 — From Relations to Functions (1:00)**
- Section divider
- A function is a special kind of relation with extra constraints
- Definition: A function f: A → B is a relation where for every a ∈ A, there exists exactly one b ∈ B with (a, b) ∈ f
- Two requirements: (1) Every a ∈ A must appear, (2) Each a maps to only one b
- Visual: mapping diagram from domain A to codomain B — every element of A has exactly one arrow
- Non-function example: element with two arrows (RED)
- Non-function example: element with no arrows (RED)
- Notation: f(a) = b instead of (a, b) ∈ f
- Content budget: definition (2 constraints) + valid function + non-function (2 items)

**Scene 8 — Types of Functions (1:00)**
- Section divider
- Injective (one-to-one): different inputs → different outputs. f(a) = f(b) → a = b. Visual: no two arrows point to same element
- Surjective (onto): every element of codomain is hit. Visual: every element of B has an incoming arrow
- Bijective (both): injective AND surjective. Perfect pairing.
- Example: f(x) = 2x on integers → even integers (injective but not surjective onto Z)
- Example: f(x) = x^2 on R → R (not injective, not surjective)
- Content budget: 3 definitions + visual examples

**Scene 9 — Composition (0:30)**
- Functions compose: (g ∘ f)(x) = g(f(x))
- Visual: A → B → C, two mappings chained
- Brief example: f(x) = x + 1, g(x) = 2x → g(f(3)) = g(4) = 8
- Properties carry over: composition of injective functions is injective
- Content budget: composition visual + one example

**Scene 10 — Summary + Outro (0:30)**
- Recap: relations = subsets of A × B → digraphs visualize them
- Key properties: reflexive, symmetric, transitive
- Functions = special relations (every input → exactly one output)
- Types: injective, surjective, bijective
- Next video: Equivalence Relations — relations with all three properties!
- Content budget: 3 summary items + next preview
