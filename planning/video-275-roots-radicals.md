# Video 275: Roots and Radicals — Plan

**Playlist:** Numbers & Arithmetic (Foundations track), curriculum row 10
**Class:** `Video275_RootsRadicals` → `scripts/foundations/video-275-roots-radicals.py`
**Target:** 10–13 min (competitive analysis window; curriculum est. 12 min)
**YouTube title (double-keyword, Mr. J pattern):** "What are Square Roots? | Radicals, Cube Roots, and Undoing Exponents Explained"

## Competitive analysis inputs (complete 2026-09-11, improvements.md)

Inverse-pair spine per analysis technique #3 (and the market gap: NO competitor
opens roots from "what undoes the exponent" — they all open definition-first,
"What times itself makes nine?"). Math Antics' most-viewed math video (2.4M,
"Exponents and Square Roots") literally chains exponents → square roots, proving
our exact serial position; their terms-after-concept ordering is adopted
(radical sign / radicand named only after the idea lands). Mr. J's 1.5M intro
confirms perfect-squares-table-first pedagogy + double-keyword titles. Domain
of Science (288K on the name alone) + our own 274 squared=area beat → the
geometry-of-the-name scene. Khan's cube-roots video (931K) covers ∛ of
negatives — adopted, plus the even/odd root asymmetry. MindYourDecisions'
cube-root mental trick is the biggest video in the entire space (15.2M) —
adapted into a "superpower" scene (∛1728 in your head). Scope check: the
simplifying-radicals technique niche (TOCT 2.7M, Mario's 1.5M, Khan 1.6M) is
Algebra-Fundamentals material — deliberately excluded, we keep foundations only.
Serial continuity: opens on 274's closing teaser ("the ladder in reverse — what
number times itself makes nine? what undoes a square?"), closes on the Real
Number Line doorway (√2 has an address between 1 and 2 — row 11).

## Thumbnail recipe (analysis technique #1)

BG #1A1832 + one giant `√9 = ?` with the radical in PRIMARY #5BC0EB and the
radicand digit in ACCENT #FFD166, dot-grid texture, ≤2 elements total. Nobody
in the niche's top set features the radical sign itself as a designed hero
object on a dark background — ours does, consistent with the winning
dark+yellow-accent trend from the 274/273 analyses.

## Description SEO (TOCT playbook)

Chaptered description listing each beat with its formula (√9=3, (√) undoes ²,
∛8=2, ∛(−8)=−2, √(−9) no real answer, x²=9 → x=±3 vs √9=3, ∛1728=12,
√(3²+4²)=5) + note that √2 is irrational + next-video link to The Real Number
Line.

## Scenes (12 scenes, one narration caption each, ~12 min target)

| # | Scene | Beat | Budget (≤5 visible) |
|---|-------|------|---------------------|
| 1 | hook | The undo: − undoes +, ÷ undoes ×; 274 built the jump — what undoes a jump? Serial open on 274's teaser. | intro + title + 2 inverse pairs + 3²=9 with ? arrow |
| 2 | meaning | √9 asks "what times itself makes 9"; 3·3=9 → √9=3; vocabulary radical sign + radicand; readings √25=5, √49=7 | title + √9=? → =3 + 2 labels |
| 3 | geometry | Why "square": area 9 grid → side 3 (the root of the square is its side); area 16 → side 4 | title + 3×3 grid + area/side labels |
| 4 | perfect squares | Two-way street 5² ⇄ √25; the ten perfect squares 1..100; roots of perfect squares are whole | title + double-arrow row + 10-square chain |
| 5 | sandwich | √10 between 3 and 4 (9<10<16); √50 between 7 and 8; pin any root without a calculator | title + sandwich rows + number-line band |
| 6 | irrational | √2: diagonal of the unit square; 1.4→1.96, 1.5→2.25, 1.4142…; digits never end, never repeat; no fraction captures it — irrational | title + unit square + digit chain + name card |
| 7 | cube roots | Undo a cube: ∛8=2, ∛27=3 (volume→side); the index; fourth root ∜16=2; nth roots | title + 2 eqs + cube grid + index label |
| 8 | negatives | Odd roots sail through: ∛(−8)=−2, ∛(−27)=−3; even roots refuse: √(−9) has no answer (both signs square positive) | title + odd row + RED no-answer card |
| 9 | ± vs √ | x²=9 has two answers ±3, but √9 means only the positive one (the convention, named once) | title + equation row + convention box |
| 10 | mental magic | ∛1728 in your head: last digit 8→2³→ends in 2; between 10³ and 20³ → 12; check 12³=1728 | title + 2-step rows + check line |
| 11 | habitat | Pythagoras: legs 3,4 → squares hold 9+16, long side = √25 = 5; area→side, volume→side, diagonal→root | title + 3-4-5 triangle + area labels |
| 12 | summary | Recap map; √2 has an address between 1.4 and 1.5 forever → The Real Number Line; outro | title + 4 lines + play_outro |

Animation vocabulary: titles→Write, body→FadeIn(shift=LEFT*0.15), formulas→
Write/Transform/ReplacementTransform, grids fade in cell by cell, sandwich rows
appear as aligned equation groups. All positioning via LayoutEngine
(title/safe_place/center_in_content/stack_down/formula_box/section_divider).
Scene dividers numbered 1–11 for scenes 2–12.

## Pacing (standardized cohort method, as Video 274)

1. Script written with provisional declareds; caption texts finalized FIRST,
   then AST full-text extraction (handles implicit string concat) from the
   script file.
2. Naturals measured per caption: DIRECT single-clip edge-tts, voice
   en-US-AndrewNeural, rate −5%; ffprobe duration.
3. declared = natural + 0.7 (2 dp).
4. Block-final wait bumps: every caption slot ≥ natural + 1.0 (target usage
   ≤ ~0.94). Slot model: section_divider 2.9s, title 0.75s, clear 0.8s,
   play_intro 6.2s, play_outro 8.0s, play(run_time=NORMAL)=1.2 / SLOW=2.0 /
   FAST=0.6, wait(x)=x. Bumps carry `# pacing:` comments; final slot (incl.
   outro) ≥ natural + 2.0.
5. py_compile after every edit pass.

## Handoff

Compile-clean + pacing-aligned script is handed to the produce stage:
`bash templates/produce.sh Video275_RootsRadicals ql` (480p15 draft), then
verify chain (render-1 SRT slot math → scene-final wait bumps → render #2 →
SRT slot math + central log 0 warnings/0 skips + volumedetect ≈ −20 dB + dot
QA + md5-matched copy to rendered/) per the cohort recipe.
