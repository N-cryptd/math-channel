# Video 80: Predicate Logic
## Discrete Mathematics — Video 2 of 12

**Predecessor:** Video 79 (Propositional Logic)
**Next:** Video 81 (Sets and Operations)

### Competitive Analysis

Based on analysis in channel-analysis/improvements.md (2026-06-21):
- **MASSIVE GAP:** No high-quality Manim-animated predicate logic video exists on YouTube
- All competitors (TrevTutor, Khan Academy) use whiteboard/lecture format
- We continue our unique position as the only Manim-animated discrete math series
- Following Video 79's success with color-coded truth tables, we'll color-code quantifiers

### Key Differentiators
1. Animated domain visualization: show a set of objects as dots, then highlight which ones satisfy the predicate
2. Color-coded quantifiers: ∀ in PRIMARY (blue), ∃ in SECONDARY (green) — visual distinction
3. Negation push-through animation: NOT past quantifiers (De Morgan's for predicates)
4. Nested quantifier visual: grid/matrix showing which pairs satisfy a two-variable predicate
5. Connection to propositional logic: bridge from Video 79's truth tables to predicate evaluation

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Universal quantifier ∀ | PRIMARY | #5BC0EB |
| Existential quantifier ∃ | SECONDARY | #7BC950 |
| Predicates P, Q | ACCENT | #FFD166 |
| Domain elements | WHITE | #FFFFFF |
| Free variables | RED | #EF476F |
| Bound variables | DIM | #6B6B8D |
| Negation ¬ | RED | #EF476F |
| TRUE/T satisfied | SECONDARY | #7BC950 |
| FALSE/F unsatisfied | RED | #EF476F |

### Structure (12 minutes, 9 scenes)

**Scene 1 — Hook: The Limitation of Propositional Logic (1:00)**
- Recall from Video 79: propositions are statements that are true or false
- But what about: "x > 3"? This isn't a proposition — it depends on x
- "Every student passed the exam" — how do we express "every"?
- Propositional logic can't handle variables and "for all"/"there exists"
- Motivating: we need a richer language
- Content budget: 3 motivating statements + the gap

**Scene 2 — Predicates (1:00)**
- Section divider
- Definition: A predicate is a statement that becomes a proposition when you substitute values for its variables
- Notation: P(x), Q(x, y), etc.
- Example: P(x) = "x is even", Q(x, y) = "x > y"
- When x = 4, P(4) = TRUE; when x = 7, P(7) = FALSE
- Visual: show P(x) with different values being substituted
- Content budget: definition + 2 predicate examples

**Scene 3 — The Domain of Discourse (1:00)**
- Section divider
- The domain (universe) specifies what values x can take
- Same predicate, different domain = different truth values
- Example: P(x) = "x > 0" — over natural numbers vs. over all integers
- Visual: show domain as a set of dots; highlight which ones satisfy P
- Content budget: definition + domain comparison example

**Scene 4 — Universal Quantifier (1:30)**
- Section divider
- ∀x P(x) means "for all x in the domain, P(x) is true"
- ∀ reads as "for all" or "for every"
- Example: ∀x (x ≥ 0) over natural numbers — TRUE
- ∀x (x ≥ 0) over integers — FALSE (because -1 exists)
- Visual: domain as dots, check mark on every one (all green)
- Content budget: definition + 2 examples with visual

**Scene 5 — Existential Quantifier (1:30)**
- Section divider
- ∃x P(x) means "there exists some x in the domain such that P(x) is true"
- ∃ reads as "there exists" or "for some"
- Example: ∃x (x > 10) over natural numbers — TRUE (e.g., x = 11)
- ∃x (x < 0) over natural numbers — FALSE
- Visual: domain as dots, one highlighted (one green)
- Content budget: definition + 2 examples with visual

**Scene 6 — Free vs Bound Variables (1:00)**
- Section divider
- In ∀x P(x), x is bound (captured by the quantifier)
- In P(x) with no quantifier, x is free (needs a value)
- A statement with free variables is not a proposition
- A statement with only bound variables IS a proposition
- Color: free vars in RED, bound vars in DIM
- Content budget: definition + examples of each type

**Scene 7 — Negating Quantified Statements (1:30)**
- Section divider
- ¬∀x P(x) ≡ ∃x ¬P(x) — "not for all" = "there exists some that doesn't"
- ¬∃x P(x) ≡ ∀x ¬P(x) — "there doesn't exist" = "for all, not"
- These are De Morgan's laws for quantifiers!
- Visual: animated transformation — NOT pushes through the quantifier and flips ∀↔∃
- Real-world: "Not everyone passed" = "Someone failed"
- Content budget: 2 laws + animated transformation + example

**Scene 8 — Nested Quantifiers (1:30)**
- Section divider
- ∀x ∃y P(x, y) — "for every x, there exists some y such that..."
- Example: ∀x ∃y (y > x) over natural numbers — TRUE (y = x + 1)
- Order matters: ∃x ∀y P(x, y) ≠ ∀y ∃x P(x, y) in general
- Visual: grid/matrix of dots showing evaluation
- Content budget: 1 nested example + order-reversal comparison

**Scene 9 — Summary + Outro (0:30)**
- Recap: predicates → domains → ∀ and ∃ → free/bound → negation → nesting
- "This is the language that mathematicians use every day"
- Next: Sets and Operations — predicates are closely related to set membership
- Content budget: 3 summary items
