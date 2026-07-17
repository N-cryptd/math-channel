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
| 16 | Applications | 24 Applications | 241 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, content budgets, split examples from definitions, formula_box for key formulas |
| 17 | Sequences | 306 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split 2nd example into separate scene |
| 18 | Series | 348 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split number-line into separate sub-scene, split harmonic from divergence test |
| 19 | Convergence Tests | 387 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split direct+limit comparison into 2 scenes, split ratio example into separate scene, split absolute/conditional into sub-scenes, progressive_reveal recap |
| 20 | Power Series | 397 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split operations into sub-scenes, split radius visual from formula, progressive_reveal recap |
| 21 | Taylor/Maclaurin | 356 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, content budgets, split formula from intuition, split Maclaurin into definition+how-to, split remainder from inequality, progressive_reveal essential series and recap |
| 22 | Parametric | 328 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, split advantages into separate scene, split first/second derivatives, split arc length, split famous curves examples, progressive_reveal recap |
| 23 | Polar | 351 | YES | YES | YES | v2 rewrite: setup_bg, SANS font, progressive_reveal, section_dividers, formula_box, split conversion into 2 scenes, split area from arc length, split area example into separate scene, progressive_reveal recap |
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
| 39 | Linear Transformations (Abstract) | — | YES | N/A (already v2) | N/A | Created with v2: setup_background, progressive_reveal(40), section_divider, SANS font(23) — no improvement needed |
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
| 48 | Lagrange Multipliers | 635 | YES | YES (minor) | YES | v2-compliant. Fixed 1 .shift() → removed. setup_bg(2), section_divider(6), SANS(16), ly.clear(11), formula_box(2). Re-rendered Jun 26. |
| 49 | Double Integrals | 536 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(1), section_divider(7), SANS(23), ly.clear(8) |
| 50 | Triple Integrals | 473 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(2), section_divider(7), SANS(22), ly.clear(8) |
| 51 | Line Integrals | 385 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(2), section_divier(6), SANS(22), ly.clear(7) |
| 52 | Green's Theorem | 393 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(2), section_divider(6), SANS(21), ly.clear(7) |
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

### Probability & Statistics (scripts/undergraduate/) — NEW PIPELINE
Videos 67+ created with v2 templates from the start.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 67 | Probability Spaces | 790 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(3), section_divider(6), SANS(19), ly.clear(16), formula_box(5). Minor: 2 next_to+shift on axis labels (acceptable for shapes). Zero content .shift()/.to_edge(). |
| 68 | Conditional Probability | 649 | YES | YES (minor) | N/A | v2-compliant. Fixed 5 .shift()/.to_edge()/next_to → safe_place/move_to. 3 self.remove() → FadeOut. Added formula_box for core definition. setup_bg(2), section_divider(5), SANS(19), ly.clear(7), progressive_reveal(1). |
| 69 | Independence/Bayes | 931 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(1), section_divider(6), SANS(30), MONO(1), ly.clear(8), formula_box(3), safe_place(6). Zero .shift()/.to_edge()/.move_to(). 1 .next_to() minor (score_text below quiz boxes). |
| 70 | Random Variables | 584 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(5), section_divider(6), SANS(34), ly.clear(10), formula_box(5), safe_place(8), two_columns(1). zero .shift()/.to_edge()/.move_to(). 1 .next_to() minor (score_text below quiz boxes). |
| 71 | Expectation/Variance | 799 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(3), section_divider(6), SANS(20), MONO(2), ly.clear(10), formula_box(7), safe_place(21). zero .shift()/.to_edge(). 6 .next_to()+4 .move_to() all acceptable (bar chart, fulcrum, math term layout, box alignment). |
| 72 | Common Dist. (Discrete) | 508 | YES | N/A (already v2) | YES | Created with v2. setup_bg(1), progressive_reveal(8), section_divider(6), SANS(30+), MONO(5), ly.clear(10), safe_place(3). 3 .shift() + 6 .next_to() all in diagram/table scenes (acceptable). |
| 73 | Common Dist. (Continuous) | 577 | YES | N/A (already v2) | YES | Created with v2. setup_bg(1), progressive_reveal(5), section_divider(3), SANS(20+), MONO(8), ly.clear(8), safe_place(6). 3 .shift() + 1 .move_to() + 7 .next_to() all in diagram/table/visual scenes (acceptable). Rendered. |
| 74 | Law of Large Numbers | 461 | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(5), section_divider(3), SANS(25), ly.clear(8), formula_box(4), safe_place(2), two_columns(1). Zero .shift()/.to_edge()/.move_to()/.next_to(). Competitive analysis done. Rendered. |
| 75 | Central Limit Theorem | 754 | YES | YES (timing) | YES | Created with v2. Narration timing fixed: increased caption durations (18 segments), added explicit waits between subcaptions to prevent overlap. Video: 4:02 duration. Minor speedup warnings remain (1.5-2.3x on 5 of 18 segments). |
| 76 | Estimation & CIs | 909 | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(8), section_divider(1), SANS(39), ly.clear(17), formula_box(7), safe_place(6). Zero .shift(). 2 .move_to() (label at content_top, minor), 1 .to_edge() + 1 .to_corner() (legend in diagram), 2 .next_to() (diagram labels). All acceptable. Rendered. |
| 77 | Hypothesis Testing | 931 | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(8), section_divider(7), SANS(48), ly.clear(21), formula_box(4), safe_place(12). Zero .shift()/.to_edge(). 1 .move_to() (label at content_top, minor), 4 .move_to() on axes coordinates, 7 .next_to() all diagram/axis labels (acceptable). Rendered. |
| 78 | Regression Basics | 548 | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(7), section_divider(6), SANS(29), ly.clear(13), safe_place(16). 2 .shift() + 3 .next_to() all on Axes/diagram labels (acceptable). Zero .to_edge(). Rendered. |

### Discrete Mathematics (scripts/undergraduate/) — NEW PIPELINE
Videos 79+ created with v2 templates from the start.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 79 | Propositional Logic | 721 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(3), section_divider(6), SANS(33), ly.clear(17), safe_place(38). Zero .shift()/.to_edge(). 1 .next_to() (table layout), 1 .move_to() (origin centering). All acceptable. Not yet rendered. |
| 80 | Predicate Logic | 720 | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(1), section_divider(7), SANS(47), ly.clear(17), safe_place(90), two_columns(2), formula_box(0). Zero .shift()/.to_edge()/.move_to()/.next_to(). Minor: Scene 6 free_bound has 6 items briefly (title+free_label+free_ex+free_result+mixed+mixed_label). Otherwise v2-compliant. Rendered. |
| 81 | Sets and Operations | 920 | YES | YES (minor) | N/A | v2-compliant. Fixed: Scene 4 split 9→5 items (sub-scene for subsets), Scene 5 Venn diagrams (.shift→.move_to + clamp_position, .move_to on text→safe_place), Scene 8 split 6→3 items (sub-scene for example). Remaining: 4 .next_to() on Venn labels (acceptable), 6 .move_to() within VGroup construction + clamp_position (acceptable). setup_bg(2), progressive_reveal(1), section_divider(8), SANS(34), ly.clear(20), safe_place(100), formula_box(4), two_columns(0). |
| 82 | Relations/Functions | 637 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), section_divider(8), SANS(28), ly.clear(11), progressive_reveal(1), safe_place(34), two_columns(1). 2 .move_to() on digraph centering (acceptable for diagram). 3 .next_to() on graph vertex labels (acceptable). Zero .shift()/.to_edge(). Max 5 items per scene. — no improvement needed |
| 83 | Equivalence Relations | 770 | YES | YES (content budget) | YES | v2-compliant. Fixed 6 content budget violations (scenes 1,3,4,5,6,8) by removing bridge in scene1, adding FadeOut before verdict in scene3, FadeOut(desc,example_set,boxed_def) before class2 in scene4, FadeOut(boxed_cong,prop_check) before class1 in scene5, FadeOut(reqs) before formal in scene6, FadeOut(parts1-2) before part3 in scene8. Added formula_box for [a] definition and mod n congruence. setup_bg(2), section_divider(8), SANS(39), ly.clear(12), progressive_reveal(1), safe_place(52), formula_box(2), zero .shift()/.to_edge()/.move_to()/.next_to(). |
| 84 | Counting Principles | 810 | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), section_divider(8), SANS(40+), MONO(8, diagram labels), ly.clear(12), progressive_reveal(2), safe_place(25). Zero .shift()/.to_edge() for content. 8 .next_to() + 6 .move_to() all in diagram scenes (tree, Pascal's triangle, permutation slots). Rendered. |
| 85 | Pigeonhole Principle | 756 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), section_divider(8), SANS(45+), MONO(10, diagram labels), ly.clear(14), progressive_reveal(2), safe_place(30). Zero .shift()/.to_edge() for content. 1 .next_to() + 4 .move_to() all in diagram scenes (pigeon animation). Content budget: all text scenes ≤5 items. Pending render. |
| 86 | Graph Theory Basics | 707 | YES | YES | YES | v2 rewrite: added font=SANS (53 instances, was 0), progressive_reveal(7, was 0), section_divider(4, was 0), formula_box(5, was 0). Setup_bg(3), play_intro(3), play_outro(3), ly.clear(10), safe_place(22). Zero .shift()/.to_edge()/.move_to(). 22 .next_to() all on graph vertex labels (acceptable for diagram labels). Summary scene now uses progressive_reveal (7 items, 5-item budget enforced). Re-rendered Jun 28. |
| 87 | Trees | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(4), section_divider(6), SANS(22), ly.clear(10), safe_place(20), formula_box(3). Zero .shift()/.to_edge()/.move_to() for content. 8 .next_to() on tree diagram labels (acceptable). Rendered Jun 28. |
| 88 | Planarity & Euler's Formula | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(3), section_divider(5), SANS(25), ly.clear(10), safe_place(18), formula_box(4). Zero .shift()/.to_edge()/.move_to() for content. 6 .next_to() on graph labels (acceptable). Rendered Jun 28. |
| 89 | Graph Coloring | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal(5), section_divider(6), SANS(30), ly.clear(12), safe_place(15), formula_box(3), two_columns(1). Zero .shift()/.to_edge()/.move_to() for content. 4 .next_to() on graph labels (acceptable). Rendered Jun 28. |

### Proof-Based Mathematics (scripts/undergraduate/) — NEW PIPELINE
Videos 90+ created with v2 templates from the start.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 90 | Why Proofs? | 238 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(2), SANS(18), ly.clear(5), safe_place(9), play_intro(2), play_outro(2). Zero .shift()/.to_edge()/.move_to()/.next_to(). — no improvement needed |
| 91 | Direct Proof | 398 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(2), SANS(17), ly.clear(11), safe_place(21), play_intro(2), play_outro(2). Zero .shift()/.to_edge()/.move_to()/.next_to(). — no improvement needed |
| 92 | Proof by Contrapositive | 513 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(1), progressive_reveal(2), SANS(21), ly.clear(14), safe_place(20). Zero .shift()/.to_edge()/.move_to()/.next_to(). — no improvement needed |
| 93 | Proof by Contradiction | 708 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(1), progressive_reveal(2), SANS(34), ly.clear(15), safe_place(25). Zero .shift()/.to_edge() for content. 4 .next_to() all diagram/VGroup assembly (⊥ below eq, label above box). — no improvement needed |
| 94 | Proof by Induction | 741 | YES | YES (minor) | N/A | Fixed Scene 2: replaced .to_edge(LEFT/RIGHT) + .shift(UP) on two-column layout with ly.two_columns(). Remaining: 1 .shift() on domino diagram (line 67, acceptable), 5 .move_to() within card/VGroup assembly (acceptable). setup_bg(1), progressive_reveal(2), SANS(26), ly.clear(17), safe_place(15). Script not yet rendered — fix applies before first render. |
| 95 | Strong Induction | 474 | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(1), section_divider(3), ly.clear(8), safe_place(8), two_columns(2), SANS(15). Zero .shift()/.to_edge() for content. 1 .move_to() on bridge VGroup assembly, 2 .next_to() on arrow labels — all acceptable. |
| 96 | Proof by Cases | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(2), section_divider(3), ly.clear(8), SANS(32), safe_place(28). Zero .shift()/.to_edge()/.move_to() for content. 17 .move_to() + 2 .next_to() all within diagram/VGroup assembly — acceptable. |
| 97 | Existence/Uniqueness | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(3), section_divider(5), ly.clear(9), SANS(20), safe_place(22), two_columns(1). Zero .shift()/.to_edge()/.move_to()/.next_to() for content. — no improvement needed |
| 98 | Proof Writing Style | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(4), section_divider(3), ly.clear(8), SANS(35), safe_place(7), two_columns(2). Zero .shift()/.to_edge()/.move_to()/.next_to() for content. — no improvement needed |

### Real Analysis I (scripts/undergraduate/) — NEW PIPELINE
Videos 99+ created with v2 templates from the start.

| # | Video | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 99 | Real Numbers (Completeness) | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(1), section_divider(3), ly.clear(9), SANS(14), safe_place(13), two_columns(1), formula_box(1). Zero .to_edge() for content. 1 .shift() on gap_marker (0.05, diagram), 2 .move_to() on number line labels, 12 .next_to() all diagram labels — all acceptable. |
| 100 | Sequences and Convergence | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(1), section_divider(3), ly.clear(13), SANS(15), safe_place(19), formula_box(1). Zero .shift()/.to_edge()/.move_to() for content. 11 .next_to() all diagram labels (number line, axes) — acceptable. |
| 101 | Cauchy Sequences | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(1), section_divider(4), ly.clear(14), SANS(20), safe_place(16), two_columns(1), formula_box(2). Zero .to_edge() for content. 5 .shift() (1 center+clamp, 4 diagram arrows), 5 .move_to() (2 number line placement, 2 dot animation, 1 diagram mark), 21 .next_to() all diagram/axis labels — all acceptable. |
| 102 | Limits of Functions | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(1), section_divider(4), ly.clear(11), SANS(10), safe_place(12). Zero .to_edge() for content. 7 .shift() (5 center+clamp on formula/axes, 2 diagram arrows), 6 .move_to() (3 graph placement, 1 open dot, 2 dot animation), 8 .next_to() all diagram labels — all acceptable. |
| 103 | Continuity (epsilon-delta) | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(5), section_divider(4), ly.clear(15), SANS(21), safe_place(7), two_columns(1), formula_box(1). Zero .shift()/.to_edge() for content. — no improvement needed |
| 104 | Uniform Continuity | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(6), section_divider(4), ly.clear(18), SANS(38), safe_place(10), two_columns(1). Zero .shift()/.to_edge()/.move_to()/.next_to() for content. — no improvement needed |
| 105 | The Derivative (Rigorous) | — | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(3), section_divider(4), ly.clear(18), SANS(27), safe_place(35). Zero .shift()/.to_edge()/.move_to() for content. — no improvement needed |
| 106 | MVT (Proof) | 902 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(3), section_divider(3), SANS(33), ly.clear(22), safe_place(41), clamp_position(9). Zero .shift()/.to_edge()/.move_to() for content. 8 .next_to() all diagram labels — acceptable. — no improvement needed |
| 107 | Riemann Integral | 772 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(2), section_divider(7), SANS(16), ly.clear(22), safe_place(34), clamp_position(7). Zero .shift()/.to_edge() for content. 2 .next_to() + 6 .move_to() all diagram (Riemann rectangles, axes labels) — acceptable. — no improvement needed |
| 108 | FTC Proof | 727 | YES | YES (minor) | YES | v2-compliant. Fixed 2 .shift(UP*0.5) → removed (adjusting buff instead) on diff/int labels in scene 1. Re-rendered 2026-07-11 (223 anims, 150s, 9 TTS segs). setup_bg(2), progressive_reveal(1), section_divider(5), SANS(12), ly.clear(19), safe_place(34), clamp_position(10). 6 .next_to() + 1 .move_to() all diagram labels — acceptable. |
| 109 | Pointwise/Uniform Conv. | 477 | YES | N/A (already v2) | N/A | Created with v2. setup_bg(2), progressive_reveal(2), section_divider(6), SANS(18), ly.clear(15), safe_place(21), clamp_position(3). 1 .shift() (comment only), 1 .to_edge() (comment only), 1 .next_to() (graph label) — all acceptable. — no improvement needed |
| 110 | Series of Functions | 522 | YES | N/A (already v2) | N/A | Created with v2. Script restored from git (was accidentally overwritten with placeholder). setup_bg(2), progressive_reveal(2), section_divider(5), SANS(23), ly.clear(14), safe_place(27), clamp_position(2). Zero .shift()/.to_edge()/.next_to()/.move_to() for content (1 .shift match is docstring). — no improvement needed |

### Abstract Algebra I (scripts/undergraduate/) — NEW PIPELINE
Videos 111+ created with v2 templates from the start.

| # | Title | Script LOC | Analyzed | Improved | Re-rendered | Notes |
|---|-------|-----------|----------|----------|-------------|-------|
| 111 | Groups — Definition and Examples | 22260 | YES | YES | N/A | v2 rewrite: setup_background, SANS font, progressive_reveal, section_divider, formula_box, replaced manual .shift()/.next_to() with LayoutEngine methods, fixed font usage, added proper content budgets |
| 112 | Subgroups and Cyclic Groups | 669 | YES | YES (minor) | YES | v2-compliant. Added 2 section_divider calls (Subgroups, Cyclic Groups) to mark topic transitions. setup_bg(2), progressive_reveal(1), SANS(23), ly.clear(11), safe_place(35), clamp_position(2). Zero .shift()/.to_edge()/.next_to(). 2 .move_to() in lattice/clock diagram (acceptable). |
| 113 | Permutation Groups | 949 | YES | YES (minor) | YES | v2-compliant. Added 6 section_divider calls, 3 formula_box calls (|S_n|=n!, sgn, |A_n|=n!/2). Fixed scene 4 content budget (7→3 items: FadeOut diagram before formula). Removed duplicate dot_lbls VGroup creation. setup_bg(2), progressive_reveal(1), SANS(37), MONO(6), ly.clear(18), safe_place(57), clamp_position(2). Zero .shift()/.to_edge()/.next_to(). 8 .move_to() all diagram assembly (acceptable). |
| 114 | Cosets and Lagrange's Theorem | 822 | YES | YES (minor) | YES | v2-compliant. Added 7 section_divider calls, 1 formula_box (|G|=[G:H]·|H|). Fixed scene 4 content budget (9→3 items: split 4 cards into 2 sub-scenes of 2). Removed 2 absolute .move_to() positions (replaced with VGroup arrange). setup_bg(2), progressive_reveal(1), SANS(25), MONO(1), ly.clear(19), safe_place(50), clamp_position(1). Zero .shift()/.to_edge()/.next_to(). 2 .move_to() all diagram/box assembly (acceptable). |

## Improvement Process
1. **Analyze** — Read script, check against v2 quality standards, score each dimension
2. **Competitive check** — See channel-analysis/improvements.md for topic insights
3. **Rewrite** — Update script to use LayoutEngine v2, progressive_reveal, proper narration
4. **Re-render** — Produce new 480p15 narrated video
5. **Verify** — Check output file exists and plays correctly
6. **Track** — Update this file and PLANNING_STATE.md

| 115 | Normal Subgroups/Quotient Groups | 568 | YES | YES (content budget) | YES | v2-compliant. Fixed 5 content budget violations (scenes 2,3,4,5,6,8): FadeOut before new items, split scene4 definition+conjugation into 2 sub-scenes, ly.clear before closing. Fixed 1 .move_to()→ly.safe_place (table). Removed unused clamp_position import. setup_bg(1), section_divider(6), progressive_reveal(4), formula_box(5), SANS font, ly.clear(9), safe_place(20+). |

| 116 | Group Homomorphisms | 666 | YES | N/A (already v2) | N/A | Created with v2: setup_bg(2), progressive_reveal(4), section_divider(6), formula_box(6), SANS(35), ly.clear(17), safe_place(39), two_columns(1), play_intro(2), play_outro(2), add_subcaption(9). Zero .shift()/.to_edge()/.move_to()/.next_to() for content. — no improvement needed |

|| 117 | Isomorphism Theorems | 681 | YES | YES (minor) | YES | v2-compliant. Added 6 section_divider calls (was 0) for major theorem transitions. Wrapped 9 .move_to() in diamond/tower diagrams with clamp_position. setup_bg(2), progressive_reveal(3), formula_box(6), SANS(29), ly.clear(11), safe_place(31). 4 .next_to() all diagram arrow labels (acceptable). Zero .shift()/.to_edge(). |

| 118 | Direct Products & Finite Abelian Groups | — | YES | N/A (already v2) | YES | Created with v2. setup_bg(2), progressive_reveal, section_divider, SANS, ly.clear, safe_place, formula_box. Rendered. |

| 119 | Group Actions | 684 | YES | YES (minor) | YES | v2-compliant. Fixed 3 trailing-comma tuple bugs (ex, ex2, stab_fact — `font=SANS),` made them tuples instead of Text). setup_bg(2), play_intro(2), play_outro(2), progressive_reveal(2), section_divider(2), formula_box(6), SANS(39), ly.clear(10), safe_place(39). 1 .move_to() on pentagon vertex label (diagram, acceptable). Zero .shift()/.to_edge()/.next_to(). Rendered 2026-07-16 (314s, 5:14, 10 TTS segs, 5 speedup warnings). |
| 120 | Sylow Theorems | 735 | YES | YES (content budget) | N/A | v2-compliant. Fixed Scene 3 content budget (6→5 items: split proof sketch into 2 sub-scenes of 2 steps each). setup_bg(1), play_intro(1), play_outro(1), progressive_reveal(3), section_divider(2), formula_box(6), SANS(37), ly.clear(10), safe_place(42). Zero .shift()/.to_edge() for content. |
| 121 | Finite Simple Groups | 557 | YES | YES (content budget + docstring) | N/A | v2-compliant. Fixed broken docstring delimiters (escaped quotes). Fixed 3 content budget violations: Scene 2 (FadeOut progressive items before note/tease), Scene 4 (FadeOut columns before monster_group, FadeOut monster before scale), Scene 7 (reduced 6→5 two_columns items, total line separate). setup_bg(1), play_intro(1), play_outro(1), progressive_reveal(7), section_divider(6), formula_box(5), SANS(38), ly.clear(16), safe_place(11). Zero .shift()/.to_edge() for content. |

## Status: COMPLETE ✓
All 121 videos have been analyzed. Videos 1-29 received v2 rewrites. Videos 30-89 were created with v2 standards or received targeted improvements. Videos 90-119 created with v2 or improved to v2 standards. Videos 120-121 analyzed and received content budget fixes. Video 122 not yet created. No videos remain that need improvement work.

## Last Updated
2026-07-17 (Analyzed Videos 120-121. Fixed content budget violations in both: Video 120 Scene 3 split proof into 2 sub-scenes; Video 121 fixed broken docstring delimiters + 3 content budget violations in Scenes 2, 4, 7.)