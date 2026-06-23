# Video 83: Equivalence Relations
## Discrete Mathematics — Video 5 of 12

**Predecessor:** Video 82 (Relations and Functions)
**Next:** Video 84 (Counting Principles)

### Competitive Analysis

Analyzed 6 competitor videos on equivalence relations (2026-06-22):

- **Dr. Trefor Bazett**: "Equivalence Relations" (194K views, 4:36, iPad whiteboard). Short, definition-focused, no equivalence classes or partitions. 3/10 visual quality. 4.5/10 overall.
- **Kimberly Brehm**: "9.5.1 Equivalence Relations" (144K views, 22:30, tablet whiteboard). Full coverage with video chapters, covers classes + partitions + mod 4. Well-structured but visually static. 5/10 overall.
- **Neso Academy**: "Equivalence Relation" (316K views) + "Equivalence Classes" (403K views, slide-based). Split across two videos, high views from subscriber base. 4/10 overall.
- **TrevTutor**: "RELATIONS" (1M+ views, 15:36, screen whiteboard). Broad coverage, shallow on equivalence specifically. 3.5/10 overall.
- **Wrath of Math**: "What is an Equivalence Relation?" (41K views, 5:01). Good conversational tone, good non-examples. 5/10 overall.

**MAJOR GAP:** No high-quality animated video unifies equivalence relations + classes + partitions + modular arithmetic in one visual presentation. All competitors use static whiteboards or slides. We continue our unique Manim-animated position.

### Key Differentiators
1. **Animated digraphs** with color-coded properties: reflexive loops (PRIMARY), symmetric pairs (SECONDARY), transitive chains (ACCENT) — building on Video 82's visual vocabulary
2. **Visual partitions**: animated set-splitting showing how equivalence classes divide the set into colored "buckets"
3. **Number line animation** for modular arithmetic equivalence classes
4. **Progressive reveal** from individual properties → combined definition → deep result (partition theorem)
5. **Unified coverage** in one video (competitors split this across 2-3 videos)

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Reflexive property / loops | PRIMARY | #5BC0EB |
| Symmetric property / pairs | SECONDARY | #7BC950 |
| Transitive property / chains | ACCENT | #FFD166 |
| Equivalence class [a] | WHITE | #FFFFFF |
| Partition blocks | PRIMARY/SECONDARY/ACCENT | mixed |
| Not an equivalence relation | RED | #EF476F |
| Modular arithmetic examples | ACCENT | #FFD166 |

### Structure (13 minutes, 10 scenes)

**Scene 1 — Hook: The Power of "Same As" (1:30)**
- Last video: we learned relations can be reflexive, symmetric, transitive — separately
- But what happens when a relation has ALL THREE properties at once?
- Real-world examples: "same birthday", "same blood type", "same nationality"
- These "same as" relations share a deep structure — they split the world into groups
- A relation with all three properties is called an EQUIVALENCE RELATION
- Content budget: 3 real-world examples + concept of grouping

**Scene 2 — Definition: Equivalence Relation (1:00)**
- Section divider
- Definition: R is an equivalence relation on A if R is reflexive AND symmetric AND transitive
- Visual: recall the three properties with their color coding from Video 82
- Animated digraph on small set showing all three simultaneously
- The "triple crown" — all loops, all symmetric pairs, all transitive closures
- Content budget: definition + animated digraph with all 3 properties

**Scene 3 — Examples: Which Relations Are Equivalence Relations? (1:30)**
- Section divider
- Example 1: = (equals) on real numbers. Reflexive: a = a ✓. Symmetric: if a = b then b = a ✓. Transitive: if a = b and b = c then a = c ✓. YES — the simplest equivalence relation.
- Example 2: ≤ (less than or equal) on real numbers. Reflexive: a ≤ a ✓. Transitive: if a ≤ b and b ≤ c then a ≤ c ✓. But NOT symmetric: a ≤ b does not imply b ≤ a (e.g., 1 ≤ 2 but 2 ≰ 1). NO.
- Example 3: "has same parity as" on integers. Reflexive: n has same parity as n ✓. Symmetric ✓. Transitive: if n ~ m and m ~ k, then n and k have same parity ✓. YES.
- Content budget: 3 examples with property checks (progressive reveal, one at a time)

**Scene 4 — Equivalence Classes (1:30)**
- Section divider
- When we have an equivalence relation, every element a belongs to a GROUP
- Definition: [a] = {b ∈ A : b ~ a} — the equivalence class of a
- Visual: small set {1, 2, 3, 4, 5} with relation "same parity as"
- Show [1] = {1, 3, 5} highlighted in PRIMARY color
- Show [2] = {2, 4} highlighted in SECONDARY color
- Key insight: [a] = [b] if and only if a ~ b
- Content budget: definition + animated class highlight + insight

**Scene 5 — Equivalence Classes: Modular Arithmetic (1:30)**
- Section divider
- The canonical example: congruence mod n
- Definition: a ≡ b (mod n) iff n divides (a − b)
- Check: reflexive (n|0 ✓), symmetric (if n|(a−b) then n|(b−a) ✓), transitive ✓
- Visual: number line with Z, mod 3 equivalence classes
- [0] = {..., −6, −3, 0, 3, 6, 9, ...} highlighted in PRIMARY
- [1] = {..., −5, −2, 1, 4, 7, 10, ...} highlighted in SECONDARY
- [2] = {..., −4, −1, 2, 5, 8, 11, ...} highlighted in ACCENT
- Content budget: definition + mod 3 visual with three colored classes on number line

**Scene 6 — Partitions (1:00)**
- Section divider
- Definition: A partition of A is a collection of non-empty, disjoint subsets whose union is A
- Three requirements: (1) Each block is non-empty, (2) Blocks are pairwise disjoint, (3) Union covers A
- Visual: set A splits into colored blocks — animated partition
- Content budget: definition (3 requirements) + animated partition visual

**Scene 7 — The Deep Connection: Equivalence Relations = Partitions (1:30)**
- Section divider
- Theorem: Every equivalence relation on A defines a partition of A (its equivalence classes)
- Theorem: Every partition of A defines an equivalence relation (a ~ b iff they're in the same block)
- Visual: show the two-way bridge — equivalence relation ↔ partition
- Animated: equivalence classes forming partition, then partition defining relation
- Content budget: 2 theorems + two-way visual bridge

**Scene 8 — Proof Sketch: Classes Form a Partition (1:00)**
- Section divider
- Need to show: (1) Classes are non-empty, (2) Classes are disjoint or identical, (3) Union covers A
- (1) Reflexive: a ~ a, so a ∈ [a]. Non-empty ✓
- (2) Key lemma: if [a] ∩ [b] ≠ ∅, then [a] = [b]. Proof: if c ∈ both, then c ~ a and c ~ b. By symmetry a ~ c. By transitivity a ~ b. So everything in [a] is in [b] and vice versa.
- (3) Every a ∈ A is in [a], so union covers A ✓
- Visual: animated proof with digraph highlighting
- Content budget: 3-part proof sketch with visual support

**Scene 9 — Practice: Another Partition Example (0:30)**
- Section divider
- Example: Let A = {students in a class}, relation = "same major"
- Check: reflexive (same major as self ✓), symmetric ✓, transitive ✓
- Equivalence classes: all CS students, all math students, all physics students, etc.
- This partitions the class by major — visual animation
- Content budget: 1 worked example + partition visual

**Scene 10 — Summary + Outro (0:30)**
- Recap: equivalence relation = reflexive + symmetric + transitive
- Equivalence classes [a] = all elements related to a
- Every equivalence relation partitions the set, and every partition defines an equivalence relation
- Modular arithmetic is the canonical example
- Next video: Counting Principles — if we can partition, we can count!
- Content budget: 3 summary items + next preview
