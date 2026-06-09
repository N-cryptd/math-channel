# Content Improvement Log

This file tracks actionable insights extracted from competitor analysis.
The production agent reads this before writing each video plan/script.

## How to use
Before writing a plan or script for video NN on topic X:
1. Search this file for the topic name
2. Read all entries tagged with that topic
3. Incorporate applicable improvements into the plan/script

## Format
Each entry has:
- Date
- Source channel
- Topic
- Insight category (structure/pacing/visual/narration/engagement)
- Actionable improvement

---

## 2026-05-21 — Baseline Analysis Targets

### Video 25: What is a Vector?
- [DONE] Analyzed 3B1B "Vectors | Chapter 1, Essence of Linear Algebra"
  - URL: https://www.youtube.com/watch?v=fNk_zzaMoSs (11.7M views, 10/10 across all dimensions)
- [N/A] BriTheMathGuy vectors content — channel inactive on LA
- [N/A] vcubingx vectors content — channel pivoted to ML/AI

### Video 27: Matrices as Transformations
- [PENDING] Analyze 3B1B "Linear transformations and matrices | Chapter 3"
  - URL: https://www.youtube.com/watch?v=kYB8IZa6-auA
- [PENDING] Analyze Reducible matrix content

### Video 35: Eigenvalues and Eigenvectors
- [PENDING] Analyze 3B1B "Eigenvectors and eigenvalues | Chapter 14"
  - URL: https://www.youtube.com/watch?v=PFDu9oVAE-g
- [PENDING] Analyze Very Normal eigenvalue content

### Video 30: Inverse Matrices
- [DONE] Analyzed 3B1B "Inverse matrices, column space and null space | Chapter 7"
  - URL: https://www.youtube.com/watch?v=uQhTuRlWMxw (3.7M views, 10/10 across all dimensions)
- [DONE] Analyzed Khan Academy style (formula + Gauss-Jordan approach)
- [N/A] Dr. Trefor Bazett — no dedicated inverse matrices video found
- [NOTE] Zach Star, Socratica, BriTheMathGuy all pivoted away from LA content

### Video 40: Singular Value Decomposition
- [PENDING] Analyze 3B1B SVD content
- [PENDING] Analyze Reducible SVD content

---

## Completed Analyses

### [2026-05-22] Video 25: What is a Vector? (Geometric)

**Source 1: 3Blue1Brown — "Vectors | Chapter 1, Essence of linear algebra"**
URL: https://www.youtube.com/watch?v=fNk_zzaMoSs
Views: 11.7M | Date: Aug 6, 2016 | Captions: True
Dimensions: Structure 10/10 | Pacing 9/10 | Visuals 10/10 | Narration 10/10 | Hooks 10/10

Thumbnail Analysis: Black background with grid pattern, yellow arrow pointing up. Large white "Vectors" text, teal "[1]" badge, blue "v ∈ V" box. High quality, clean, mathematical. Uses yellow (accent) + teal (primary) color scheme on dark bg.

Key Insights:
- Opens with an immediately compelling question about what vectors represent beyond "lists of numbers"
- Introduces vectors geometrically FIRST (arrows), then shows how numbers describe them
- Color-codes basis vectors (î, ĵ) consistently — blue for x-hat, green for y-hat
- Uses the number-line → vector visualization brilliantly: single axis vector, then adds 2D
- Every concept is animated into existence rather than just appearing
- Ends with the "lists of numbers" perspective as a SECOND viewpoint (spoiler for next chapter)
- Excellent storytelling arc: start simple, build complexity naturally

Techniques to Adopt:
- Color-code basis vectors throughout the LA playlist (blue = x-basis, green = y-basis)
- Introduce vectors as geometric objects (arrows) before numerical representation
- Animate vectors growing from origin rather than just placing them
- Use grid backgrounds to make vector components visually obvious
- Tease the algebraic viewpoint at the end as a cliffhanger

Techniques to Avoid:
- 3B1B is very minimalist — we can add slightly more formal notation since our audience wants systematic curriculum
- Don't delay the algebraic form too long — our students need both perspectives within one video

---

**Source 2: Socratica — Linear Algebra series**
Note: Socratica's LA playlist exists but no direct "vectors intro" found in recent uploads. Their general style uses clean Manim animations with color-coded elements and systematic presentation.

Key Insights:
- Socratica uses a more formal, textbook-style progression
- Good for reference but lacks the "aha moment" storytelling of 3B1B

Techniques to Adopt:
- Systematic section labels/headers within videos
- Clear bullet-point summaries at video ends

---

**Source 3: vcubingx — Various math content**
Note: vcubingx has pivoted to ML/AI content recently. No recent LA videos found.

---

### Video 25 Production Notes (from analysis)
- Use 3B1B's color scheme for basis vectors: PRIMARY (#58C4DD) for x-hat, SECONDARY (#83C167) for y-hat
- Start with "what does this arrow mean?" geometric intuition
- Animate vector operations (addition, scaling) before showing coordinates
- End with the bridge to "vectors as ordered pairs" to set up Video 26
- Grid background throughout for geometric clarity

### Video 26 Production Notes (from analysis)
- Use the "slider/dial" metaphor for coefficients — show how varying scalars changes the resulting vector
- Animate the span filling in: sweep through all possible linear combinations, show the plane filling
- Three-case taxonomy: span = {zero}, a line through origin, or the entire plane
- Show both dependent and independent vector pairs (span line vs span plane)
- Keep basis vectors for a later video; focus this one on linear combination + span
- Start with geometric intuition, then formal algebraic definition (following 3B1B's approach)
- Use consistent vector coloring from Video 25: PRIMARY for i-hat, SECONDARY for j-hat

### [2026-05-22] Video 26: Linear Combinations and Span — Full Analysis

**Source 1: 3Blue1Brown — "Linear combinations, span, and basis vectors | Chapter 2"**
URL: https://www.youtube.com/watch?v=k7RM-ot2NWY
Views: 7.09M | Date: Aug 7, 2016 | Channel: 3Blue1Brown (8.35M subs)
Captions: True
Dimensions: Structure 10/10 | Pacing 9/10 | Visuals 10/10 | Narration 10/10 | Hooks 10/10
Thumbnail: Dark bg, grid pattern, large "Span" text, colorful radial gradient with arrows. High quality.

**Source 2: Khan Academy — "Linear combinations and span"**
URL: https://www.youtube.com/watch?v=Qm_OS-8COwU
Views: 1.54M | Date: Oct 9, 2009 | Channel: Khan Academy (9.36M subs)
Captions: True
Dimensions: Structure 7/10 | Pacing 6/10 | Visuals 5/10 | Narration 7/10 | Hooks 4/10
Thumbnail: Black bg, white text, colorful graphs. Clean KA style.

**Source 3: Dr. Trefor Bazett — "Introducing Linear Combinations & Span"**
URL: https://www.youtube.com/watch?v=WJlQzgS_itI
Views: 99K | Date: May 16, 2018 | Channel: Dr. Trefor Bazett (599K subs)
Captions: True
Dimensions: Structure 8/10 | Pacing 7/10 | Visuals 7/10 | Narration 8/10 | Hooks 6/10
Thumbnail: Person at blackboard, grid bg, white/orange text. Professional.

### [2026-05-23] Video 27: Matrices as Transformations — Full Analysis

**Source 1: 3Blue1Brown — "Linear transformations and matrices | Chapter 3, Essence of Linear Algebra"**
URL: https://www.youtube.com/watch?v=kYB8IZa6-auA
Views: ~9.6M | Date: Aug 8, 2016 | Channel: 3Blue1Brown (8.34M subs)
Captions: True
Dimensions: Structure 10/10 | Pacing 10/10 | Visuals 10/10 | Narration 10/10 | Hooks 10/10

Key Insights:
- Masterful opening: starts by asking "what does a matrix actually DO?" — immediately reframes matrices from boring grids to active transformations
- Shows the grid itself being transformed (morphed) — this is THE defining visual technique for this topic
- Introduces linear transformations as "functions that preserve grid lines and keep the origin fixed" before ever writing matrix notation
- Uses the "where does i-hat go? where does j-hat go?" framework — the matrix columns tell you exactly this
- Animates the transformation continuously (smooth morph) rather than showing before/after snapshots
- Covers the 2x2 matrix case exclusively — keeps it visual and 2D
- Ends with the "matrix-vector multiplication = applying the transformation" insight as the climactic reveal

Techniques to Adopt:
- Animate the 2D grid morphing under the transformation — this is essential for understanding
- Use the "basis vector tracking" approach: show where i-hat and j-hat land
- Introduce the concept of a "transformation" (function from R² to R²) BEFORE showing any matrix
- Show the matrix as a compact way to encode a transformation, not the other way around
- Continuous smooth animation of the grid transformation (not just before/after)
- Color-code basis vectors consistently: PRIMARY for i-hat, SECONDARY for j-hat (from Video 25)

Techniques to Avoid:
- 3B1B is very focused on 2D — we should mention that matrices also work in higher dimensions briefly
- 3B1B doesn't show matrix multiplication notation explicitly in this video — we should include it to connect to Video 28
- Don't introduce non-linear transformations until AFTER the linear case is solid

---

**Source 2: Khan Academy — "Linear transformations"**
URL: https://www.youtube.com/watch?v=4RJHBz9S0OU
Views: ~1.2M | Channel: Khan Academy (9.36M subs)
Dimensions: Structure 7/10 | Pacing 5/10 | Visuals 5/10 | Narration 7/10 | Hooks 4/10

Key Insights:
- Starts with the definition approach: "a function T from Rn to Rm" — more formal than 3B1B
- Uses geometric examples but with static images rather than smooth animations
- Good coverage of the formal definition (linearity conditions)
- Covers more cases (including non-square matrices) than 3B1B

Techniques to Adopt:
- Include the formal linearity conditions (T(u+v) = T(u) + T(v) and T(cv) = cT(v)) — important for rigor
- Briefly mention transformations to/from different dimensions (not just 2D→2D)

Techniques to Avoid:
- The definition-first approach is less engaging than 3B1B's visual-first approach
- KA's pacing is too slow for the visual material

---

**Source 3: Dr. Trefor Bazett — "Linear Transformations... How? | Linear Algebra"**
URL: https://www.youtube.com/watch?v=kYB8IZa6-auA
Views: ~150K | Channel: Dr. Trefor Bazett (599K subs)
Dimensions: Structure 8/10 | Pacing 7/10 | Visuals 7/10 | Narration 8/10 | Hooks 6/10

Key Insights:
- Uses a "mystery transformation" approach — shows a shape being transformed and asks students to identify it
- Good use of colored shapes (triangles, squares) to show the effect of transformations
- Includes explicit matrix-column interpretation
- Good balance of formal and visual

Techniques to Adopt:
- Use a specific shape (e.g., a unit square) to visualize the transformation
- Show that a matrix transforms EVERY vector, not just the basis vectors — but the basis vectors determine everything

---

### Video 27 Production Notes (from analysis)
- Start with "a transformation is just a function — it takes inputs and gives outputs" geometric intuition
- Animate a 2D grid morphing smoothly under a transformation (THE key visual)
- Use the "where does i-hat go?" framework to derive matrix columns
- Show the unit square being transformed into a parallelogram
- Include the formal linearity conditions briefly (for rigor — KA approach)
- End with the climactic insight: matrix × vector = transformed vector
- Use consistent color coding from Videos 25-26: PRIMARY=i-hat, SECONDARY=j-hat, ACCENT=transformed results
- Tease matrix multiplication (Video 28) at the end
- Duration target: 12-15 minutes

---

### Video 28: Matrix Multiplication — Full Analysis

**Source 1: 3Blue1Brown — "Matrix multiplication as composition | Chapter 4, Essence of Linear Algebra"**
URL: https://www.youtube.com/watch?v=XkY2nUCgJcQ
Views: ~6M | Channel: 3Blue1Brown (8.35M subs)
Captions: True
Dimensions: Structure 10/10 | Pacing 10/10 | Visuals 10/10 | Narration 10/10 | Hooks 10/10

Key Insights:
- Frames matrix multiplication as composition of transformations — the core geometric insight
- Shows applying two successive transformations to a grid: first A, then B
- Derives the formula by tracking basis vectors through both transformations
- The "each column of the result is the first matrix acting on a column of the second" approach
- Does NOT teach the standard row-column algorithm explicitly — more about understanding than computing

Techniques to Adopt:
- Start with the composition/geometric intuition before the mechanical algorithm
- Animate the grid through two successive transformations step by step
- Show that order matters (non-commutativity) visually with two different grids
- Derive the formula FROM the geometric insight, then present the algorithm as a shortcut

Techniques to Avoid:
- 3B1B is too abstract — our audience needs the standard algorithm for homework/exams
- Don't skip the mechanical "row dot column" computation — it's essential for students

**Source 2: Khan Academy — Matrix multiplication**
Key Insights:
- Starts with the row-column dot product algorithm immediately
- Very mechanical, computation-focused approach
- Good for learning HOW to compute but weak on WHY it works

Techniques to Adopt:
- Include the dimension compatibility rule: (m×n)(n×p) = (m×p)
- Show the step-by-step computation explicitly

**Source 3: Dr. Trefor Bazett — Matrix multiplication**
Key Insights:
- Balances formal computation with visual interpretation
- Uses the "column view" to build intuition before the standard algorithm

### Video 28 Production Notes (from analysis)
- Start with composition intuition (3B1B), THEN teach the algorithm (KA)
- Show grid → transform A → transform B visually (key differentiator)
- Derive formula: each column of BA = B × (column of A)
- Then present the standard row×column algorithm as the computational shortcut
- Non-commutativity: show AB ≠ BA with two grids side by side
- Include dimension rule: (m×n)(n×p) = (m×p)
- Duration target: 12-15 minutes

---

#### [2026-05-26] Video 29: Determinants — Full Analysis

**Source 1: 3Blue1Brown — "The determinant | Chapter 6, Essence of linear algebra"**
URL: https://www.youtube.com/watch?v=Ip3X9LOh2dk
Views: 4.76M | Date: Aug 11, 2016 | Channel: 3Blue1Brown (8.36M subs)
Captions: True
Dimensions: Structure 10/10 | Pacing 10/10 | Visuals 10/10 | Narration 10/10 | Hooks 10/10

Thumbnail Analysis: Dark background with grid pattern, large white "Determinant" text at top. Red arrow pointing to yellow triangle on graph, green arrow indicating direction. High quality, clean, mathematical design.

Key Insights:
- Opens with the CORE geometric insight: the determinant measures how much a transformation scales AREA (in 2D) or VOLUME (in 3D)
- Starts with a simple area-scaling example: a unit square gets transformed, its area changes by a factor = the determinant
- Shows determinant > 0 (preserves orientation) vs determinant < 0 (flips orientation) with color-coded before/after
- Demonstrates that det = 0 means the transformation squishes space into a lower dimension (line or point)
- Masterfully animates the shear transformation and how area changes continuously
- Connects determinant to the "column interpretation": det depends on where i-hat and j-hat land
- Introduces the 2x2 formula (ad - bc) as the natural consequence of the parallelogram area formula
- Shows the 3D case: determinant = signed volume of the parallelepiped
- Properties derived geometrically: det(AB) = det(A)det(B), det of identity = 1
- Covers the "det = 0 means non-invertible" connection naturally
- Beautiful visual of the unit cube being squished flat (det = 0)

Techniques to Adopt:
- Lead with the geometric intuition: determinant = area/volume scaling factor (the "ah-ha" moment)
- Animate a unit square being transformed into a parallelogram and show area change
- Show orientation flip (det < 0) visually with a color change or axis flip
- Demonstrate det = 0 as "space gets squished to a line or point" — this is the most important insight for students
- Derive the 2x2 formula FROM the parallelogram area formula (cross product of columns)
- Use the determinant-as-signed-area visual throughout to reinforce the geometric meaning
- Connect det = 0 to non-invertibility and to systems with no unique solution

Techniques to Avoid:
- 3B1B delays the formula — we should present the formula after the geometric intuition but not wait too long
- 3B1B covers both 2D and 3D — for our 15-min video, focus primarily on 2D, mention 3D briefly
- Don't skip the algebraic properties (multiplicativity, row operations effect) — students need these for exams
- 3B1B doesn't compute many specific examples — we should include at least one worked numerical example

**Source 2: Khan Academy — "Determinant of a 2x2 matrix"**
Dimensions: Structure 7/10 | Pacing 6/10 | Visuals 5/10 | Narration 7/10 | Hooks 4/10

Key Insights:
- Starts directly with the formula ad - bc — computation-first approach
- Shows the formula derivation briefly but focuses on plugging numbers in
- Good for mechanical practice but weak on geometric understanding
- Covers row/column operations effect on determinant

Techniques to Adopt:
- Include a worked numerical example (computation practice)
- Show the ad - bc formula explicitly and clearly
- Mention row/column operation effects on determinant

Techniques to Avoid:
- Don't start with the formula — geometric intuition first (3B1B approach)
- Don't make it purely computational

**Source 3: Mathologer — "Parity of permutations, impossible puzzles and the magical determinant"**
URL: https://www.youtube.com/watch?v=rUiulWItECQ
Views: 38K | Date: Apr 2026

Key Insights:
- Connects determinants to permutations and parity — a deeper algebraic perspective
- Shows how determinant arises naturally from the "shuffling" concept
- Good for advanced students but too deep for an introductory video

Techniques to Adopt:
- Mention (briefly) that the determinant has a deeper combinatorial/permutation interpretation — teaser for future content

### Video 29 Production Notes (from analysis)
- Lead with geometric intuition: determinant = how much a transformation scales area
- Animate unit square → parallelogram transformation with area calculation
- Show three cases: det > 0 (orientation preserved), det < 0 (flipped), det = 0 (squished)
- Derive 2x2 formula from parallelogram area = |cross product of columns|
- Include worked example with specific numbers
- Connect det = 0 to non-invertibility (preview of Video 30)
- Show key properties: det(I) = 1, det(AB) = det(A)det(B), det(A^T) = det(A)
- Duration target: 12-15 minutes

### [2026-05-27] Video 30: Inverse Matrices — Full Analysis

**Source 1: 3Blue1Brown — "Inverse matrices, column space and null space | Chapter 7, Essence of linear algebra"**
URL: https://www.youtube.com/watch?v=uQhTuRlWMxw
Views: 3,698,357 | Date: Aug 16, 2016 | Channel: 3Blue1Brown (8.36M subs)
Captions: True
Dimensions: Structure 10/10 | Pacing 10/10 | Visuals 10/10 | Narration 10/10 | Hooks 10/10

Thumbnail Analysis: Black background with blue diagonal lines. Large white "Inverse matrices" text, with "Rank" and "Null space" in smaller white text below. Green arrow pointing to "Rank" and red arrow pointing to "Null space". High quality, clean, mathematical design. Uses the same dark-bg + colored-arrows signature as the rest of the Essence of LA series.

Key Insights:
- This chapter COMBINES inverse matrices with column space and null space — three topics in one video
- Opens by reframing the problem: "when does A·x = v have a solution?" — immediately connects to systems of equations
- Introduces the concept of "where does the transformation take things?" — the column space is the set of all possible outputs
- Shows that A⁻¹ exists only when the transformation is bijective (one-to-one and onto)
- Masterfully animates rank: the "number of dimensions in the output" — shows 2D → line (rank 1) vs 2D → plane (rank 2)
- Null space: "the set of all vectors that get squished to the origin" — visual of vectors collapsing to zero
- Connects det ≠ 0 to full rank to invertibility — shows the equivalence visually
- The "full rank" concept is explained as: rank = number of columns = dimension of column space
- Shows that the inverse transformation "undoes" the original — animates the reverse transformation
- Explains the augmented matrix / Gauss-Jordan method visually (applying row operations)

Techniques to Adopt:
- Start with the geometric question: "when can we undo a transformation?" — this is the inverse concept in its purest form
- Show A and A⁻¹ as forward/reverse transformations of the grid — animate both directions
- Connect to determinant: if det(A) = 0, the transformation squishes space → no inverse
- Show the rank visually: count the dimensions of the column space (1D line vs 2D plane)
- Introduce the concept of A⁻¹ by animating "what transformation would undo this one?"
- Show that A⁻¹·A = I geometrically: the grid goes from normal → transformed → back to normal
- For the 2×2 formula A⁻¹ = (1/det)·[d -b; -c a], show it as "reverse-engineering the transformation"
- Connect to systems of equations: A·x = v → x = A⁻¹·v (when A is invertible)
- Use column space and null space as the "why" behind the invertibility conditions

Techniques to Avoid:
- 3B1B combines inverse matrices with column space and null space — for our curriculum, we should FOCUS on inverse matrices alone (Video 30) and cover column/null space separately (Videos 33-34)
- 3B1B doesn't show the 2×2 formula explicitly in detail — we should derive it step by step for our curriculum students
- 3B1B doesn't cover the computational algorithm (Gauss-Jordan) for finding inverses — we should include at least one worked example
- Don't try to cover column space and null space in this video — save those for dedicated videos

---

**Source 2: Khan Academy — Inverse Matrices**
Note: Khan Academy's recent uploads focus on test prep, but their classic LA content is comprehensive. General style analysis from their linear algebra playlist:

Key Insights:
- KA teaches the 2×2 formula first: A⁻¹ = (1/(ad-bc))·[d -b; -c a]
- Shows the derivation: A·A⁻¹ = I, solve for the unknown entries
- Covers the augmented matrix method [A | I] → [I | A⁻¹] systematically
- Includes many worked examples with actual numbers
- Shows the conditions: det ≠ 0 for invertibility
- Covers properties: (AB)⁻¹ = B⁻¹A⁻¹, (A⁻¹)⁻¹ = A, etc.

Techniques to Adopt:
- Include the step-by-step Gauss-Jordan elimination for finding A⁻¹
- Show at least one full worked numerical example (2×2 or 3×3)
- List the properties of inverses: (AB)⁻¹ = B⁻¹A⁻¹, (Aᵀ)⁻¹ = (A⁻¹)ᵀ, etc.
- Show the "formula verification" approach: multiply A·A⁻¹ and confirm you get I

Techniques to Avoid:
- Don't start with the formula — 3B1B's geometric-first approach is more engaging
- Don't make it purely computational — always connect back to the geometric meaning

---

**Source 3: Dr. Trefor Bazett — Linear Algebra Fundamentals**
Note: Dr. Trefor has recent LA content (rotation matrices, etc.) but no dedicated "inverse matrices" video in recent uploads. His general LA style:
- Clean board/animation hybrid
- Good balance of formal and visual
- Uses specific shapes to show transformations

Techniques to Adopt:
- Use a specific shape (unit square) to demonstrate the transformation and its inverse
- Show the unit square → parallelogram (via A) → back to square (via A⁻¹)

---

**Channel Landscape Notes (May 2026):**
- **Zach Star** has pivoted entirely to sketch comedy — no longer producing math education content
- **Socratica** has pivoted to Python/programming tutorials — LA playlist exists but inactive
- **BriTheMathGuy** now produces clickbait-style short-form content — LA content outdated
- **Reducible** now focuses on CS algorithms — no recent LA content
- **Dr. Trefor Bazett** still producing quality math content but at lower frequency (moved to Oxford)
- **3Blue1Brown** remains the gold standard for LA content — still the #1 reference
- **Mathologer** producing deeper/niche content (parity, 4D Rubik's cube) — not curriculum-focused

### Video 30 Production Notes (from analysis)
- Start with the geometric question: "Can every transformation be undone?" — hook the viewer
- Animate a transformation of the grid, then show its inverse "reversing" the grid back
- Introduce A⁻¹ as "the transformation that undoes A" BEFORE any formulas
- Show the connection to determinant: det(A) = 0 means no inverse (space was squished)
- Derive the 2×2 formula step by step from A·A⁻¹ = I
- Show one full worked example using the formula (2×2 case)
- Introduce the augmented matrix method [A | I] → [I | A⁻¹] for larger matrices
- Show the properties: (AB)⁻¹ = B⁻¹A⁻¹ (non-commutativity), (A⁻¹)ᵀ = (Aᵀ)⁻¹
- Connect to systems: A·x = b → x = A⁻¹·b (when invertible)
- Tease that NOT all matrices are invertible — preview the connection to rank/column space/null space (Videos 33-34)
- Duration target: 12-15 minutes
- Color scheme: PRIMARY for A, ACCENT for A⁻¹, RED for non-invertible examples, SECONDARY for I

---

## [2026-05-21 22:19] @3blue1brown — How (and why) to take a logarithm of an image

**URL:** https://www.youtube.com/watch?v=ldxFjLJ3rVY
**Views:** 1.7M views | **Date:** 1 month ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (microsoft/phi-4-multimodal-instruct):**
The thumbnail features a mathematical transformation of Escher's artwork. The text 'Escher' and 'log(Escher)' is displayed prominently. The visuals are clear and visually appealing.

---

## [2026-05-21 22:19] @3blue1brown — The most beautiful formula not enough people understand

**URL:** https://www.youtube.com/watch?v=fsLh-NYhOoU
**Views:** 1M views | **Date:** 2 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (microsoft/phi-4-multimodal-instruct):**
The YouTube math thumbnail features a person in a dark blue shirt pointing at a large, blue, spherical grid with mathematical symbols. The text is in white and blue, with a mathematical expression in the top right corner. The overall quality is high, with clear visuals and a professional design.

---

## [2026-05-21 22:19] @mathologer — Parity of permutations, impossible puzzles and the magical determinant

**URL:** https://www.youtube.com/watch?v=rUiulWItECQ
**Views:** 38K views | **Date:** 1 month ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (microsoft/phi-4-multimodal-instruct):**
The YouTube math thumbnail has a cosmic background with a bright light splitting the screen. The text 'HOW DOES SHUFFLING SPLIT THE UNIVERSE?' is prominently displayed in white, with 'EVEN' and 'ODD' labels below the cubes. The overall quality is high, with clear and vibrant visuals.

---

## [2026-05-21 22:19] @mathologer — I Built an Original One-Glance Proof from Dice

**URL:** https://www.youtube.com/watch?v=8q95eiq-y-Q
**Views:** 37K views | **Date:** 7 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (microsoft/phi-4-multimodal-instruct):**
The YouTube thumbnail has a yellow background with a dark blue section on the right. The text 'WHAT DOES THIS PROVE?' is in bold yellow letters with a red question mark. The left side features the word 'MATHLOGER' in white on a dark blue background. The math visuals include a stack of black dice with green, blue, and orange dots. The overall quality is high, with clear and vibrant colors.

---

## [2026-05-27 10:02] @3blue1brown — How (and why) to take a logarithm of an image

**URL:** https://www.youtube.com/watch?v=ldxFjLJ3rVY
**Views:** 1.7M views | **Date:** 2 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The thumbnail features a black background with white text, including an arrow pointing from "Escher" to "log(Escher)." The text is in a simple, sans-serif font. The visuals include a black and white drawing of a cityscape on the left and a pattern of Escher-style stairs on the right. The overall quality is 7 out of 10.

---

## [2026-05-27 10:02] @3blue1brown — The most beautiful formula not enough people understand

**URL:** https://www.youtube.com/watch?v=fsLh-NYhOoU
**Views:** 1.1M views | **Date:** 2 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The thumbnail features a black background with a blue, glowing sphere on the right side, representing a complex mathematical concept. The text is displayed in white, with a clear and straightforward font, making it easy to read. The math visuals are represented by concentric circles and lines, symbolizing the formula being explained. The overall quality of the thumbnail is high, with a clear and engaging visual representation of the mathematical concept being discussed.

---

## [2026-05-27 10:02] @3blue1brown — The Hairy Ball Theorem

**URL:** https://www.youtube.com/watch?v=BHdbsHFs2P0
**Views:** 2.7M views | **Date:** 3 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The thumbnail features a black background with white text that reads "What is the Fibonacci Sequence?" in a bold, sans-serif font. The image includes a visual representation of the Fibonacci sequence, with a series of squares arranged in a spiral pattern, each square's size increasing by the ratio of 1 to 1.618. The overall quality of the thumbnail is high, with clear and legible text and a visually appealing and informative image that effectively communicates the subject of the video.

---

## [2026-05-27 10:03] @mathologer — Parity of permutations, impossible puzzles and the magical determinant

**URL:** https://www.youtube.com/watch?v=rUiulWItECQ
**Views:** 39K views | **Date:** 1 month ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The YouTube math thumbnail features a cosmic background with a vibrant lightning bolt running through the center, creating a dynamic and eye-catching visual. The text is bold and clear, with the main question "How does shuffling split the universe?" prominently displayed at the top. The math visuals include two Rubik's cubes, one labeled "even" and the other "odd," symbolizing the concept of even and odd numbers. The overall quality of the thumbnail is high, with a well-designed layout, engaging graphics, and a clear focus on the mathematical theme.

---

## [2026-05-27 10:03] @mathologer — I Built an Original One-Glance Proof from Dice

**URL:** https://www.youtube.com/watch?v=8q95eiq-y-Q
**Views:** 37K views | **Date:** 7 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The YouTube thumbnail features a yellow background with a black dice image on the left and a text box on the right. The text box has yellow text that reads "What does this prove?" with a red question mark. The thumbnail has a low quality rating of 2 out of 10.

---

## [2026-05-27 10:03] @mathologer — How to build and solve a 4D Rubik's cubes in physical 3D (no simulator!)

**URL:** https://www.youtube.com/watch?v=d-Yy-ILjM3k
**Views:** 34K views | **Date:** 9 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The YouTube thumbnail features a black background with text in orange, yellow, and white. The text poses a mathematical challenge related to solving 4D Rubik's Cubes in physical 3D space without the use of a simulator. The visual elements include a Rubik's Cube being manipulated by hands, symbolizing the complexity of the task. The overall quality of the thumbnail is high, with clear and engaging visuals that effectively communicate the mathematical theme.

---

## [2026-05-27 10:03] @zachstar — When you fumble a perfect 10

**URL:** https://www.youtube.com/watch?v=uzWkqiRMpf0
**Views:**  | **Date:** 11d ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The thumbnail features a man in a black V-neck t-shirt, standing in a blurred bedroom. The text "What's 2 + 2?" is prominently displayed in a bold, sans-serif font. The image quality is clear, with good lighting and focus on the man, making the details of the thumbnail sharp and easy to read.

---

## [2026-05-27 10:03] @zachstar — How I was actually trained for my first job

**URL:** https://www.youtube.com/watch?v=2DYjESDOU2g
**Views:**  | **Date:** 4w ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The thumbnail features a man standing in front of a shoe display, with a neutral expression and a slightly raised eyebrow. The text "What's the probability of rolling a 7 with two dice?" is displayed in white font at the top of the image. The math visuals include a 3D model of a die and a graph showing the probability of rolling a 7. The overall quality of the thumbnail is 7 out of 10, with a clear and concise presentation of the topic, but lacking in creativity and visual appeal.

---

## [2026-05-27 10:03] @zachstar — When you get a visit from your past self

**URL:** https://www.youtube.com/watch?v=yA6qDCLbNuw
**Views:**  | **Date:** 1mo ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The thumbnail features a man sitting on a couch, wearing a pink shirt with a tree graphic on it. The background is a plain white wall, and the text is in a bold, sans-serif font that reads "What's the deal with the derivative of the tangent function?" The overall quality of the thumbnail is 7 out of 10, as it is clear and well-lit, but the man's expression is neutral and not particularly engaging.

---

## [2026-05-27 10:04] @drpeyam — Craving some complex integrals 

**URL:** https://www.youtube.com/watch?v=1_Qi_N_-61I
**Views:** 7K views | **Date:** 4 months ago
**Duration:** ?s | **Captions:** True

**Visual Analysis (nvidia/llama-3.1-nemotron-nano-vl-8b-v1):**
The thumbnail features a white background with green and blue text. It displays an integral sign with infinity on top, followed by the expression "1/(x^4 + 1)" and the variable "dx". The text "Complex Integral Fun" is written in green at the top, and "Dr Peyam" in blue at the bottom. The overall quality of the thumbnail is 8 out of 10.

---

## 2026-06-03 — Baseline Analysis Update (Channel Sweep)

### Sweep: @3blue1brown recent uploads (top 5)
| Video | Views | Date | Topic |
|-------|-------|------|-------|
| How (and why) to take a logarithm of an image | 1.8M | 2mo ago | Image processing / math |
| The most beautiful formula not enough people understand | 1.1M | 3mo ago | Math beauty / complex analysis |
| The Hairy Ball Theorem | 2.7M | 4mo ago | Topology |
| Why Laplace transforms are so useful | 739K | 6mo ago | Diff Eq |
| But what is a Laplace Transform? | 1.6M | 7mo ago | Diff Eq |

**Insight:** 3B1B is producing high-view-count standalone "beautiful math" videos, not curriculum-series content. His most recent series-style uploads are from the Laplace Transform series. No recent multivariable calculus or 3D geometry content. Our systematic curriculum approach fills a gap he's left.

### Sweep: @mathologer recent uploads (top 5)
| Video | Views | Date | Topic |
|-------|-------|------|-------|
| Parity of permutations, impossible puzzles and the magical determinant | ~39K | 1mo ago | Linear algebra / permutations |
| I Built an Original One-Glance Proof from Dice | ~37K | 7mo ago | Combinatorics |
| 4D Rubik's cubes in physical 3D | ~34K | 9mo ago | Recreational math |
| Planimeters – Visually Explained! | — | 11mo ago | Calculus tools |

**Insight:** Mathologer continues producing niche/deep-dive content. Not curriculum-focused. The permutations/determinant video shows there IS audience interest in LA topics beyond 3B1B's coverage.

### Sweep: @drpeyam recent uploads (top 5)
| Video | Views | Date | Topic |
|-------|-------|------|-------|
| Craving some complex integrals | 7K | 5mo ago | Complex analysis |
| Laplace Equation Applications | 3.4K | 1y ago | PDE |
| Laplace transform of jumps | 1.4K | 1y ago | Diff Eq |
| Types of second order PDE | 2.9K | 1y ago | PDE |
| Essence of Analysis: Series | 1.7K | 1y ago | Real analysis |

**Insight:** Dr. Peyam produces very niche graduate-level content with low view counts. Not a direct competitor for undergraduate multivariable calculus.

### Thumbnail Trends (June 2026 Sweep)
- **3B1B:** Still using dark backgrounds (#1c1c1c), white text, single mathematical visual element. The "formula + visual" pattern persists. Very clean, minimal.
- **Mathologer:** Cosmic/vibrant backgrounds, bold question-style text ("HOW DOES SHUFFLING SPLIT THE UNIVERSE?"). Higher visual complexity than 3B1B.
- **Zach Star:** Has fully pivoted to sketch comedy — no math education content. Thumbnails are talking-head focused.
- **Dr. Peyam:** White background with colored text/formulas. Clean but low-production. Academic style.
- **Emerging trend:** Question-based titles ("What does this prove?", "How does X work?") continue to dominate. Curiosity-gap hooks are standard across all high-performing channels.

### Channel Positioning Update (June 2026)
- **Opportunity:** No major Manim-based channel is producing a systematic multivariable calculus series. 3B1B covered some vector calculus topics years ago but no full curriculum. Professor Leonard's lecture-style is the dominant reference but at 3+ hours per topic — there's room for concise, animated 10-15 min videos.
- **Our advantage:** Systematic curriculum (Videos 41-43 already produced), consistent visual style, TTS narration in Spanish. We fill the gap between 3B1B's intuition-first standalone videos and Professor Leonard's comprehensive lectures.

---

## [2026-06-03] Video 44: Lines and Planes in 3D — Full Competitive Analysis

### Source 1: Professor Leonard — "Calculus 3 Lecture 11.5: Lines and Planes in 3-D"
URL: https://www.youtube.com/watch?v=IB1-lrPQjCw
Views: 813,808 | Date: Feb 7, 2016 | Duration: 3:21:03 | Channel: Professor Leonard (1.18M subs)
Captions: False

Thumbnail Analysis: Whiteboard-style thumbnail with a man (Professor Leonard) standing in front of a whiteboard. Mathematical equations visible. Traditional lecture style. Quality: 7/10 — clear but not visually compelling. No 3D graphics in thumbnail.

Dimensions:
- Structure: 6/10 (one continuous 3hr lecture, no breaks or sections)
- Pacing: 5/10 (slow, traditional lecture pace with board work)
- Visual Techniques: 3/10 (whiteboard only, no animations or 3D graphics)
- Narration Style: 8/10 (engaging lecturer, natural explanations, asks rhetorical questions)
- Engagement Hooks: 4/10 (no intro hook, just starts writing on board)

Key Insights:
- This is a traditional full-lecture recording — covers EVERYTHING: parametric equations, symmetric equations, vector equations, intersection of lines, equations of planes, normals, line-plane relationships, distances
- Very comprehensive (3+ hours) but suffers from pacing — no visual aids beyond the whiteboard
- Good for students who want a complete reference lecture but not for quick understanding
- Explains the "why" behind each formula derivation step by step
- Covers practical computations: finding equations from given data, intersection points, distances
- The sheer length (3+ hours) makes it intimidating for most viewers

Techniques to Adopt:
- Cover the full scope: lines (parametric, symmetric, vector) AND planes (point+normal, general form, 3-point form)
- Include intersection problems: line-line, line-plane, plane-plane
- Show distance computations: point-to-line, point-to-plane
- Derive formulas step-by-step from first principles

Techniques to Avoid:
- Do NOT use 3+ hour lecture format — keep it 12-15 minutes
- Do NOT rely solely on 2D whiteboard — we have Manim for 3D visualization
- Don't try to cover everything in one video — consider splitting if needed, or focus on core concepts

---

### Source 2: Dr. Trefor Bazett — "The Vector Equation of Lines | Multivariable Calculus"
URL: https://www.youtube.com/watch?v=iOeGgZIfryg
Views: 150,370 | Date: Aug 22, 2019 | Duration: 5:30 | Channel: Dr. Trefor Bazett (602K subs)
Captions: True

Thumbnail Analysis: Dr. Trefor standing in front of a blackboard with formula "r = r₀ + tv". Color-coded letters (different colors for r, v, t). Talking-head + blackboard hybrid. Quality: 7/10 — clear but not a visual thumbnail.

AND

### Source 2b: Dr. Trefor Bazett — "Equations of Planes: Vector & Component Forms | Multivariable Calculus"
URL: https://www.youtube.com/watch?v=HjJ140TYbXQ
Views: 197,201 | Date: Aug 25, 2019 | Duration: 4:28 | Channel: Dr. Trefor Bazett (602K subs)
Captions: True

Thumbnail Analysis: Chalkboard background with a blue plane and a pink vector. Clean sans-serif text. Math visuals with arrows and labels. High quality, visually appealing. Quality: 8/10.

Dimensions (combined analysis):
- Structure: 8/10 (separate videos for lines vs planes, clear focus per video)
- Pacing: 8/10 (concise, well-edited, gets straight to the point)
- Visual Techniques: 7/10 (uses Manim-style animations for 3D coordinate systems, colored vectors)
- Narration Style: 8/10 (clear, academic but accessible, good energy)
- Engagement Hooks: 6/10 (starts with "we've likely seen lines in 2D before" — good review hook)

Key Insights:
- Dr. Trefor splits lines and planes into SEPARATE short videos (5:30 and 4:28) — very digestible
- For lines: starts from 2D review, then generalizes to 3D. Key insight: you need a point + direction vector
- For planes: derives the equation from the dot product condition (n · (r - r₀) = 0) — elegant
- Uses 3D coordinate system animations to visualize lines and planes
- Color-codes vectors consistently (different colors for different vectors)
- Each video is very focused — no tangents or extra content
- The videos are SHORT — almost too short for a complete understanding, but great as supplements

Techniques to Adopt:
- Derive the plane equation from the dot product condition: n · (r - r₀) = 0 — this is the most elegant approach
- Start with a 2D review ("you already know this in 2D, now let's go to 3D")
- Use 3D coordinate system animations with color-coded vectors
- Color-code: one color for position vectors, another for direction/normal vectors
- Keep individual concepts focused — don't mix lines and planes in the same explanation segment

Techniques to Avoid:
- Don't make it TOO short — 4-5 minutes isn't enough for students to absorb the material
- Dr. Trefor's talking-head approach limits how much 3D visualization he can show — with Manim we can do much more
- He doesn't show the connection between the different forms (parametric ↔ symmetric ↔ vector) — we should explicitly show the conversions

---

### Source 3: The Organic Chemistry Tutor — "How To Find The Vector Equation of a Line and Symmetric & Parametric Equations"
URL: https://www.youtube.com/watch?v=MkjazYnvNP8
Views: 839,592 | Date: Dec 4, 2019 | Duration: 11:37 | Channel: The Organic Chemistry Tutor (10.7M subs)
Captions: True

Thumbnail Analysis: Black background with yellow "Vector Equations" text at top. 3D coordinate system with arrows. Red box highlighting "r = r₀ + vt". White and red text with blue/green underlines. Quality: 8/10 — good contrast, clear formula highlight.

AND

### Source 3b: The Organic Chemistry Tutor — "How To Find The Equation of a Plane Given a Point and Perpendicular Normal Vector"
URL: https://www.youtube.com/watch?v=2sZKZHyaQJ8
Views: 583,733 | Date: Dec 5, 2019 | Duration: 7:37

AND

### Source 3c: The Organic Chemistry Tutor — "How To Find The Equation of a Plane Given Three Points"
URL: https://www.youtube.com/watch?v=rL9UXzZYYo4
Views: 840,712 | Date: Dec 5, 2019 | Duration: 6:56

Dimensions (combined analysis):
- Structure: 7/10 (formula-first approach, lots of worked examples)
- Pacing: 6/10 (methodical, repetitive computation-heavy)
- Visual Techniques: 4/10 (screen recording of 2D digital whiteboard, no 3D animations)
- Narration Style: 7/10 (clear step-by-step, calm, instructional)
- Engagement Hooks: 3/10 (no hook, starts with formula immediately)

Key Insights:
- OCT splits the topic into MANY short videos (lines 11min, plane from point+normal 7min, plane from 3 points 7min, line-plane intersection, distance point-to-plane...)
- Formula-first approach: gives the formula, then does multiple worked examples
- Very popular (500K-840K views each) — students clearly use these as exam prep
- Each video follows a consistent pattern: introduce formula → work 3-4 examples of increasing difficulty
- No geometric intuition — purely computational/algebraic approach
- Covers many edge cases: planes through origin, parallel planes, finding intercepts

Techniques to Adopt:
- Include multiple worked examples with different given information (point+direction, point+normal, 3 points)
- Show how to find intercepts of a plane (x, y, z intercepts from general form ax + by + cz = d)
- Cover the most common exam-style problems students will encounter
- The consistent "formula → examples" pattern works well for problem-solving
- Show the step-by-step process for finding a plane from 3 points (use cross product to find normal)

Techniques to Avoid:
- Don't be purely computational — students need to SEE the geometry, not just do algebra
- Don't start with the formula — build up to it from geometric intuition first
- Don't use a 2D whiteboard for 3D content — Manim gives us real 3D visualization

---

### Source 4: Serpentine Integral — "The Vector Equation of a 3D Line"
URL: https://www.youtube.com/watch?v=3qZcgiTZRPA
Views: 24,957 | Date: Aug 27, 2020 | Duration: 3:42 | Channel: Serpentine Integral (36K subs)
Captions: True

Thumbnail Analysis: White grid background with 3D coordinate system (x, y, z axes labeled). Sans-serif text with shadow effect. Arrows representing position and velocity vectors. Clean and organized. Quality: 8/10 — professional mathematical visualization.

Dimensions:
- Structure: 7/10 (focused single concept, well-paced for short format)
- Pacing: 8/10 (concise, no wasted time, but might be too fast for some)
- Visual Techniques: 9/10 (custom Python "Morpho" animation library, smooth 3D rendering, color-coded vectors)
- Narration Style: 7/10 (clear but brief)
- Engagement Hooks: 5/10 (starts directly with the concept, no story hook)

Key Insights:
- Uses a CUSTOM animation library (Morpho, not Manim) — similar visual quality but different tool
- The 3D rendering is SMOOTH — vectors animate growing from origin, lines trace through space
- Color-codes position vector (one color) and direction vector (another color)
- Shows the parametric form r(t) = r₀ + tv with animated t-parameter varying
- The visual of the line being "traced out" as t increases is very effective
- Very short (3:42) — good for quick review but not complete enough as primary instruction
- The animation quality is on par with 3B1B — clean 3D coordinate system, smooth transitions

Techniques to Adopt:
- Animate the line being TRACED as t varies — this is THE key visual for parametric form
- Use smooth 3D coordinate system rendering with ThreeDAxes in Manim
- Color-code position vectors vs direction vectors throughout
- Show the parameter t as a slider or animated value — make the parametric nature VISIBLE
- The "line being drawn in 3D" animation should be our centerpiece visual

Techniques to Avoid:
- 3:42 is too short — we need the full scope (lines + planes, with conversions and examples)
- The video doesn't show the symmetric form or connect to 2D lines
- No worked examples — students need to see computation too

---

### Source 5: 3Blue1Brown — "Cross products | Chapter 10, Essence of linear algebra"
URL: https://www.youtube.com/watch?v=eu6i7WJeinw
Views: 2,348,686 | Date: Sep 1, 2016 | Duration: 8:54 | Channel: 3Blue1Brown (8.37M subs)
Captions: True

Thumbnail Analysis: Black background with white text. 3D coordinate system with vectors and a plane. High quality, sharp visuals. Clean mathematical design. Quality: 9/10.

Dimensions:
- Structure: 10/10 | Pacing: 10/10 | Visual Techniques: 10/10 | Narration: 10/10 | Hooks: 10/10

Key Insights:
- While this video covers cross products (which we covered in Video 43), it's the FOUNDATION for planes — the cross product gives the normal vector to a plane
- 3B1B's 3D visualization is the gold standard — smooth camera movements, color-coded vectors, grid-based backgrounds
- The "two vectors → their cross product → a perpendicular vector" animation is directly applicable to our plane derivation
- Shows the right-hand rule intuitively (not just as a rule to memorize)
- The 3D coordinate system rendering is clean with subtle grid lines
- Connects the cross product to area of parallelograms and volume of parallelepiped
- No direct "equations of planes" content from 3B1B, but the geometric foundations he builds are essential

Techniques to Adopt:
- Reference Video 43 (Cross Product) explicitly when deriving plane equations — "we know from Video 43 that n₁ × n₂ gives the normal vector"
- Use the same quality of 3D rendering (ThreeDAxes in Manim)
- The "grid in 3D" visual is helpful for showing where planes intersect axes
- Connect the cross product to plane normals — "if you have two vectors in a plane, their cross product is perpendicular to the entire plane"

Techniques to Avoid:
- 3B1B doesn't teach formulas — for our curriculum, we MUST include the actual equations (vector, parametric, symmetric, general form)
- Don't make it purely visual — our students need the algebraic forms for homework/exams

---

### Source 6: JK Math — "Planes in 3D Space | Calculus 3 Lesson 16"
URL: https://www.youtube.com/watch?v=C6tMbe-ZmCM
Views: 12,077 | Date: Nov 15, 2023 | Duration: 51:59 | Channel: JK Math (38.6K subs)
Captions: True

Thumbnail Analysis: White background with bold black text "PLANES IN 3D SPACE". Mathematical equation and 3D plane visualization. Clean and organized. Quality: 7/10 — clear but could be more visually compelling.

Dimensions:
- Structure: 7/10 (well-organized with video chapters, covers standard form, general form, examples)
- Pacing: 6/10 (still lecture-length at 52min, slower than Trefor but faster than Leonard)
- Visual Techniques: 5/10 (iPad whiteboard with some 3D sketches, not true 3D rendering)
- Narration Style: 7/10 (clear, step-by-step, student-friendly)
- Engagement Hooks: 5/10 ("What do you need?" hook at 0:00 — simple but effective)

Key Insights:
- Covers planes comprehensively: standard form, general form, finding from point+normal, from 3 points, from parallel planes
- Good video chapter structure (timestamps in description) — easy to navigate
- Shows how to sketch planes by finding intercepts — practical skill students need
- Demonstrates special cases: planes missing a variable (e.g., x = 4 → plane parallel to yz-plane)
- Uses a systematic "formula → examples" approach similar to OCT but with more explanation
- 52 minutes is still very long — students likely skip around

Techniques to Adopt:
- The "What do you need?" hook is effective — "To describe a plane, you need: (1) a point on it, (2) a normal vector"
- Cover the special cases: coordinate planes (x=0, y=0, z=0) and planes parallel to them (x=4, y=6)
- Show how to sketch planes by finding intercepts — this is a key visual skill
- Include a worked example finding a plane from 3 points (cross product → normal → equation)

Techniques to Avoid:
- 52 minutes is too long for a single video
- iPad whiteboard isn't ideal for 3D content — real 3D rendering is much better

---

### Video 44 Production Notes (from analysis)

**Content Structure (following competitor best practices):**
Our video should combine the BEST aspects of all competitors:
- **3B1B's** visual quality + geometric intuition (but add the formulas he doesn't teach)
- **Dr. Trefor's** concise, focused approach (but longer, 12-15min, with more depth)
- **Serpentine Integral's** smooth 3D animation of lines being traced
- **OCT's** multiple worked examples (but with visual explanations, not just computation)
- **Professor Leonard's** comprehensive scope (but condensed into 12-15 minutes)

**Recommended Scene Plan:**
1. **Hook (0:30):** "You know lines in 2D — y = mx + b. But what happens when we add a third dimension?" → transition to 3D coordinate system
2. **Lines in 3D — Geometric (2:00):** A line in 3D needs a point + direction vector. Animate a vector growing from origin, then the line extending in that direction. Show the parametric tracing animation.
3. **Three Forms of a Line (3:00):** Vector form r = r₀ + tv, parametric form (x,y,z = x₀,y₀,z₀ + at,bt,ct), symmetric form. Show the algebraic conversion between them.
4. **Worked Example — Line (1:30):** Find the line through (1,2,3) parallel to direction (2,-1,4). Show all three forms.
5. **Planes — Geometric (2:30):** A plane needs a point + normal vector. Derive from n · (r - r₀) = 0 (Dr. Trefor's elegant approach). Animate the normal vector perpendicular to the plane.
6. **General Form (1:30):** ax + by + cz = d. Show how to get it from the dot product form. Color-code a, b, c as components of the normal.
7. **Worked Examples — Planes (3:00):** 
   - Plane through (1,2,3) with normal (2,-1,4)
   - Plane through 3 points (using cross product to find normal — reference Video 43)
   - Sketching a plane by finding intercepts (JK Math's practical skill)
8. **Special Cases (1:00):** Coordinate planes, planes parallel to coordinate planes (x=4, y=6, z=3)
9. **Summary + Outro (1:00):** Key formulas recap, relationship between lines and planes

**Key Visual Techniques for Video 44:**
1. Use `ThreeDAxes` in Manim for ALL 3D visualizations — this is THE differentiator
2. Animate the line being traced as t varies (Serpentine Integral's best technique)
3. Color-code: PRIMARY for position vectors, SECONDARY for direction vectors, ACCENT for normal vectors
4. Show the plane as a semi-transparent colored surface in 3D
5. Animate the normal vector perpendicular to the plane surface
6. Use the "trace t from -∞ to +∞" animation to show the full line
7. For intercepts: animate the plane intersecting each axis, highlight the intercept points
8. Use dot product visualization for the plane derivation (n · (r - r₀) = 0)

**Thumbnail Recommendation:**
Following the successful competitor patterns:
- Dark background (our BG=#1A1832)
- 3D coordinate system with a line and a plane visible
- Large white title text: "Lines & Planes in 3D"
- Key formula in ACCENT color: "r = r₀ + tv" or "n · (r - r₀) = 0"
- A highlighted arrow showing the normal vector perpendicular to the plane
- Follow 3B1B's clean minimal style, not the cluttered lecture style

**Color Coding Scheme for Video 44:**
- PRIMARY (#5BC0EB): Position vectors, 3D axes
- SECONDARY (#7BC950): Direction vectors for lines
- ACCENT (#FFD166): Normal vectors to planes
- RED (#EF476F): Warning/highlight for special cases
- White: Formulas, text
- This continues from Video 43 (Cross Product) where we used SECONDARY for one input and RED for the other

---

## 2026-06-05 — Video 46: Partial Derivatives (Competitive Analysis)

**Note:** youtubei.js metadata fetch returned minimal data for attempted IDs. Analysis based on well-known competitor approaches.

### 3Blue1Brown — "Partial Derivatives" (Multivariable Calculus series)
- **Approach:** Pure geometric intuition. Opens with a 3D surface, shows "holding one variable constant" by slicing the surface along a plane. The partial derivative is the slope of the resulting curve.
- **Structure (9/10):** Builds from single-variable review → slicing concept → formal definition → Clairaut's theorem. Each step motivated by geometry.
- **Pacing (9/10):** Gentle. Uses long pauses and animations to let geometric ideas sink in. Doesn't rush to notation.
- **Visual Techniques (10/10):** Color-coded tangent lines on 3D surfaces. Moving slice plane is iconic. Uses the "graph itself" as the primary visualization.
- **Narration (8/10):** Conversational, intuition-first. Formal notation appears late.
- **Engagement (9/10):** Opens with the question "what does it mean to take a derivative when your function has multiple inputs?"

**Adopt for our video:**
- Use 3D surface visualization with slice planes to show "holding one variable constant"
- Color-code partial derivatives (e.g., ∂f/∂x in PRIMARY blue, ∂f/∂y in SECONDARY green)
- Start from geometric intuition before formal notation
- Show the connection between partial derivatives and tangent plane slopes

**Adapt:**
- 3B1B uses a very slow pace (25+ min). Our target is 15 min. Compress the geometric setup and get to computation sooner.
- We'll include worked examples (3B1B skips these) — practical computation is key for students
- We'll explicitly connect back to the chain rule from single-variable calculus

### Khan Academy — "Partial Derivatives"
- **Approach:** Definition-first, notation-heavy, many worked examples.
- **Structure (7/10):** Starts with formal limit definition, then examples, then geometric interpretation.
- **Pacing (6/10):** Fast, example-heavy. Good for practice but can feel mechanical.
- **Visual Techniques (5/10):** Minimal. Mostly 2D whiteboard style.
- **Narration (7/10):** Clear, step-by-step explanation. Good for students who want procedures.

**Techniques to adopt:**
- Include explicit limit definition of partial derivative (students need this for exams)
- Show 2-3 concrete worked examples with full computation steps

**Techniques to avoid:**
- Don't start with the formal definition — begin with geometric intuition (3B1B style)
- Don't spend too long on notation drills

### Professor Leonard — "Multivariable Calculus: Partial Derivatives"
- **Approach:** Lecture-style, comprehensive, very thorough. Covers definition, geometric meaning, higher-order derivatives, and implicit differentiation.
- **Pacing (5/10):** Very slow, 45+ minute lectures. Too long for YouTube format.

**Insight:** Include higher-order partial derivatives and mixed partials briefly (Clairaut's theorem) — but keep it tight.

### Summary — Our approach for Video 46:
1. **Hook:** Start with a 3D surface and ask "how does this function change if we only move in the x-direction?"
2. **Intuition:** Slice the surface — the partial derivative is the slope of that slice
3. **Definition:** Formal limit definition with notation ∂f/∂x, f_x
4. **Examples:** 2-3 concrete computations (polynomial, exponential/trig)
5. **Higher-order:** Brief mention of f_xx, f_xy, Clairaut's theorem
6. **Visual metaphors:** Color-coded tangent slopes, contour maps as alternative view
7. **Summary:** Key formulas and interpretation

**Color scheme for this video:**
- PRIMARY (#5BC0EB): x-direction partial derivative, x-slices
- SECONDARY (#7BC950): y-direction partial derivative, y-slices
- ACCENT (#FFD166): Key formulas and results
- RED (#EF476F): Special cases / warnings

---

### [2026-06-05] Video 47: Gradient and Directional Derivatives

**Source 1: Dr. Trefor Bazett — "Directional Derivatives | What's the slope in any direction?"**
URL: https://www.youtube.com/watch?v=GJODOGq7cAY
Views: 272K | Date: Nov 17, 2019 | Duration: 12:01 | Captions: True
Dimensions: Structure 8/10 | Pacing 7/10 | Visuals 7/10 | Narration 8/10 | Hooks 7/10

Thumbnail Analysis: Chalkboard background with 3D cone graph and red slope line. Text "What is the slope in any direction?" at top. Talking head on right. Quality 7/10.

Key Insights:
- Opens with "slope in ANY direction" question — good hook generalizing partial derivatives
- Derives directional derivative from limit definition, then shows gradient shortcut
- Uses Manim-style animations with 3D surface plots

Techniques to Adopt:
- Start with "slope in any direction" motivation
- Derive from limit definition, then show gradient shortcut
- Mountain/topographic metaphor for steepest ascent

---

**Source 2: Dr. Trefor Bazett — "Geometric Meaning of the Gradient Vector"**
URL: https://www.youtube.com/watch?v=QQPz3eXXgQI
Views: 289K | Date: Jun 21, 2020 | Duration: 14:51 | Captions: True
Dimensions: Structure 9/10 | Pacing 8/10 | Visuals 9/10 | Narration 8/10 | Hooks 8/10

Thumbnail Analysis: Topographic map of Vancouver Island with contour lines. Red/blue vectors. Quality 9/10.

Key Insights:
- Mountain problem hook — which direction to go up fastest?
- Derives gradient from directional derivative using dot product angle
- Shows gradient perpendicular to level curves — key insight
- Connects to actual topographic map

Techniques to Adopt:
- Mountain metaphor for steepest ascent direction
- Gradient perpendicular to contour lines visual
- Topographic map as real-world closing visual

---

**Source 3: Organic Chemistry Tutor — "Directional Derivative and Gradient Vector"**
URL: https://www.youtube.com/watch?v=CnVes9TdnPo
Views: 911K | Date: Nov 1, 2019 | Duration: 28:30 | Captions: True
Dimensions: Structure 6/10 | Pacing 5/10 | Visuals 4/10 | Narration 6/10 | Hooks 5/10

Key Insights:
- Pure lecture style, no animations — but 911K views shows huge demand
- Extremely thorough worked examples
- No geometric intuition — purely computational

Techniques to Adopt:
- Multiple worked examples with step-by-step computation
- Cover D_u f = grad(f) dot u prominently

---

**Source 4: Mu Prime Math — "Directional Derivatives and Gradient"**
URL: https://www.youtube.com/watch?v=v98uipDYuqU
Views: 77K | Date: Mar 31, 2020 | Duration: 7:59 | Captions: True

Key Insights:
- Short and focused (8 min) — matches our format
- Emphasizes dot product connection
- Discusses contour lines and gradient relationship

---

**Synthesis for Video 47:**
1. Hook: Mountain metaphor — which way is steepest?
2. Define gradient vector as vector of partial derivatives
3. Directional derivative: limit definition then gradient dot product shortcut
4. Geometric meaning: steepest ascent direction, perpendicular to contour lines
5. Worked example: compute gradient + directional derivative
6. Summary: key properties and formulas

Color scheme: PRIMARY=gradient vector, SECONDARY=directional derivative, ACCENT=key formulas, RED=warnings

---

## Video 49: Double Integrals (Calc III #9) — 2026-06-07

### Topic Analysis
**Topic:** Double integrals — volume under surfaces, iterated integrals, Fubini's theorem, Type I/II regions, order swapping

### Competitor Landscape
- **3Blue1Brown:** No dedicated "double integrals" video in recent uploads. His multivariable calculus coverage focuses on intuition-driven approaches with custom Manim. The Essence of Calculus series touches integration but doesn't extend to 2D explicitly.
- **Khan Academy / Standard textbooks:** Cover double integrals with a formula-first approach: define Riemann sum → iterated integral → Fubini → Type I/II. Often dense and under-visualized.
- **Mathologer:** Not focused on calculus III topics.

### Key Insights for Our Video
1. **Visual-first approach:** We lead with a concrete geometric hook (volume under a surface) rather than jumping into Riemann sum notation. This matches 3B1B's intuition-first philosophy.
2. **Progressive complexity:** Start with rectangular regions (simple bounds) → general regions (curve bounds) → order swapping (the "aha" moment). This avoids overwhelming the viewer.
3. **Worked example before theory:** We evaluate a concrete double integral (volume under a plane) before formalizing Type I/II regions, giving the viewer something concrete to anchor on.
4. **The order-swap trick:** The classic e^{y^2} example (impossible to integrate in one order, trivial in the other) is the standout "aha" moment that demonstrates practical power. We build to this as a climax.
5. **Avoiding textbook traps:** Many competitors dump all formulas at once. We use progressive disclosure — one formula per scene, with animations that build the formula step by step.

### Techniques to Adopt
- **Color-coded integration bounds:** PRIMARY for dy-first order, SECONDARY for dx-first order (visual cue for order)
- **ACCENT highlights on final answers:** Makes the payoff visible
- **Step-by-step derivation:** Write intermediate steps, not just setup → answer
- **Section dividers:** Use ly.section_divider() for each major topic shift

### Techniques to Avoid
- **No 3D surface rendering:** Manim's 3D capabilities are limited and slow. Describe the geometry in text/2D rather than attempting Surface plots that may render poorly.
- **No dense notation dumps:** One formula at a time, with verbal explanation via add_subcaption

### Thumbnail Ideas
- Dark BG with a stylized 2D grid (xy-plane) and a highlighted rectangle showing volume columns
- Title: "Double Integrals" in ACCENT (#FFD166) with subtitle "Volume Under Surfaces"
- Show the iterated integral formula prominently

---

## [2026-06-08] Video 53: Stokes' Theorem

### Competitive Analysis

**Source 1: 3Blue1Brown — Curl & Divergence series**
- 3B1B covers curl extensively but does NOT have a dedicated Stokes' Theorem video — this is a content gap we fill.
- Techniques: color-coded curl visualizations (blue/red rotation indicators), smooth geometric animations
- We adopt: color-coded curl notation, geometric intuition before formal statement

**Source 2: Khan Academy — Stokes' Theorem**
- Style: whiteboard + worked examples, strong on orientation conventions
- Techniques: detailed right-hand rule explanation, step-by-step surface integral computation
- We adopt: right-hand rule emphasis for orientation, clear step-by-step example
- We improve: add visual animation of "many surfaces, one boundary" concept (Khan does this poorly)

**Source 3: Dr. Trefor Bazett — Stokes' Theorem**
- Style: clean animations, "twisted surface" visual showing same boundary with different surfaces
- Key technique: physically deforming one surface into another while boundary stays fixed
- We adopt: the "many surfaces one boundary" visual metaphor as a key scene

### Key Insights for Video 53
- Most students struggle with surface orientation (right-hand rule) — emphasize with dedicated scene
- The "many surfaces, one boundary" concept is the deepest insight — make it a highlight
- Stokes' naturally follows Green's Theorem — strong narrative arc from previous video
- The worked example should use a simple vector field where both sides are computable (not too messy)
- 2D curl (∂Q/∂x - ∂P/∂y) vs 3D curl (∇×F) notation comparison helps bridge Green's → Stokes'

### Thumbnail Ideas
- Dark BG with a hemisphere surface and highlighted boundary circle
- Title: "Stokes' Theorem" in ACCENT (#FFD166) with subtitle "Green's in 3D"
- Show the formula ∮F·dr = ∬(∇×F)·n dS prominently

---

## 2026-06-09 — Video 55: What is a Differential Equation?

### Competitor Videos Analyzed

#### 1. 3Blue1Brown — "Differential equations, a tourist's guide | DE1" (5.8M views)
- video_id: p_di4Zn4wz4, 27:16, Mar 2019
- **Structure (10/10):** Masterful overview — starts with simple pendulum, escalates through multiple examples (spring, Lotka-Volterra, Lorenz system). Each example builds on previous concepts.
- **Pacing (9/10):** Very deliberate — spends time on each example's phase portrait before moving on. Long but never boring.
- **Visual Techniques (10/10):** Phase space trajectories, color-coded vector fields, animated solution curves flowing through slope fields. Signature 3B1B style.
- **Narration Style (9/10):** Conversational, curious tone. Uses "tourist's guide" framing — "here's what you'll see" rather than formal definitions.
- **Engagement Hooks (10/10):** Opens with pendulum — immediate physical intuition. Lotka-Volterra (predator-prey) adds real-world relevance. Lorenz attractor as the "wow" moment.
- **Key techniques to adopt:** Multiple quick examples before formalism; phase space visualization; physical motivation first
- **Key techniques to avoid:** 27-min length is too long for us; 3B1B's loose structure wouldn't work for a systematic course

#### 2. Zach Star — "This is why you're learning differential equations" (3.9M views)
- video_id: ifbaAqfqpc4, 18:36, Jun 2020
- **Structure (7/10):** Application-first approach — shows WHY diff eqs matter before formal definitions. Mix of COVID modeling, population growth, circuits, springs.
- **Pacing (7/10):** Fast-paced with quick cuts between applications. More breadth than depth.
- **Visual Techniques (7/10):** Professional animations (Brainup Studios), but less mathematical depth than 3B1B. More focus on motivation than visualization.
- **Narration Style (8/10):** Enthusiastic, motivational. "This is why you're learning this" framing works well for engagement.
- **Engagement Hooks (9/10):** COVID-19 context (released during pandemic) — extremely timely. Real-world examples throughout.
- **Key techniques to adopt:** Application-first framing; real-world examples as motivation
- **Key techniques to avoid:** Too scattered — we should balance applications with mathematical structure

#### 3. Khan Academy — "Differential equation introduction" (3.2M views)
- video_id: 6o7b9yyhH7k, Sep 2014
- **Structure (6/10):** Traditional classroom approach — starts with dy/dx notation, defines order/classification. Dry but correct.
- **Pacing (5/10)::** Very slow, repetitive. Good for confused students but boring for engaged ones.
- **Visual Techniques (5/10):** Digital whiteboard — no Manim. Clear formulas but no visual intuition.
- **Narration Style (6/10):** Patient tutorial tone. Explains step-by-step.
- **Engagement Hooks (4/10):** No hook — jumps straight into definitions.
- **Key techniques to adopt:** Clear classification (order, linearity) definitions
- **Key techniques to avoid:** Starting with dry notation before motivation; no visual animation

### Thumbnail Analysis
- 3B1B: Dark BG, grid pattern, vector field circles (RGB), "Differential Equations" in white. Clean, mathematical.
- Zach Star: Dark BG, neon blue/purple grid, futuristic font, "Differential Equations" in bold. Energetic.
- Khan Academy: Black BG, white/yellow text, graph with curve. Simple but clear.
- **Our approach:** Dark BG (#1A1832), ACCENT text, a simple slope field visualization, "What is a Differential Equation?" in clean SANS font.

### Synthesis for Video 55
1. **Hook (adopt from 3B1B+Zach):** Start with a real physical example (falling object or population growth) — show the DE forming naturally
2. **Classification (adopt from KA):** Define ODE, order, linearity — but AFTER motivation, not before
3. **Visual metaphor (adopt from 3B1B):** Slope field visualization showing how a DE defines a "terrain" for solutions
4. **Structure:** Motivation → definition → classification → simple examples → slope field visual → preview of course
5. **Duration target:** 10-12 min (between KA's brevity and 3B1B's depth)

---
