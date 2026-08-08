# Video 165: Hilbert Spaces

**Playlist:** Functional Analysis
**Prerequisites:** Video 164 (Inner Product Spaces), Video 163 (Banach Spaces), Video 158 (L^p Spaces)

## Competitive Analysis Summary
- No major competitor channel has a dedicated Manim-animated video on Hilbert Spaces
- Steve Brunton covers applications (optimization, ML) but uses whiteboard style, not animation
- 3B1B has no dedicated Hilbert space video (touches on it in Fourier/quantum series)
- This is a significant gap in the market — we can be the first animated exposition
- Our approach: bridge the inner product space (Video 164) + completeness (Video 163) into a unified concept

## Scene Plan

### Scene 1: Hook — The Perfect Marriage (0:00-1:30)
**Content budget:** 4 items max
- Hook: "What do you get when you combine the geometry of inner product spaces with the analytic power of completeness?"
- Answer: A Hilbert space — the natural setting for Fourier analysis, quantum mechanics, and signal processing
- Motivation: In an inner product space, Cauchy sequences might not converge. Hilbert spaces guarantee they do.
- Items: 3 text items + formula \|x - x_n\| → 0

### Scene 2: Definition (1:30-3:00)
**Content budget:** 4 items
- Section divider: "Definition: Hilbert Space"
- Definition: A Hilbert space is a complete inner product space
- Two inputs: (X, ⟨·,·⟩) where X is complete under the induced norm
- Equivalent: "Banach space whose norm comes from an inner product"
- Key formula: \|x\| = √⟨x,x⟩ + every Cauchy sequence converges

### Scene 3: Why Completeness Matters (3:00-5:00)
**Content budget:** 4 items
- Example of non-complete inner product space: C[0,1] with L^2 inner product
- Cauchy sequence of continuous functions converging to a discontinuous function
- The limit is NOT in C[0,1] — it's in L^2[0,1]
- Completion gives L^2[0,1], a Hilbert space

### Scene 4: Examples (5:00-7:00)
**Content budget:** 3 items per example (swap out)
- l^2: square-summable sequences (separable, countable basis)
- L^2(Ω): square-integrable functions (infinite-dimensional)
- C^n (finite-dimensional — all finite-dimensional inner product spaces are Hilbert)
- Brief mention: Sobolev spaces H^k

### Scene 5: Orthogonal Decomposition (7:00-9:00)
**Content budget:** 4 items
- Theorem: If M is a closed subspace, H = M ⊕ M⊥
- Proof sketch: take x, project onto M, remainder is in M⊥
- Projection theorem: every x has unique decomposition x = m + n where m ∈ M, n ∈ M⊥
- This is the foundation of Fourier series and least squares

### Scene 6: Orthonormal Bases and Fourier Expansion (9:00-11:30)
**Content budget:** 4 items
- Separable Hilbert spaces have countable orthonormal bases
- Fourier expansion: x = Σ ⟨x, e_n⟩ e_n
- Parseval's identity: \|x\|^2 = Σ |⟨x, e_n⟩|^2
- Example: {1, cos(nx), sin(nx)} in L^2[-π,π]

### Scene 7: Riesz Representation Theorem (11:30-13:30)
**Content budget:** 4 items
- Statement: Every continuous linear functional f on H is f(x) = ⟨x, y⟩ for some y ∈ H
- \|f\| = \|y\| (isometric isomorphism between H and H*)
- This is WHY inner products matter — they capture ALL continuous linear functionals
- Bridge to next video: Bounded Linear Operators (Video 166)

### Scene 8: Summary + Outro (13:30-15:00)
**Content budget:** 3 items
- Key takeaways recap (3 bullet points)
- Outro with play_outro()

## Duration Target: 12-15 minutes
