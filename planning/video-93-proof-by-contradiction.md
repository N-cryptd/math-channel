# Video 93: Proof by Contradiction

**Playlist:** Introduction to Proofs (Proof-Based Mathematics, Level 4)
**Prerequisites:** Video 90 (Why Proofs?), Video 91 (Direct Proof), Video 92 (Contrapositive)
**Target Duration:** 10-12 minutes
**Class:** `Video93_ProofByContradiction`

## Competitive Analysis Summary

Based on analysis of 4 competitor videos (Numberphile, Mathologer, Bright Side of Mathematics, Wrath of Math):
- **3.5M+ aggregate views** — very strong demand
- **Zero Manim-animated proof-by-contradiction videos** exist — we fill this gap entirely
- No competitor covers all four key topics in one video (general technique + sqrt(2) + primes + vs contrapositive)
- Numberphile leads with ~2M views using conversational blackboard format; Mathologer has best visuals but only covers sqrt(2)
- Key opportunity: animated "contradiction explosion" moment, assumption tracker, and explicit contrapositive distinction

Full analysis: `channel-analysis/improvements_proof_by_contradiction.md`

## Learning Objectives

1. Understand the logic of proof by contradiction: assume P ∧ ¬Q, derive False
2. Recognize when contradiction is the right tool (vs direct proof or contrapositive)
3. Work through the classic proof that sqrt(2) is irrational
4. Work through Euclid's proof of the infinitude of primes
5. Distinguish contradiction from contrapositive (linking back to Video 92)

## Scenes

### Scene 1: Hook — The Impossible Assumption (~25s)

**Concept:** What if we assume something we know is false, and show it breaks math itself?

**Visual:** A clean equation that slowly "cracks" and turns red, leading to a spark/explosion effect. The word "CONTRADICTION!" flashes on screen.

**Narration beats:**
- "Imagine proving something is true by showing that if it were false, mathematics itself would break."
- "That's proof by contradiction — one of the most powerful tools in all of mathematics."

---

### Scene 2: The Logic — How Contradiction Works (~60s)

**Concept:** Formal structure: To prove P → Q, assume P ∧ ¬Q, derive a contradiction.

**Visual elements:**
- Logical structure diagram: `P ∧ ¬Q → (chain of reasoning) → False ⊥`
- Color coding: Assumption box in PRIMARY (blue), deductions in SECONDARY (green), the final ⊥ in RED
- Comparison alongside the direct proof structure (from Video 91): `P → (reasoning) → Q`
- Brief truth-table-style note: if assuming ¬Q leads to False, then Q must be True

**Narration beats:**
- "In a direct proof, we assume P and walk toward Q."
- "In proof by contradiction, we assume the OPPOSITE — that P is true but Q is false."
- "Then we reason forward. If we hit a contradiction — something that cannot be true — our assumption must have been wrong."
- "Therefore Q must be true."

---

### Scene 3: When to Use Contradiction (~40s)

**Concept:** Strategy selection — when is contradiction better than direct or contrapositive?

**Visual elements:**
- Three columns: Direct Proof / Contrapositive / Contradiction
- Brief labels for each:
  - Direct: "Clear path P → Q"
  - Contrapositive: "P → Q seems blocked; ¬Q → ¬P looks easier"
  - Contradiction: "The statement involves 'not exists' or 'there is no', or assuming the opposite creates an object we can analyze"
- Key signal words: "irrational", "infinite", "no solution", "cannot", "unique"

**Narration beats:**
- "How do you know when to use contradiction? There are signals."
- "Statements about irrationality, infinity, or non-existence are classic candidates."
- "The key idea: assume the opposite, and you get a concrete object to work with — a rational number, a finite list, a solution — that you can then show leads to absurdity."

---

### Scene 4: Example 1 — sqrt(2) is Irrational (~150s)

**Concept:** The most famous proof by contradiction. Show that sqrt(2) cannot be written as a/b in lowest terms.

**Visual elements (step-by-step animated):**
1. **Assumption box appears** (PRIMARY): "Assume sqrt(2) = a/b where a, b are integers with no common factor"
2. **Step 1:** Square both sides: `2 = a²/b²` → `a² = 2b²` → "a² is even" (SECONDARY)
3. **Step 2:** Therefore `a` is even (link to Video 91's proof: if a² is even, a is even) → `a = 2k`
4. **Step 3:** Substitute: `4k² = 2b²` → `b² = 2k²` → "b² is even" → "b is even"
5. **Contradiction spark**: Both a and b are even — but we assumed NO common factor! (RED flash, assumption box cracks/breaks)
6. **Conclusion** (ACCENT): "Therefore sqrt(2) is irrational"

**Narration beats:**
- Walk through each algebraic step clearly
- Pause at the contradiction moment for emphasis
- Note: "This proof is over 2,000 years old and it's still beautiful"

---

### Scene 5: Example 2 — Infinitude of Primes (~130s)

**Concept:** Euclid's proof. Show that there is no largest prime.

**Visual elements (step-by-step animated):**
1. **Assumption box** (PRIMARY): "Assume there are only finitely many primes: p₁, p₂, ..., pₙ"
2. **Construct N:** `N = p₁ × p₂ × ... × pₙ + 1`
3. **Key insight:** N is either prime itself, or divisible by a prime not in our list
4. **Analyze:** If N is prime → contradiction (we missed it). If N has a factor → that factor doesn't divide N-1, so it's a new prime → contradiction
5. **Contradiction spark** (RED): Our list was supposed to be COMPLETE
6. **Conclusion** (ACCENT): "Therefore there are infinitely many primes"

**Visual enhancement:** Show the primes as a row of numbered boxes; show N being constructed; animate the "either/or" branching; both branches lead to the same red contradiction

**Narration beats:**
- "Euclid proved this around 300 BCE. The argument is stunningly simple."
- Walk through the construction step by step
- "No matter how many primes you have, there's always one more."

---

### Scene 6: Contradiction vs Contrapositive (~50s)

**Concept:** Explicit comparison — they're different techniques with different structures.

**Visual elements:**
- Side-by-side comparison (two columns):
  - **Contrapositive (Video 92):** Prove ¬Q → ¬P directly. The statement is EQUIVALENT to P → Q.
  - **Contradiction (This video):** Assume P ∧ ¬Q, derive ANY contradiction. The contradiction could be anything.
- Key distinction highlighted:
  - Contrapositive: "You prove a specific equivalent statement"
  - Contradiction: "You assume the negation and hunt for ANY absurdity"
- Venn diagram or decision tree for "which technique?"

**Narration beats:**
- "If you've seen Video 92, you might be wondering: how is this different from contrapositive?"
- "In contrapositive, you prove an equivalent statement: not-Q implies not-P, and you prove it directly."
- "In contradiction, you assume P AND not-Q together, and derive any contradiction at all — not necessarily arriving at not-P."
- "They're related but distinct. Contradiction is more flexible."

---

### Scene 7: Summary & Outro (~30s)

**Concept:** Recap the technique, preview next video.

**Visual elements:**
- Bullet-point summary with color coding:
  - Assume the opposite (PRIMARY)
  - Reason forward (SECONDARY)
  - Find a contradiction (RED)
  - Conclude the original statement (ACCENT)
- Preview card: "Next: Proof by Mathematical Induction"

**Narration beats:**
- "Proof by contradiction: assume the opposite, derive absurdity, conclude the truth."
- "Three classic applications: irrationality of sqrt(2), infinitude of primes, and many more."
- "Next time, we'll tackle proof by mathematical induction — a completely different flavor."

---

## Production Notes

- **Consistent color language** with Videos 90-92: PRIMARY=assumption/hypothesis, SECONDARY=deduction, RED=contradiction/error, ACCENT=conclusion
- **Contradiction "spark" effect** is the signature visual moment — invest animation time here
- **Assumption box** should be a persistent visual element (rounded rectangle with label) that appears at the start of each proof and gets "broken" at the contradiction
- **Scene 4 (sqrt(2))** is the longest scene — it carries the video's educational weight
- **Scene 6 (vs contrapositive)** is critical for playlist coherence — Video 92 viewers need this bridge
- Total estimated time: 25 + 60 + 40 + 150 + 130 + 50 + 30 = ~485s ≈ 8 minutes (comfortably within 10-12 min target with animation pauses)
