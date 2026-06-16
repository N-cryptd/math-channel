# Math Channel — Video Improvement Tracker

Tracks which videos have been analyzed and improved with v2 quality standards.

## Quality Standards (v2)
- [x] LayoutEngine v2 with 5-item content budget
- [x] Progressive reveal (items appear one by one)
- [x] Source Sans 3 font (not Menlo for body)
- [x] Dot grid background + radial gradient
- [x] Sequential narration timeline (no amix overlap)
- [x] Section dividers between concepts
- [x] Animation variety (≥2 types per scene)
- [x] play_intro() / play_outro() branding
- [x] TTS gap enforcement (0.3s min)

## Improvement Status

### Calculus I/II (scripts/pre-university/) — OLD PIPELINE
All 24 videos need improvement. They use old templates without progressive_reveal,
content budgets, or proper narration timing.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 01 | Tangent Problem | 563 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets |
| 02 | Power Rule | 436 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, fixed narration timing |
| 03 | Product/Quotient | 483 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, area model simplified |
| 04 | Chain Rule | 367 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split examples into separate scenes |
| 05 | Implicit/Related | 419 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, split ladder/ripple into separate scenes |
| 06 | Exp/Log | 357 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split graph scene from definition scene |
| 07 | Trig Derivatives | 273 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split special limits into 2 scenes |
| 08 | MVT Applications | 226 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, simplified visual scenes |
| 09 | Concavity | 246 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, two_columns comparison |
| 10 | Curve Sketching | 248 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, split analysis into separate scene from setup |
| 11 | L'Hôpital | 286 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, split examples into separate scenes, split caveat from rule |
| 12 | Intro Integration | 319 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, split FTC into sub-scenes, simplified Riemann animation |
| 13 | Antiderivatives | 229 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, formula_box for key rules |
| 14 | U-Substitution | 267 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, split examples into separate scenes |
| 15 | Integration by Parts | 244 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, LIATE as progressive_reveal, formula_box for key formula |
| 16 | Applications | 241 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, split examples from definitions, formula_box for key formulas |
| 17 | Sequences | 306 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, split 2nd example into separate scene |
| 18 | Series | 348 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split number-line into separate sub-scene, split harmonic from divergence test |
| 19 | Convergence Tests | 387 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split direct+limit comparison into 2 scenes, split ratio example into separate scene, split absolute/conditional into sub-scenes, progressive_reveal recap |
| 20 | Power Series | 397 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split operations into sub-scenes, split radius visual from formula, progressive_reveal recap |
| 21 | Taylor/Maclaurin | 356 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split formula from intuition, split Maclaurin into definition+how-to, split remainder from inequality, progressive_reveal essential series and recap |
| 22 | Parametric | 328 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split advantages into separate scene, split first/second derivatives, split arc length, split famous curves examples, progressive_reveal recap |
| 23 | Polar | 351 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split conversion into 2 scenes, split area from arc length, split area example into separate scene, progressive_reveal recap |
| 24 | Calc II Review | 327 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, two_columns for parametric/polar, split exam strategy from common mistakes, split closing from Calc III preview, content budgets |

### Linear Algebra (scripts/undergraduate/) — NEW PIPELINE
Videos 25-40 created with v2 templates. Videos 25-29 received targeted improvements. Videos 30-40 verified v2-compliant at creation.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 25 | What is a Vector? | 598 | YES | YES | YES | v2 rewrite: setup_background, SANS font, progressive_reveal, section_divider, formula_box, split crowded scenes into sub-scenes, content budgets enforced |
| 26 | Linear Combinations | 657 | YES | YES | YES | v2 rewrite: setup_background, SANS font, progressive_reveal, section_divider, formula_box, split scene2/5/6/7 into sub-scenes, content budgets |
| 27 | Matrices as Trans. | 854 | YES | YES | YES | v2 rewrite: setup_background, SANS font, progressive_reveal, section_divider, formula_box, split 9→15 sub-scenes, content budgets |
| 28 | Matrix Multiplication | 882 | YES | YES | YES | v2 targeted fix: SANS font (21 replacements), progressive_reveal in summary, ly.title() for summary, already had setup_background |
| 29 | Determinants | 747 | YES | YES | YES | v2 targeted fix: SANS font (20 replacements), progressive_reveal in summary, ly.title() for summary, already had setup_background |
| 30 | Inverse Matrices | 786 | YES | N/A (already v2) | YES | Created with v2: setup_background, progressive_reveal(15), section_divider, formula_box, SANS font(15), no content .shift()/.to_edge() — no improvement needed |
| 31 | Systems of Equations | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(26), section_divider, SANS font, ly.clear — no improvement needed |
| 32 | Row Reduction | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(32), section_divider, SANS font(4), zero .shift()/.to_edge() — no improvement needed |
| 33 | Null/Column Space | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(26), section_divider, SANS font(15) — no improvement needed |
| 34 | Rank and Nullity | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(24), section_divider, SANS font(4) — no improvement needed |
| 35 | Eigenvalues | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(26), section_divider, SANS font(7) — no improvement needed |
| 36 | Diagonalization | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(18), section_divider, SANS font(4) — no improvement needed |
| 37 | Inner Product Spaces | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(23), section_divider, SANS font(5) — no improvement needed |
| 38 | Orthogonality/Gram-Schmidt | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(22), section_divider, SANS font(4) — no improvement needed |
| 39 | Linear Transformations | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(40), section_divider, SANS font(23) — no improvement needed |
| 40 | SVD | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(28), section_divider, SANS font(18) — no improvement needed |

### Calculus III + ODE (scripts/undergraduate/) — NEW PIPELINE
Videos 41+ created with v2 templates from the start.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 41 | Vectors in 3D | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(24), section_divider, SANS font(10) |
| 42 | Dot Product in 3D | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(24), section_divider, SANS font(17) |
| 43 | Cross Product in 3D | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(24), section_divider, SANS font(16) |
| 44 | Lines and Planes in 3D | 337 | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(8), section_divider(6), SANS font(15) |
| 45 | Vector-Valued Functions | — | YES | N/A (already v2) | YES | Created with v2: setup_background(2), progressive_reveal(8), section_divider(6), SANS font(14) |
| 46 | Partial Derivatives | — | YES | N/A (already v2) | YES | Created with v2: setup_background(2), progressive_reveal(2), section_divider(5), SANS font(21) |
| 47 | Gradient/Directional | — | YES | N/A (already v2) | N/A | Created with v2: setup_background(2), progressive_reveal(3), section_divider(5), SANS font(21) |
| 48 | Lagrange Multipliers | 635 | YES | YES (minor) | N/A | v2-compliant. Fixed 1 .shift() → removed. setup_bg(2), section_divider(6), SANS(16), ly.clear(11), formula_box(2) |
| 49 | Double Integrals | 536 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(1), section_divider(7), SANS(23), ly.clear(8) |
| 50 | Triple Integrals | 473 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(2), section_divider(7), SANS(22), ly.clear(8) |
| 51 | Line Integrals | 385 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(2), section_divider(6), SANS(22), ly.clear(7) |
| 52 | Green's Theorem | 380 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(2), section_divider(6), SANS(21), ly.clear(7) |
| 53 | Stokes' Theorem | 411 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(4), section_divider(6), SANS(30), ly.clear(7) |
| 54 | Divergence Theorem | 635 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(6), section_divider(7), SANS(48), ly.clear(14) |
| 55 | What is a DE? | 612 | YES | YES (minor) | YES | v2-compliant. Fixed 1 .to_edge() → clamp_position. setup_bg(2), progressive_reveal(4), section_divider(4), SANS(31), ly.clear(12) |
| 56 | Separable Equations | 668 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(2), section_divider(4), SANS(24), ly.clear(9) |
| 57 | First-Order Linear | 744 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(1), section_divider(4), SANS(16), ly.clear(6), formula_box(1), zero .shift()/.to_edge() |
| 58 | Second-Order Linear Intro | 636 | YES | N/A (already v2) | YES | Created with v2: setup_bg(2), progressive_reveal(4), section_divider(4), SANS(14), ly.clear(7), zero .shift()/.to_edge() |
| 59 | Second-Order IVPs | 570 | YES | N/A (already v2) | YES | Created with v2: setup_bg(2), progressive_reveal(3), section_divider(5), SANS(10), ly.clear(7), zero .shift()/.to_edge() |
| 60 | Non-Homogeneous Equations | 438 | YES | N/A (already v2) | YES | Created with v2: setup_bg(2), progressive_reveal(3), section_divider(4), SANS(10), ly.clear(6), zero .shift()/.to_edge() |
| 61 | Variation of Parameters | 555 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(3), section_divider(5), SANS(9), ly.clear(7), formula_box(3), zero .shift()/.to_edge() |
| 62 | Power Series Solutions | 605 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(3), section_divider(5), SANS(13), ly.clear(12), formula_box(5), zero .shift()/.to_edge() |
| 63 | Laplace Transforms | 678 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(4), section_divider(1), SANS(14), ly.clear(9), zero .shift()/.to_edge() |
| 64 | Systems of ODEs | 771 | YES | YES (shortened) | YES | Script shortened from 830→771 lines (reduce wait times, remove TracedPath). Narrated. 2:23 duration. |
| 65 | Phase Portraits | 586 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(4), section_divider(6), SANS(24), ly.clear(8), zero .shift()/.to_edge() for content. next_to only on axis labels. |
| 66 | Numerical Methods | 523 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(4), section_divider(5), SANS(18), MONO(3, table), ly.clear(8), zero .shift()/.to_edge() for content. next_to only on axis labels. |
| 67 | Probability Spaces | 790 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(3), section_divider(6), SANS(19), ly.clear(16), formula_box(5). Minor: 2 next_to+shift on axis labels (acceptable for shapes). Zero content .shift()/.to_edge(). |
| 68 | Conditional Probability | 649 | YES | YES (minor) | N/A | v2-compliant. Fixed 5 .shift()/.to_edge()/next_to → safe_place/move_to. 3 self.remove() → FadeOut. Added formula_box for core definition. setup_bg(2), section_divider(5), SANS(19), ly.clear(7), progressive_reveal(1). |

### Probability & Statistics (scripts/undergraduate/) — NEW PIPELINE
Videos 67+ created with v2 templates from the start.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 67 | Probability Spaces | 790 | YES | N/A (already v2) | N/A | Created with v2: competitive analysis done, plan+script+render. 3:45 duration. |

## Improvement Process
1. **Analyze** — Read script, check against v2 quality standards, score each dimension
2. **Competitive check** — See channel-analysis/improvements.md for topic insights
3. **Rewrite** — Update script to use LayoutEngine v2, progressive_reveal, proper narration
4. **Re-render** — Produce new 480p15 narrated video
5. **Verify** — Check output file exists and plays correctly
6. **Track** — Update this file and PLANNING_STATE.md

## Status: COMPLETE ✓
All 68 existing videos have been analyzed. Videos 1-29 received v2 rewrites. Videos 30-47 were created with v2 standards and verified compliant. Videos 48-57 analyzed and verified v2-compliant (minor fixes to 48 and 55). Videos 58-63 analyzed and verified v2-compliant. Re-render tasks for Videos 1-29 completed. Video 55 re-rendered after minor fix (.to_edge() → clamp_position). Videos 65-66 analyzed and verified v2-compliant (created with v2). Videos 67-68 analyzed (67 verified v2-compliant, 68 received minor fixes: 5 positioning violations fixed, 3 self.remove→FadeOut, formula_box added).

## Last Updated
2026-06-16 (Video 68 improved: fixed 5 .shift()/.to_edge()/next_to violations, added formula_box, replaced self.remove() with FadeOut. Videos 65-67 analyzed and verified v2-compliant.)
