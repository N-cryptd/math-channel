# Video 161: Lebesgue vs Riemann Integration

**Playlist:** Measure Theory (Video 12 of 12 — SERIES FINALE)
**Class:** Video161_LebesgueVsRiemann
**File:** scripts/graduate/video-161-lebesgue-vs-riemann.py
**Estimated duration:** ~560s (9 min)

## Topics
1. Recap: Riemann integration from first principles (partition-based)
2. How Lebesgue integration works differently (level sets / horizontal slices)
3. Key differences: partitions of x-axis vs partitions of y-axis
4. Comparison of the integral spaces (which functions are integrable?)
5. Advantages of Lebesgue: dominated convergence, L^p completeness, etc.
6. Examples of Lebesgue-integrable but not Riemann-integrable (Dirichlet function)
7. Examples of Riemann-integrable functions (continuous on compact sets)
8. Lebesgue's characterization theorem (Riemann integrable ↔ bounded + a.e. continuous)
9. Practical guidance: when to use which
10. Summary of the Measure Theory playlist + what's next

## Prerequisites
- Videos 151-160 (complete Measure Theory playlist)
- Calculus I Videos 14-15 (Integration basics, IBP)

## Competitive Analysis
**Note:** Analysis skipped (youtubei.js search returned minimal data). Plan draws on standard exposition (Rudin, Tao, Folland).

## Scene Plan

### Scene 1: Hook — Two Ways to Integrate (30s)
**Content budget:** Title + visual comparison + 2 text items
- "The Riemann integral partitions the x-axis. The Lebesgue integral partitions the y-axis."
- Visual: vertical slices (Riemann) vs horizontal slices (Lebesgue)
- Motivating question: which is "better"?

### Scene 2: Riemann Integration Recap (40s)
**Content budget:** Title + formula + 2 items
- Upper sum U(f,P) and lower sum L(f,P)
- Riemann integrable if sup L(f,P) = inf U(f,P) as ||P|| → 0
- Requires continuity almost everywhere (bounded + compact support)

### Scene 3: Lebesgue Integration Approach (45s)
**Content budget:** Title + formula + 2 items
- Simple function approximation from below
- ∫ f dμ = sup{∫ s dμ : s simple, 0 ≤ s ≤ f}
- Horizontal slicing vs vertical slicing (key intuition)

### Scene 4: Key Differences (45s)
**Content budget:** Two-column comparison (4 items)
| Feature | Riemann | Lebesgue |
|---------|---------|----------|
| Slices | Vertical (x-axis) | Horizontal (y-axis) |
| Domain | Bounded intervals | Arbitrary measure spaces |
| Limit behavior | Interchanging limit/integral hard | DCT/MCT make it easy |
| Integrable functions | Bounded + a.e. continuous | Bounded measurable on finite measure |

### Scene 5: Dirichlet Function Example (45s)
**Content budget:** Title + formula + 2 items
- f(x) = 1 if x ∈ Q, 0 if x ∉ Q
- Not Riemann integrable (U = 1, L = 0)
- Lebesgue integrable: ∫ f dλ = 0 (Q has Lebesgue measure zero)

### Scene 6: Lebesgue's Characterization (40s)
**Content budget:** Title + theorem in formula box + 1 text
- Theorem: f is Riemann integrable on [a,b] iff
  - f is bounded AND
  - The set of discontinuities has Lebesgue measure zero
- "Riemann integrability is a measure-theoretic property!"

### Scene 7: Advantages of Lebesgue Integration (40s)
**Content budget:** Title + 3 progressive items
- L^p spaces are complete (Banach/Hilbert spaces)
- Convergence theorems (MCT, DCT, Fatou) allow limit interchange
- Works on arbitrary measure spaces (not just R^n)
- Better for probability theory (expectation, conditional expectation)

### Scene 8: Practical Guidance (35s)
**Content budget:** Title + 2-column: when Riemann vs when Lebesgue
- Use Riemann: basic calculus, physics, engineering (intuition-friendly)
- Use Lebesgue: probability, functional analysis, convergence questions
- For continuous functions on [a,b]: they agree!

### Scene 9: Playlist Recap + Series Outro (45s)
**Content budget:** Takeaways (4 items) + outro
- Measure theory gives us: sigma-algebras, Lebesgue measure, the integral
- Convergence theorems are the payoff
- RN derivatives, product measures, Fubini complete the toolkit
- Next: Functional Analysis (Video 162+)

## Visual Design Notes
- Use a visual diagram comparing vertical slices (Riemann) vs horizontal slices (Lebesgue)
- Color-code: PRIMARY for Riemann, SECONDARY for Lebesgue throughout
- Dirichlet function: animate the rationals coloring vs the Lebesgue measure zero
- Formula box for Lebesgue's characterization theorem
- Play outro with special "series complete" styling
