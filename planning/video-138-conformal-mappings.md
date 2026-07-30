# Video 138: Conformal Mappings

**Playlist:** Complex Analysis (Video 15 of 15 — FINAL)
**Class:** Video138_ConformalMappings
**Script:** scripts/undergraduate/video-138-conformal-mappings.py
**Est. Duration:** 12 min
**Status:** PLAN

## Competitive Analysis Summary

[Analysis based on known competitor content.]

- **3Blue1Brown:** Has NOT produced a dedicated conformal mappings video. His visual style would suggest: showing a grid in the z-plane being mapped to a curvy grid in the w-plane, with angles preserved at every intersection.
- **Faculty of Khan:** Has a video on conformal mappings. Whiteboard style, covers angle preservation and basic examples.
- **Michael Penn:** Has computation videos on Möbius transformations.
- **Dr. Peyam:** Lecture-style video.
- **BriTheMathGuy:** Manim-based but fast-paced.

**Market gap:** No video visually animates conformal mappings by showing a grid deforming while angles are preserved. The visual of "stretching and rotating but never shearing" is the key geometric insight and almost never animated.

**Techniques to adopt:**
- Animate a grid mapping: show z-plane grid → w-plane image, with angle preservation visible
- Visualize Möbius transformations as mappings of the extended complex plane
- Show practical applications: mapping disks to half-planes
- Make this a satisfying FINALE to the entire Complex Analysis playlist

## Scene Plan

### Scene 1: Hook — "Preserving Angles" (~50s)
- "We've explored integration, series, residues, and zeros. One last topic: geometry"
- "A conformal mapping is a function that preserves angles — curves that cross at 90° in the z-plane cross at 90° in the w-plane too"
- Visual: two perpendicular curves → mapped to two curves that are still perpendicular
- "This is the final video in our Complex Analysis playlist"

### Scene 2: What Makes a Mapping Conformal? (~55s)
- Theorem: f is conformal at z₀ if f'(z₀) ≠ 0
- Proof: f(z₀+h) ≈ f(z₀) + f'(z₀)·h. The factor f'(z₀) is a complex number = scaling × rotation. Scaling changes lengths, rotation changes direction, but angles between vectors are preserved
- Visual: show f'(z₀) = re^{iθ} as scaling by r and rotation by θ
- "The derivative being nonzero guarantees local angle preservation"
- Singularities and critical points (f' = 0) break conformality

### Scene 3: Möbius Transformations (~60s)
- Definition: T(z) = (az + b)/(cz + d) where ad - bc ≠ 0
- Properties: preserve angles, map circles/lines to circles/lines, invertible
- Visual: show specific Möbius transformation mapping a grid
- Example: T(z) = (z - i)/(z + i) maps upper half-plane to unit disk
- "Möbius transformations are the most important conformal mappings"

### Scene 4: Visualizing a Conformal Map (~55s)
- Example: w = z². This maps the first quadrant to the upper half-plane
- Visual: show the grid lines in the z-plane (Re=const, Im=const) mapped to curves in the w-plane
- At z = 0, f'(0) = 0, so the map is NOT conformal there — angles double
- "Conformal everywhere except at critical points"

### Scene 5: Applications (~50s)
- Conformal mappings solve PDEs by transforming domains
- Example: map a complicated domain to a simple one (disk or half-plane), solve there, map back
- Visual: irregular region → disk via conformal map
- "The Riemann Mapping Theorem guarantees such maps exist for simply-connected domains"

### Scene 6: Playlist Finale (~50s)
- Full recap of the entire Complex Analysis playlist (13 videos)
- "From complex numbers to conformal mappings — what a journey"
- Thank the viewer for completing the playlist
- Outro with "Complex Analysis — COMPLETE" marker

## Color Coding
- PRIMARY (#5BC0EB): z-plane, input domain, grid lines
- SECONDARY (#7BC950): w-plane, output domain, images
- ACCENT (#FFD166): theorem statements, Möbius transformations, key results
- RED (#EF476F): critical points, singularities, non-conformal regions
- DIM (#6B6B8D): computation steps, labels
