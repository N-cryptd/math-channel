# Video 97: Existence and Uniqueness Proofs

**Playlist:** Introduction to Proofs (Video 8 of 9)
**Level:** Undergraduate (Discrete Math / Proof-Based Mathematics)
**Class:** Video97_ExistenceUniqueness
**Script:** scripts/undergraduate/video-97-existence-uniqueness.py

## Prerequisites
- Video 90: Introduction to Proofs (why we prove things)
- Video 93: Direct Proof
- Video 93: Proof by Contradiction
- Video 96: Proof by Cases
- Basic familiarity with quantifiers (∃ and ∀)

## Learning Objectives
1. Understand the difference between existence and uniqueness claims
2. State the formal structure: ∃! x, P(x) means "there exists exactly one x such that P(x)"
3. Apply constructive existence proofs (find/exhibit the object)
4. Apply non-constructive existence proofs (prove it must exist without finding it)
5. Apply uniqueness proofs (assume two solutions, show they are equal)
6. Combine existence + uniqueness into a complete proof

## Competitive Analysis References
- Analysis: channel-analysis/improvements.md (2026-07-03 entry)
- Trefor Bazett's existence proofs: adopt clean distinction between constructive and non-constructive
- Kimberly Brehm's practical examples: incorporate real-number examples alongside discrete
- Key gap: No competitor comprehensively covers BOTH existence AND uniqueness in one video
- Our edge: Unified treatment with visual "detective" metaphor, progressive examples from easy to hard

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — The Detective and the Thief (~40s)
**Visual:** A detective (magnifying glass icon) looking at a set of footprints.
Question: "Is there a thief?" = existence. "Is there exactly ONE thief?" = uniqueness.
Two colored badges: EXISTS (green check) and UNIQUE (gold star).
**Content:** "In every proof we have asked: is this statement TRUE? But some of the most powerful results in mathematics answer a different question: does a solution EXIST? And if so, is it the ONLY one? Today we will master both types of proof — existence and uniqueness — and learn how they combine into one of the most satisfying proof structures in all of mathematics."
**Elements:** Detective icon, "EXISTS?" badge, "UNIQUE?" badge, footprints visual
**Content budget:** 4 elements max

### Scene 2: Two Types of Claims (~50s)
**Visual:** Side-by-side comparison.
Left column: Existence claim — ∃x, P(x) — "At least one object satisfies P"
Right column: Uniqueness claim — ∃!x, P(x) — "Exactly one object satisfies P"
Expand ∃!x as: ∃x, P(x) ∧ ∀y∀z, (P(y) ∧ P(z)) → y = z
**Content:** "There are two fundamentally different questions. Existence asks: is there at least one object with property P? The quantifier is the existential: there exists. Uniqueness asks: is there exactly one? The quantifier is exists-unique, and it means two things at once: at least one exists, AND any two that exist must be the same object."
**Elements:** Two columns, quantifier formulas, expanded definition
**Content budget:** 5 elements (progressive reveal)

### Scene 3: Constructive Existence Proofs (~60s)
**Visual:** Step-by-step example with "construction" visual (building blocks).
- Claim: There exists an integer n such that 2n + 1 = 7
- Solution: Let n = 3. Then 2(3) + 1 = 7. Done.
- Green checkmark: We EXHIBITED the witness n = 3
- Key label: "The witness: the object that proves existence"
**Content:** "The simplest existence proof: just find the object. This is called a constructive proof. We literally exhibit a witness — a specific object that satisfies the property. There is an integer n such that 2n + 1 equals 7. Let n equal 3. Check: 2 times 3 plus 1 equals 7. We are done. The witness IS the proof."
**Elements:** Claim, solution step, checkmark, witness label
**Content budget:** 4 elements

### Scene 4: Non-Constructive Existence Proofs (~70s)
**Visual:** Contrast constructive vs. non-constructive side by side.
- Example: Prove that there exist irrational numbers a, b such that a^b is rational.
- Proof: We know sqrt(2)^sqrt(2) is either rational or irrational (proof by cases).
  Case 1: It is rational. Done — a = sqrt(2), b = sqrt(2).
  Case 2: It is irrational. Then (sqrt(2)^sqrt(2))^sqrt(2) = sqrt(2)^2 = 2, which is rational. Done — a = sqrt(2)^sqrt(2), b = sqrt(2).
- Key insight: "We proved existence WITHOUT finding the actual values!"
- Visual: "?" marks where the actual value would go
**Content:** "Sometimes we can prove something exists without ever finding it. This is a non-constructive existence proof. Consider: are there irrational numbers a and b such that a to the power b is rational? We know root 2 to the power root 2 is either rational or irrational. If it is rational, done. If it is irrational, raise it to the power root 2, and you get root 2 squared equals 2, which IS rational. In either case, such a pair exists — but we never determined which case we are in! We proved existence without knowing the answer."
**Elements:** Claim, case split, "?" placeholders, key insight label
**Content budget:** Progressive reveal, max 5 at a time

### Scene 5: Uniqueness Proofs — The Method (~50s)
**Visual:** Template/pattern with animated "assumption → contradiction" flow.
- To prove uniqueness: assume x and y both satisfy P. Show x = y.
- Template: "Assume P(x) and P(y). Then ... therefore x = y."
- Visual: Two objects (x and y) starting apart, an arrow pushing them together until they overlap → "same object!"
**Content:** "Uniqueness proofs have a beautiful template. To prove there is at most one object with property P, assume two such objects exist — call them x and y — and then show they must be equal. The logic is clean: if ANY two objects with the property are forced to be the same, then there can be at most one."
**Elements:** Template formula, two-object visual, merge animation, key label
**Content budget:** 4-5 elements

### Scene 6: Example — Unique Solution to an Equation (~80s)
**Visual:** Full existence + uniqueness proof.
- Claim: The equation 3x - 5 = 10 has a unique solution in the reals.
- Existence: Let x = 5. Then 3(5) - 5 = 10. Done.
- Uniqueness: Suppose 3x - 5 = 10 and 3y - 5 = 10. Then 3x = 3y, so x = y.
- QED badge with both EXISTS and UNIQUE stamps
**Content:** "Let us put it all together. Claim: the equation 3x minus 5 equals 10 has a unique real solution. First, existence: let x equal 5. Check: 3 times 5 minus 5 equals 10. A witness exists. Second, uniqueness: suppose x and y both satisfy the equation. Then 3x minus 5 equals 10 and 3y minus 5 also equals 10. Subtracting, 3x minus 3y equals 0, so x equals y. There can be at most one. Combine both parts: exactly one solution exists. QED."
**Elements:** Claim, existence proof, uniqueness proof, QED with dual stamps
**Content budget:** Progressive reveal, max 5 at a time

### Scene 7: Example — Uniqueness of Multiplicative Inverse (~80s)
**Visual:** Proof in abstract algebra style.
- Claim: Every nonzero real number a has a unique multiplicative inverse.
- Existence: Let x = 1/a (which exists since a ≠ 0). Then ax = a · (1/a) = 1. Done.
- Uniqueness: Suppose ax = 1 and ay = 1. Then ax = ay. Multiply both sides by 1/a: x = y.
- Connect to: "This is why we write a^{-1} — it names the UNIQUE inverse."
**Content:** "A more abstract example. Claim: every nonzero real number a has exactly one multiplicative inverse. Existence: let x equal 1 over a. Since a is nonzero, this is defined, and a times 1 over a equals 1. Uniqueness: suppose x and y are both inverses of a. Then a times x equals 1 and a times y equals 1, so a times x equals a times y. Multiplying both sides by 1 over a gives x equals y. This is exactly why notation like a to the power negative 1 works — there is only one object to name."
**Elements:** Claim, existence step, uniqueness step, notation insight
**Content budget:** Progressive reveal, max 5 at a time

### Scene 8: Summary — The Complete Recipe (~45s)
**Visual:** Summary flowchart with the two-part recipe.
- Step 1: EXISTENCE — Find or construct a witness (or use non-constructive argument)
- Step 2: UNIQUENESS — Assume two, show they are equal
- Together: ∃!x, P(x) = existence ∧ uniqueness
- Key: "Uniqueness without existence is meaningless!"
- Teaser for next video: Proof Writing Style
**Content:** "To wrap up: existence and uniqueness proofs answer two questions. First: does a solution exist? Prove it with a constructive witness or a non-constructive argument. Second: is it the only one? Assume two solutions and show they must coincide. Together, these give you the powerful exists-unique quantifier. One warning: proving uniqueness without proving existence first is meaningless — you might show there is at most one, but zero solutions also satisfy that. Next up: proof writing style."
**Elements:** Two-step recipe, ∃! expansion, warning note, next video card
**Content budget:** 4-5 elements
