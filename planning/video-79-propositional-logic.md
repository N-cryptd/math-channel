# Video 79: Propositional Logic
## Discrete Mathematics — Video 1 of 12

**Predecessor:** Video 78 (Regression Basics) — end of Probability & Statistics playlist
**Next:** Video 80 (Predicate Logic)

### Competitive Analysis

**Competitor landscape:**
- Reducible: "Boolean Algebra & Logic Gates" (~400K views, 18 min, Manim) — Highest quality Manim competitor. CS-framed (logic gates, circuits), not math-framed. Covers Boolean algebra, truth tables, Karnaugh maps. Beautiful animations but skips IMPLIES/IFF (pure logic). 8.6/10 avg.
- Dr. Trefor Bazett: "Propositional Logic" (~180K views, 12 min, iPad whiteboard) — Most-viewed direct competitor. Clean lecture style, covers statements, connectives, truth tables, De Morgan's, logical equivalence. No animations, traditional board. 6.8/10.
- TrevTutor: "Propositional Logic Tutorial" (~500K views, 18 min, screen whiteboard) — High views (early resource), low production quality. Covers syntax, semantics, truth tables, tautologies. 4.8/10.
- Zach Star: "Discrete Math" playlist exists but no dedicated propositional logic video.
- 3Blue1Brown: NO propositional logic content at all.
- Mathologer: NO propositional logic content.
- Looking Glass Universe: NO propositional logic content.
- Khan Academy: Has discrete math logic content in lecture format (slides + annotations). Thorough but dry.

**Common structure across competitors:** Definition of statement → logical connectives → truth tables → De Morgan's laws → tautologies/contradictions → logical equivalence. Most start definition-first with no hook.

**Key gaps to differentiate:**
1. No high-quality Manim-animated pure math propositional logic video exists
2. Nobody opens with a puzzle/paradox (all competitors are definition-first)
3. Nobody animates truth table construction with color-coded columns
4. Nobody visually morphs De Morgan's laws
5. IMPLIES connective is under-explained everywhere (Reducible skips it entirely)
6. Nobody shows the "territory map" metaphor for logical equivalence classes

### Key Differentiators
1. Paradox hook: the liar's paradox or a simple puzzle to motivate the need for formal logic
2. Animated truth table construction with color-coded columns (p = PRIMARY, q = SECONDARY)
3. Visual De Morgan's laws: morph NOT(A AND B) into NOT-A OR NOT-B with animated parentheses
4. Deep IMPLIES coverage: truth table, real-world examples, why "false → anything = true" makes sense
5. "Equivalence classes" visual: showing statements orbiting around the same truth column
6. Target 10-12 min (most competitors are 15-20 min and drag)

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Statement p | PRIMARY | #5BC0EB |
| Statement q | SECONDARY | #7BC950 |
| Connectives (AND, OR, NOT) | ACCENT | #FFD166 |
| IMPLIES / IFF | RED | #EF476F |
| Tautology (always T) | SECONDARY | #7BC950 |
| Contradiction (always F) | RED | #EF476F |
| Equivalence marker | ACCENT | #FFD166 |
| Formulas | WHITE | #FFFFFF |

### Structure (11 minutes, 8 scenes)

**Scene 1 — Hook: The Liar's Paradox (1:00)**
- Motivating puzzle: "This statement is false." — is it true or false?
- A statement that can't be classified — self-referential paradox
- "To avoid paradoxes, mathematicians build logic from carefully defined building blocks"
- Tease: propositional logic gives us a framework for reasoning without ambiguity
- Content budget: paradox text + question

**Scene 2 — What is a Proposition? (1:00)**
- Section divider
- Definition: a declarative sentence that is either true or false (not both)
- Examples: "2 + 3 = 5" (proposition, true), "x > 7" (not a proposition — depends on x), "Close the door!" (not a proposition — command)
- Introduce p and q as propositional variables
- Content budget: definition + 3 examples + variables

**Scene 3 — Logical Connectives (1:30)**
- Section divider
- NOT (negation): ¬p flips truth value. Truth table for ¬p
- AND (conjunction): p ∧ q is true only when both are true. Truth table for p ∧ q
- OR (disjunction): p ∨ q is false only when both are false. Truth table for p ∨ q
- Color-code: p in PRIMARY, q in SECONDARY, connectives in ACCENT
- Content budget: 3 connectives with mini truth tables

**Scene 4 — Implication and Biconditional (2:00)**
- Section divider
- IMPLIES (→): p → q. The tricky one.
- Truth table with emphasis: only FALSE when p is true and q is false
- "A true promise broken is the only violation"
- Real-world examples: "If it rains, I'll bring an umbrella" — all 4 cases explained
- Biconditional (↔): p ↔ q. True when p and q have the same truth value.
- IFF means "if and only if"
- Content budget: implication truth table + example + biconditional truth table

**Scene 5 — Building Truth Tables (1:30)**
- Section divider
- Worked example: build truth table for (p ∧ q) → ¬p
- Show systematic construction: enumerate all combinations, compute sub-expressions column by column
- Animated: columns appear one at a time, color-coded
- Content budget: full truth table + step-by-step animation

**Scene 6 — De Morgan's Laws (1:30)**
- Section divider
- ¬(p ∧ q) ≡ ¬p ∨ ¬q — "NOT both" = "at least one is NOT"
- ¬(p ∨ q) ≡ ¬p ∧ ¬q — "NOT either" = "both are NOT"
- Visual morph: animate the left side transforming into the right side
- Real-world: "It is NOT the case that it is raining AND cold" = "It is NOT raining OR it is NOT cold"
- Content budget: 2 laws + visual transform + example

**Scene 7 — Tautologies, Contradictions, and Equivalence (1:00)**
- Section divider
- Tautology: statement that is always true regardless of truth values (e.g., p ∨ ¬p)
- Contradiction: statement that is always false (e.g., p ∧ ¬p)
- Logical equivalence: two statements with identical truth table columns
- Visual: show p → q and ¬p ∨ q have the same truth table — they're equivalent!
- Content budget: 3 concepts + equivalence visual

**Scene 8 — Summary + Outro (0:30)**
- Recap: propositions → connectives → truth tables → De Morgan's → tautologies/equivalence
- "This is the foundation for everything in discrete math"
- Outro with next video teaser: Predicate Logic
- Content budget: 3 summary items
