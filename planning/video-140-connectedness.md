# Video 140: Connectedness
## Topology Playlist — Video 7 of 12

**Class:** Video140_Connectedness
**Script:** scripts/graduate/video-140-connectedness.py
**Target Duration:** 12 minutes
**Level:** Graduate (L5)
**Prerequisites:** Video 139 (Introduction to Topology), Real Analysis (continuity, open/closed sets)

---

## Competitive Analysis Summary

**Market gap:** No major animation channel (3B1B, Mathologer, Numberphile) has a dedicated Manim-animated video on connectedness. All existing content is lecture-style whiteboard/blackboard.

**Existing content analyzed:**
- Socratica: "Connected vs Path Connected" (~45K views) — clean but static slides
- Various lecture channels: formal definition-heavy, no visual intuition
- No one visualizes the topologist's sine curve well (the canonical connected-but-not-path-connected example)

**Our opportunity:** First high-production animated treatment of connectedness. Visual-first approach with:
- Animated splitting of disconnected spaces
- Real-time drawing of paths for path-connectedness
- The topologist's sine curve as the key visual centerpiece

**Techniques to adopt:**
- Start with physical intuition (can you walk from A to B?) before formal definitions
- Use the topologist's sine curve as the "aha moment" — connected but NOT path-connected
- Color-code connected components to show partition structure

**Techniques to avoid:**
- Starting with the formal definition (A is connected if no clopen subsets exist) — too abstract
- Dense proof without geometric motivation
- Skipping path-connectedness (students always confuse these two concepts)

---

## Content Outline

### Scene 1: Hook — "Can You Walk From Here to There?" (~50s)
**Narration word count:** ~125 words | **Duration:** ~50s

Content budget (max 5 items visible):
- Title card with intro animation
- Number line with two intervals: "walking" metaphor
- Question text
- Visual of disconnected space (two blobs)

Flow:
1. play_intro("Connectedness", "Topology")
2. Number line split into two intervals with a gap
3. "Can you walk from one interval to the other?" question
4. Key insight: some spaces can be split, others cannot

### Scene 2: Formal Definition of Connectedness (~60s)
**Narration word count:** ~150 words | **Duration:** ~60s

Content budget:
- Definition text
- Formal MathTex definition
- Visual example: connected space (single blob) vs disconnected (two blobs)
- Clopen set explanation

Flow:
1. Section divider: "Connectedness"
2. Intuition: "cannot be split into two non-empty open sets"
3. Formal definition: A ⊆ X is connected if A ∩ U and A ∩ (X\U) are empty for all proper clopen U
4. Simpler form: no non-empty proper subset is both open and closed
5. Visual: two separated regions vs one connected region

### Scene 3: Examples — Connected and Disconnected Spaces (~70s)
**Narration word count:** ~175 words | **Duration:** ~70s

Content budget:
- Example 1: [0,1] is connected (animated interval)
- Example 2: (0,1) ∪ (2,3) is disconnected (two intervals with gap)
- Example 3: R is connected (whole line)
- Example 4: Q (rationals) with subspace topology is disconnected
- Each example: show the space, explain why connected/disconnected

Flow:
1. Section divider: "Examples"
2. [0,1] — animate the interval, note any split must be by open sets
3. (0,1) ∪ (2,3) — animate the split, show the clopen partition
4. R — connected (can't split the real line with open sets)
5. Q with subspace topology — disconnected (rationals below and above any irrational form a clopen partition)

### Scene 4: Connected Components (~50s)
**Narration word count:** ~125 words | **Duration:** ~50s

Content budget:
- Definition of connected component
- Visual: space broken into components (colored differently)
- Key properties text

Flow:
1. Section divider: "Connected Components"
2. "Every space can be partitioned into maximal connected pieces"
3. Visual: space with several blobs, each colored differently
4. Definition: connected component = maximal connected subset
5. Properties: equivalence classes under the relation "x ~ y if x and y lie in a connected subset"

### Scene 5: Path-Connectedness (~60s)
**Narration word count:** ~150 words | **Duration:** ~60s

Content budget:
- Definition of path
- Definition of path-connected
- Visual: animated path from point A to point B
- Comparison text: path-connected vs connected

Flow:
1. Section divider: "Path-Connectedness"
2. "A stronger notion: connected by a continuous path"
3. Definition: γ: [0,1] → X with γ(0) = a, γ(1) = b
4. Animated path drawing from a to b
5. Path-connected ⟹ connected (every path-connected space is connected)

### Scene 6: The Topologist's Sine Curve (~70s)
**Narration word count:** ~175 words | **Duration:** ~70s

Content budget (the "aha moment"):
- The curve visualization: sin(1/x) for x > 0, plus the vertical segment at x = 0
- The two parts drawn separately then together
- Key text: "Connected but NOT path-connected"
- Explanation of why

Flow:
1. Section divider: "A Remarkable Example"
2. Draw sin(1/x) for x > 0 — oscillates infinitely as x → 0
3. Add the vertical segment {(0,y) : -1 ≤ y ≤ 1}
4. The whole set is connected (the vertical segment is in the closure of the curve)
5. But NOT path-connected (no continuous path from a point on the vertical segment to a point on the curve — would require infinite oscillation in finite time)
6. Key takeaway: path-connected ⟹ connected, but NOT conversely

### Scene 7: Summary and Connections (~40s)
**Narration word count:** ~100 words | **Duration:** ~40s

Content budget:
- Summary table or comparison
- Key takeaway text
- Preview of next topic

Flow:
1. Section divider: "Summary"
2. Connected: no clopen partition
3. Path-connected: continuous path between any two points
4. path-connected ⟹ connected (converse fails — topologist's sine curve)
5. Connected components = maximal connected pieces
6. play_outro()

---

## Production Notes
- Total estimated duration: 50+60+70+50+60+70+40 = 400s ≈ 6.7 minutes narration
- With wait times and animations: ~12 minutes
- Key visual: topologist's sine curve (Scene 6) — this is the centerpiece
- Color code: SECONDARY for connected, RED for disconnected, ACCENT for paths
- Use MathTex raw strings with single backslashes throughout
