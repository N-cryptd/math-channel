# Video 274: Exponents — Plan

**Playlist:** Numbers & Arithmetic (Foundations track), curriculum row 9
**Class:** `Video274_Exponents` → `scripts/foundations/video-274-exponents.py`
**Target:** 10–13 min (competitive analysis window; curriculum est. 12 min)
**YouTube title (double-keyword, Mr. J pattern):** "What are Exponents? | Powers, Zero, and Negative Exponents Explained"

## Competitive analysis inputs (complete 2026-09-09, improvements.md)

Pattern-first spine per analysis technique #3: build-up → division pattern → laws as
consequences (NOT named rules to memorize — direct differentiation from TOCT's
memorization-first format). Khan's 2008 "negative exponent intuition" (successive
division by the base → 2⁰=1, then 2⁻ⁿ) is the single most relevant structural idea in
the space (498K views, 16 years old, never modernized with real animation) — our
animated ladder is that video, rebuilt. Math Antics' laws video outperformed their
intro (3.8M vs 2.1M) so the laws-as-consequences material gets real screen time.
Serial continuity: opens on 273's place-value columns ("the powers of ten marching
past the ones place"), money callback (273's money habitat), closes with the
roots-and-radicals doorway (row 10).

## Thumbnail recipe (analysis technique #1)

BG #1A1832 + one giant `2⁵` in MONO with the exponent digit in ACCENT #FFD166,
dot-grid texture, ≤2 elements total. Dark+yellow-accent = the winning trend in this
niche; avoid the pure-black formula-screenshot look (only works at 10M-sub authority).

## Description SEO (TOCT playbook)

Chaptered description listing each law with its formula (a⁰=1, a⁻ⁿ=1/aⁿ,
aᵐ·aⁿ=aᵐ⁺ⁿ, aᵐ/aⁿ=aᵐ⁻ⁿ, (aᵐ)ⁿ=aᵐⁿ) + next-video link to Roots and Radicals.

## Scenes (12 scenes, one narration caption each, ~10.5 min target)

| # | Scene | Beat | Budget (≤5 visible) |
|---|-------|------|---------------------|
| 1 | hook | Penny doubled daily 30 days vs $1M — explosive growth question. Serial open on 273's columns. | intro + title + deal line + chain + final amount |
| 2 | notation | 2×2×2 → 2³ transform; base/exponent labels; 2⁵=32 | title + expanded + exponential + 2 labels |
| 3 | names | squared/cubed/nth; reps 3⁴=81, 10⁴=10,000; trap 2⁵≠2×5 | title + 3 rows + name line |
| 4 | growth | powers-of-2 chain ×2 each step; add-vs-double contrast | title + chain + note |
| 5 | down-ladder | THE division pattern: 2⁵→2¹, ÷2 every rung, "?" at bottom | title + 5-row ladder + ? |
| 6 | zero power | land 2⁰=1; any nonzero base → a⁰=1 (formula_box) | title + mini-ladder + formula |
| 7 | negative | keep dividing: 2⁻¹=1/2, 2⁻²=1/4; a⁻ⁿ=1/aⁿ; reciprocal note | title + ladder + formula + note |
| 8 | product | 2²×2³ expand & count copies → 2⁵; aᵐaⁿ=aᵐ⁺ⁿ | title + row + count note + formula |
| 9 | quotient | 2⁵/2²=2³; 2⁵/2⁵=2⁰=1 (zero power explained twice) | title + 2 eqs + formula |
| 10 | power of power | (2²)³ expand clusters → 2⁶; (aᵐ)ⁿ=aᵐⁿ; count-copies meta-rule | title + row + note + formula |
| 11 | habitat | place value = powers of ten (273 callback); m²/m³; 2¹⁰=1024; roots teaser | title + 3 rows + teaser |
| 12 | summary | one map: counting label / ladder / three consequences; outro → Roots and Radicals | title + 3 lines + play_outro |

Animation vocabulary: titles→Write, body→FadeIn(shift=LEFT*0.15), formulas→Write/
Transform, ladders fade in rung by rung. All positioning via LayoutEngine
(title/safe_place/center_in_content/stack_down/formula_box/section_divider).
Scene dividers numbered 1–11 for scenes 2–12.

## Pacing (standardized cohort method, as Video 273)

1. Script written with provisional declareds; then AST full-text caption extraction
   (handles implicit string concat) from the script file.
2. Naturals measured per caption: single-clip edge-tts, voice en-US-AndrewNeural,
   rate −5%; ffprobe duration.
3. declared = natural + 0.7 (2 dp).
4. Block-final wait bumps: every caption slot ≥ natural + 1.0 (target usage ≤ ~0.94).
   Slot model: section_divider 2.9s, title 0.75s, clear 0.8s, play_intro 6.2s,
   play_outro 8.0s, play(run_time=NORMAL)=1.2 / SLOW=2.0 / FAST=0.6, wait(x)=x.
   Bumps carry `# pacing:` comments.
5. py_compile after every edit pass.

## Handoff

Compile-clean + pacing-aligned script is handed to the produce stage:
`bash templates/produce.sh Video274_Exponents ql` (480p15 draft), then verify chain
(SRT slot math, central log zero events, volumedetect, dot QA) per the cohort recipe.
