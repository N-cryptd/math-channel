# Video 224: Solvability by Radicals -- Plan

## Metadata
- **Number:** 224
- **Topic:** Solvability by Radicals
- **Level:** Graduate (Advanced Abstract Algebra)
- **Class:** Video224_SolvabilityByRadicals
- **Script:** scripts/graduate/video-224-solvability-by-radicals.py
- **Builds on:** Video 218 (solvable groups), Video 222 (Galois groups), Video 223 (FTGT)
- **Leads to:** Video 225 (Insolvability of the Quintic)
- **Estimated duration:** 12-15 minutes

## Competitive Analysis

See channel-analysis/improvements.md for existing entries on Video 218, 220, 222, and 223.

**Key competitors for solvability by radicals:**
1. **Mathemaniac** -- "Why you can't solve quintic equations" (549K views, SoME2). The gold standard for animated Galois theory storytelling. Uses a "dial" metaphor for Galois groups. Covers the ENTIRE arc (field extensions -> Galois groups -> solvable groups -> quintic unsolvability) in 45 minutes. Deliberately skips tower law and degree of extension. Our video is the systematic treatment of ONE piece (solvability by radicals) that Mathemaniac covers in ~5 minutes.
2. **Aleph 0** -- "What is the square root of two?" (314K views). Uses sqrt(2) as a concrete hook, builds to FTGT in 25 minutes. Beautiful pink/magenta visuals, Manim-style animations. Skips solvability entirely.
3. **Math Visualized** -- "Galois Theory Explained Simply" (564K views). Uses "trousers" metaphor. Heavily simplified, does not reach solvability by radicals formally.
4. **University lecture channels** (Borcherds, Dr. Peyam, Salomone, Penn) -- all cover the theorem rigorously on whiteboard, 20-50 minutes, no animations.

**Market gap:** NO animated video provides a systematic treatment of solvability by radicals as a standalone topic with (a) the definition of radical extensions, (b) the theorem connecting solvable Galois groups to solvability by radicals, (c) a worked quartic example, AND (d) a teaser for quintic insolvability. Mathemaniac covers it all but glosses definitions. Lecturers cover definitions but no animation. We fill this gap.

**Our positioning:** The video where everything connects. This is the payoff for the entire Galois theory playlist. We explicitly reference Videos 218 (solvable groups) and 223 (FTGT) and show HOW they combine to answer the 300-year-old question: which polynomial equations can be solved by radicals?

**Techniques to adopt:**
- Mathemaniac's storytelling: each section raises a question the next section answers
- Mathemaniac's "dial" idea (but don't copy it -- use our own field tower visualization)
- Aleph 0's concrete example-first approach (quartic before the general theorem)
- The visual field tower: Q -> Q(sqrt(D)) -> Q(sqrt(D), sqrt(discriminant)) -> Q(all roots)

**Techniques to avoid:**
- Mathemaniac's 45-minute single-video approach (we focus on solvability by radicals only)
- Skipping the definition of radical extension (the gap we fill)
- Proving the full theorem (state it, prove the easy direction, sketch the hard direction)
- The "trousers" metaphor (unusual, may confuse)

## Scene Plan (8 scenes)

### Scene 1: Hook -- The 300-Year-Old Question (55s)
**Content budget:** intro animation + title + 4 progressive items
**Narration (~30s):** "For over 300 years, mathematicians sought a general formula to solve polynomial equations by radicals. Quadratics have the quadratic formula. Cubics have Cardano's formula. Quartics have Ferrari's formula. But quintics? No general formula exists. Today we connect this to Galois theory. The question 'which equations are solvable by radicals?' becomes 'which Galois groups are solvable?' And we already know the answer from Video 218."

- play_intro("Solvability by Radicals", "Advanced Abstract Algebra")
- Title: "The 300-Year-Old Question"
- 4 progressive items:
  1. "Quadratic, cubic, quartic formulas all use radicals (square roots, cube roots)"
  2. "Is there a general radical formula for degree 5 and above?"
  3. "Galois' insight: reformulate in terms of Galois groups"
  4. "Answer: exactly when the Galois group is solvable (Video 218)"

### Scene 2: Radical Extensions -- Definition (70s)
**Content budget:** section divider + title + definition + field tower visual
**Narration (~35s):** "What does it mean to solve a polynomial by radicals? It means the roots live in a field you can build by successively adjoining roots. Formally, a radical extension of F is an extension E over F where there exists a tower of fields F equals K sub zero, contained in K sub one, contained in K sub two, all the way up to K sub n equals E, where each step K sub i over K sub i minus one is obtained by adjoining an element alpha sub i such that alpha sub i to the power of m sub i lies in K sub i minus one, for some positive integer m sub i. In other words, each step adds a radical."

- Section divider: "1 -- Radical Extensions"
- Title: "Radical Extensions"
- Definition box: E/F is a radical extension if there exists a tower
- Visual: show the tower F = K_0 < K_1 < ... < K_n = E with radical adjunctions at each step
- Example: Q(sqrt(2), sqrt(3)) is a radical extension of Q (tower of two quadratic steps)

### Scene 3: Solvable by Radicals -- Definition (55s)
**Content budget:** title + definition + concrete example
**Narration (~28s):** "A polynomial f over F is solvable by radicals if its splitting field is contained in a radical extension of F. That's the definition. Let's check: x squared minus 2 over Q has splitting field Q of square root of 2, which IS a radical extension, so x squared minus 2 is solvable by radicals. For x cubed minus 2 over Q, the splitting field is Q of cube root of 2, omega, where omega is a primitive cube root of unity. This is a radical extension: first adjoin omega, then adjoin cube root of 2. So x cubed minus 2 is also solvable by radicals."

- Title: "When Is a Polynomial Solvable by Radicals?"
- Definition box: f is solvable by radicals if Split(f) is contained in a radical extension
- Worked example 1: x^2 - 2, splitting field Q(sqrt(2)), radical extension -> solvable
- Worked example 2: x^3 - 2, splitting field Q(cbrt(2), omega), radical extension -> solvable

### Scene 4: The Big Theorem (75s)
**Content budget:** section divider + title + theorem box + 3 parts
**Narration (~38s):** "Now the central theorem. A polynomial f with coefficients in a field F of characteristic zero is solvable by radicals if and only if the Galois group of its splitting field over F is a solvable group. This is the theorem that justifies the entire Galois theory program. The 'only if' direction says: if you can solve by radicals, the Galois group must be solvable. The 'if' direction says: if the Galois group is solvable, you CAN solve by radicals. This direction is harder to prove because you need to reverse-engineer the radical tower from the solvable group."

- Section divider: "2 -- The Central Theorem"
- Title: "Solvability by Radicals Theorem"
- Theorem box (formula_box, ACCENT): Gal(Split(f)/F) is solvable iff f is solvable by radicals
- 3 progressive parts:
  1. "Only if: radical extension -> solvable Galois group (easier)"
  2. "If: solvable Galois group -> radical extension (harder)"
  3. "Characteristic zero required (avoids inseparable complications)"

### Scene 5: Why Radical -> Solvable Group (80s)
**Content budget:** section divider + title + field tower + Galois group tower
**Narration (~40s):** "Let's see why the 'only if' direction works. Suppose E over F is a radical extension, so we have a tower F equals K zero contained in K one, all the way to K n equals E, where each step adjoins alpha i with alpha i to the m i in K i minus one. When we pass to the splitting field and take Galois groups, the Fundamental Theorem gives us a reverse tower of groups: Gal(E over K n) is trivial, contained in Gal(E over K n minus one), contained in, all the way up to Gal(E over F). Each quotient Gal(K i over K i minus one) is a cyclic group, because adjoining an m-th root in characteristic zero gives a cyclic Galois group. And a group with a tower of cyclic quotients is exactly a solvable group. This is the content of Video 218."

- Section divider: "3 -- Why Radical Implies Solvable"
- Title: "From Radical Extensions to Solvable Groups"
- Show field tower: K_0 < K_1 < ... < K_n (left side, PRIMARY)
- Show Galois group tower (inclusion-reversed, via FTGT): G_n < G_{n-1} < ... < G_0 (right side, SECONDARY)
- Key: each quotient G_{i-1}/G_i is cyclic
- Connection: "tower with cyclic quotients = solvable group (Video 218)"

### Scene 6: Quartic Example (85s)
**Content budget:** section divider + title + polynomial + Galois group + derived series
**Narration (~44s):** "Let's see a concrete example. Consider the polynomial x to the fourth minus 5 x squared plus 4, which factors as x squared minus 1 times x squared minus 4. Its roots are plus or minus 1 and plus or minus 2. The splitting field is just Q, since all roots are rational. The Galois group is trivial, which is trivially solvable. So the polynomial is solvable by radicals. For a less trivial example, consider x to the fourth minus 2. The roots are plus or minus fourth root of 2, and plus or minus i times fourth root of 2. The splitting field over Q has degree 8. The Galois group is the dihedral group D 4 of order 8. From Video 218, D 4 is solvable: its derived series is D 4, then V 4, then trivial. Since D 4 is solvable, x to the fourth minus 2 is solvable by radicals."

- Section divider: "4 -- Example: x^4 - 2"
- Title: "A Quartic Solvable by Radicals"
- Show: f(x) = x^4 - 2, roots: +-alpha, +-i*alpha where alpha = 2^{1/4}
- Show: Splitting field Q(2^{1/4}, i), degree 8
- Show: Galois group = D_4 (dihedral group of order 8)
- Show derived series: D_4 > V_4 > {e} (solvable!)
- Conclusion: x^4 - 2 is solvable by radicals

### Scene 7: Teaser -- The Quintic (65s)
**Content budget:** title + 2 key facts + teaser for next video
**Narration (~32s):** "Now the moment you've been waiting for. The symmetric group S 5, which is the Galois group of the general quintic polynomial, is NOT solvable. We saw in Video 218 that the derived series of S 5 is S 5, then A 5, then A 5 again. It never reaches the trivial group. So the general quintic is NOT solvable by radicals. This is Abel-Ruffini. But this is just the beginning of the story. The proof that S 5 is not solvable is beautiful, and there are specific quintics with smaller Galois groups that ARE solvable. We'll explore all of this in the next video."

- Title: "The Quintic: A Teaser"
- Show: S_5's derived series: S_5 > A_5 > A_5 > ... (never reaches {e})
- Highlight: "S_5 is NOT solvable (Video 218)"
- Show: "Therefore the general quintic is NOT solvable by radicals"
- Teaser: "Next video: the full proof + which quintics ARE solvable"

### Scene 8: Summary and Outro (50s)
**Content budget:** title + 5 takeaway items + outro
**Narration (~28s):** "Let's recap. A radical extension is built by successively adjoining roots. A polynomial is solvable by radicals if its splitting field lives inside a radical extension. The central theorem: solvable by radicals if and only if the Galois group is solvable. The proof uses the FTGT to convert a radical tower into a group tower with cyclic quotients, which is exactly a solvable group. And the quintic fails because S 5 is not solvable. This is Galois' immortal achievement."

- Section divider: "5 -- Summary"
- Title: "Key Takeaways"
- 5 progressive items:
  1. "Radical extension: built by successively adjoining n-th roots"
  2. "f solvable by radicals iff Split(f) contained in a radical extension"
  3. "THE THEOREM: f solvable by radicals iff Gal(Split(f)/F) is solvable"
  4. "Proof sketch: radical tower -> group tower with cyclic quotients (FTGT)"
  5. "The quintic: S_5 not solvable -> general quintic not solvable by radicals"
- play_outro("Insolvability of the Quintic", "Advanced Abstract Algebra")

## Visual Design Notes
- The field tower (Scene 2, 5) is a key recurring visual -- animate it building up step by step
- Scene 5's side-by-side field tower and group tower is the VISUAL CLIMAX
  - Field tower on LEFT in PRIMARY
  - Galois group tower on RIGHT in SECONDARY (inclusion-reversed, from FTGT)
  - Cyclic quotient labels in ACCENT between them
  - An arrow connecting the two towers: "FTGT"
- Scene 6 (quartic example) shows the derived series of D_4 visually
  - D_4 at top, V_4 in middle, {e} at bottom, each level in different colors
  - GREEN checkmark when it reaches {e} (solvable!)
- Scene 7 (quintic teaser) shows S_5's derived series FAILING to terminate
  - S_5 at top, A_5 in middle, A_5 repeats with RED X
  - This visual contrast (green checkmark vs red X) makes the point instantly
- The theorem box in Scene 4 is the content climax -- use ACCENT border, centered, prominent

## Thumbnail Concept
Dark BG (#1A1832) with a field tower on the left (Q -> Q(sqrt) -> ...) and a group tower on the right (S_n > ... > {e}) connected by a glowing FTGT arrow in the center. The theorem statement "Gal solvable iff f solvable by radicals" in ACCENT at the bottom. A RED X on S_5 in the corner as a teaser.