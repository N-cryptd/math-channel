# Video 98: Proof Writing Style

**Playlist:** Introduction to Proofs (Video 9 of 9 — FINAL)
**Level:** Undergraduate (Discrete Math / Proof-Based Mathematics)
**Class:** Video98_ProofWritingStyle
**Script:** scripts/undergraduate/video-98-proof-writing-style.py

## Prerequisites
- Videos 90-97: All previous Introduction to Proofs videos
- Direct Proof, Contrapositive, Contradiction, Induction, Strong Induction, Cases, Existence & Uniqueness

## Learning Objectives
1. Understand the standard structure of a well-written proof (Claim → Proof: → Let → ... → Therefore → QED)
2. Recognize the difference between a sloppy proof and a polished proof
3. Learn key notation conventions and when to use formal vs. informal language
4. Apply the "Assumptions → Definitions → Manipulations → Conclusion" template
5. Know when to use words vs. symbols and the principle of progressive disclosure in proof writing

## Competitive Analysis References
- Analysis: channel-analysis/improvements.md (2026-07-03 entry)
- Trefor Bazett's 9 tips: adopt template framework (assumptions → definitions → manipulations → conclusion)
- Graphicode's visual style: modern dark background — our Manim palette already matches
- Key gap: No competitor focuses on proof WRITING STYLE specifically — they cover types or tips, not the craft of clear writing
- Our edge: Before/after proof transformation, animated proof skeleton, notation convention cards, playlist recap montage

## Scene Plan (7 scenes, ~10 min target)

### Scene 1: Hook — Two Proofs, Same Idea (~50s)
**Visual:** Side-by-side — a messy, disorganized proof on the left vs. a clean, structured proof on the right.
- Same claim: "For all integers n, if n is even, then n^2 is even"
- Left proof: rambling, unclear variable intro, skips steps, no QED
- Right proof: clean structure, clear "Let", explicit steps, QED
- Transition: left fades, right stays and becomes the template
**Content:** "You have learned seven proof techniques. Direct proof, contrapositive, contradiction, induction, strong induction, cases, and existence and uniqueness. But knowing a technique is not the same as writing a good proof. Today we focus on style: the structure, language, and conventions that turn a correct argument into a proof that mathematicians actually want to read."
**Elements:** Messy proof text, clean proof text, divider line, arrow
**Content budget:** 4 elements max

### Scene 2: The Proof Skeleton (~60s)
**Visual:** Animated blueprint/skeleton that builds piece by piece.
- Claim (state what you will prove)
- "Proof." (opening declaration)
- Let (introduce variables/assumptions)
- ... (the body: definitions, manipulations)
- Therefore (state the conclusion)
- QED (end mark)
- Each piece appears with a color-coded label and brief description
**Content:** "Every well-written proof follows a skeleton. First, state the claim clearly. Then write the word Proof, followed by a colon or period. Introduce your variables with Let or Suppose. This is the body, where definitions, manipulations, and reasoning live. Finally, Therefore or Hence leads to the conclusion, and QED or a filled square marks the end."
**Elements:** Skeleton diagram with 6 labeled parts, each revealed progressively
**Content budget:** 5 elements (progressive reveal)

### Scene 3: Before and After — The Transformation (~80s)
**Visual:** Animated rewriting of a messy proof into a clean one.
- Example: "If a and b are odd integers, then a + b is even"
- BAD version: "a and b are odd so a=2k+1 and b=2m+1 so a+b=2k+1+2m+1=2(k+m+1) so a+b is even"
  - Problems: no "Let", runs everything together, uses k without defining, no QED
- GOOD version: Proper structure with Let, definitions, algebraic steps, Therefore, QED
  - Each improvement highlighted as it transforms
**Content:** "Here is the same argument, written two ways. The first is correct but unreadable. The second is the same logic, presented clearly. Notice the improvements: variables are introduced with Let, each step is on its own line, the algebra is shown explicitly, and QED marks the end. The logic did not change. Only the presentation did."
**Elements:** Bad proof, transformation arrow, good proof with highlights, improvement labels
**Content budget:** Progressive reveal, max 5 at a time

### Scene 4: Language — Words vs. Symbols (~60s)
**Visual:** Two columns — "Formal" vs "Conversational".
- When to use symbols: quantifiers, set notation, algebraic expressions
- When to use words: logical connectives between ideas, explanations, "therefore"
- Balance: too many symbols → unreadable; too few → imprecise
- Examples: "∀x ∈ ℤ, P(x)" vs "For every integer x, P(x) holds"
- Key rule: "Write for humans, not for computers"
**Content:** "A common question: should you write Therefore or draw an arrow? Should you write for all x in Z or use the universal quantifier? The answer is balance. Use symbols for things that are standard: quantifiers, set notation, algebraic expressions. Use words for logical flow: therefore, since, suppose, let. A proof is a piece of writing meant to be read by a human being."
**Elements:** Two-column comparison, example formulas, key rule text
**Content budget:** 5 elements (progressive reveal)

### Scene 5: Common Pitfalls (~60s)
**Visual:** Warning icons with common mistakes.
- Circular reasoning (assuming what you need to prove)
- Undefined variables (using n without saying what n is)
- Missing QED (proof trails off without conclusion)
- Mixing up converse and contrapositive
- Example of each with a brief correction
**Content:** "There are traps that even experienced mathematicians fall into. Circular reasoning: assuming the very thing you need to prove. Always check that your starting point does not secretly contain the conclusion. Undefined variables: never use a symbol without first saying what it represents. Missing QED: every proof needs a clear ending. And a classic error: confusing the converse with the contrapositive. Remember, the contrapositive is logically equivalent, but the converse is not."
**Elements:** Warning icons, mistake examples, correction labels
**Content budget:** Progressive reveal, max 5 at a time

### Scene 6: Playlist Recap — Your Proof Toolkit (~70s)
**Visual:** Timeline/montage of all 8 previous proof techniques.
- Visual icons/badges for each technique: Direct, Contrapositive, Contradiction, Induction, Strong Induction, Cases, Existence, Uniqueness
- Each appears in sequence along a timeline with a one-line description
- Style tips overlay: "Apply the writing style we just learned to ANY of these techniques"
- This unifies the whole playlist
**Content:** "This brings us to the end of the Introduction to Proofs playlist. You now have a complete toolkit: direct proof for straightforward claims, contrapositive when the conclusion is easier to negate, contradiction for existence results, induction for natural numbers, strong induction when you need the full history, cases for exhaustive arguments, and existence and uniqueness for showing exactly one solution exists. Combine any technique with the writing style we learned today, and you can write proofs that are not just correct, but clear, elegant, and professional."
**Elements:** Timeline with 8 technique badges, style tip overlay, playlist badge
**Content budget:** Progressive reveal, max 5 at a time

### Scene 7: Outro — Where to Go From Here (~40s)
**Visual:** Closing summary with forward-looking teaser.
- Three key takeaways: Structure, Language, Practice
- Teaser for the next playlist (Real Analysis I)
- Animated outro with channel branding
**Content:** "Three things to remember. First, follow the skeleton: Claim, Proof, Let, therefore, QED. Second, write for humans: use symbols where they help, words where they clarify. Third, practice: every proof you write makes the next one easier. Thank you for joining me through this entire Introduction to Proofs playlist. In the next playlist, Real Analysis, we will put these skills to work on the foundations of calculus."
**Elements:** Three takeaway items, next video card, outro animation
**Content budget:** 4 elements
