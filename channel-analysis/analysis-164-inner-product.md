# Competitive Analysis: Video 164 — Inner Product Spaces

## 2026-08-07 — Inner Product Spaces (Functional Analysis context)

### Videos Analyzed

#### 1. TBSOM — "Functional Analysis 9 | Examples of Inner Products and Hilbert Spaces" (eiD6OueArHE)
- Views: 40,056 | Date: Oct 2020 | Duration: 7:07
- Dimensions: Structure 7/10 | Pacing 6/10 | Visuals 5/10 | Narration 6/10 | Hooks 5/10
- Tablet writing style, yellow bg with coordinate plane thumbnail
- Focus: quickly runs through examples (R^n, function spaces, sequence spaces)
- Strength: breadth of examples in short time
- Weakness: no visual intuition, definition-first, very surface level

#### 2. MIT OCW — "Lecture 14: Basic Hilbert Space Theory" (EBdgFFf54U0)
- Views: 59,666 | Date: Nov 2022 | Duration: 83:24
- Dimensions: Structure 8/10 | Pacing 4/10 | Visuals 2/10 | Narration 7/10 | Hooks 3/10
- Traditional blackboard lecture from MIT 18.102
- Strength: rigorous, covers Cauchy-Schwarz, orthogonality, projection theorem
- Weakness: extremely long, no animation, chalkboard-only, passive

#### 3. Frederic Schuller — "Separable Hilbert spaces - L03" (5OGCIwx0phI)
- Views: 52,370 | Date: Mar 2016 | Duration: 108:28
- Dimensions: Structure 7/10 | Pacing 3/10 | Visuals 1/10 | Narration 7/10 | Hooks 2/10
- Dense blackboard lecture, quantum theory context
- Strength: very thorough, covers separability, orthonormal bases, isomorphisms
- Weakness: 108 minutes, no visual aids, extremely dense formalism-first

#### 4. Steve Brunton — "Inner Products in Hilbert Space" (g-eNeXlZKAQ)
- Views: 158,271 | Date: Mar 2020 | Duration: 8:41
- Dimensions: Structure 7/10 | Pacing 7/10 | Visuals 6/10 | Narration 7/10 | Hooks 6/10
- Data science framing, dark bg with blue swirl thumbnail
- Strength: connects inner products to practical data science (SVD, PCA, projections)
- Weakness: brief, skips formal axioms, assumes prerequisites
- KEY INSIGHT: Application framing (data science) drives 3-4x views vs pure math

#### 5. Dr. Bevin Maultsby — "Inner Product Spaces and Cauchy Schwarz, Real Analysis II" (Crd4UG8Viw4)
- Views: 4,372 | Date: Aug 2024 | Duration: 25:21
- Dimensions: Structure 8/10 | Pacing 6/10 | Visuals 3/10 | Narration 6/10 | Hooks 4/10
- Modern black bg with integral formula thumbnail
- Strength: good structure (definition → properties → Cauchy-Schwarz proof → orthogonality)
- Weakness: slide-based, no animation, small audience

### Thumbnail Analysis
- Best: Steve Brunton (dark bg, blue swirl, structured text) — professional, eye-catching
- TBSOM: yellow bg with coordinate plane — functional but not premium
- MIT/Schuller: chalkboard shots — low visual appeal
- Dr. Maultsby: black bg with formula — modern, decent

### Key Insights
1. **HUGE market gap:** No high-quality animated Manim video covers inner product spaces at the graduate/functional analysis level. All competitors use chalkboard or tablet.
2. **Steve Brunton's application framing works:** 158K views vs 40-59K for pure math approaches. Connecting inner products to data science (projections, PCA) dramatically boosts engagement.
3. **The "ladder" from Video 162 is the key hook:** Inner product → norm → metric → topological. Showing what an inner product ADDS to a normed space (angle, orthogonality, projection) is the "aha moment."
4. **Cauchy-Schwarz is the star theorem:** Every competitor covers it. We should make it a visual proof highlight, not just a statement.
5. **Function inner products are the graduate leap:** R^n is familiar; <f,g> = integral of f*g is the new content. This is where we add value over the LA video 37.

### Techniques to Adopt
1. Start with "what does a norm NOT give you?" — angles, orthogonality, projection. An inner product does.
2. Visual proof of Cauchy-Schwarz using projection geometry (inspired by 3B1B style)
3. Animated comparison: R^n inner product vs L^2 function inner product (side by side)
4. Show Gram-Schmidt process working in function space (building orthogonal polynomials)
5. Application teaser: signal processing (Fourier series as orthogonal decomposition)

### Techniques to Avoid
1. Definition-first without motivation (Schuller/MIT approach)
2. Chalkboard aesthetic — oversaturated, lower engagement
3. Covering too many examples without depth
4. Going full Hilbert space in this video — save completeness for Video 165
