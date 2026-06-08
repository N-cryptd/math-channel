# Quality Improvement Plan — Math Channel v2

**Date:** 2026-05-24
**Trigger:** User review of Calc I/II videos (Videos 1-24)
**Scope:** Template overhaul, narration pipeline, production standards

---

## Issues Found

### 1. Audio Overlap & Distortion (Critical)
- `narrate.py` uses `amix` with no gap enforcement between segments
- Adjacent `add_subcaption()` calls with overlapping timings cause audio bleed
- TTS speedup via `atempo` (up to 3x) produces distorted, unnatural speech
- No silence padding between segments

### 2. Layout & Positioning (Critical)
- LayoutEngine exists but is inconsistently used
- Scripts use hardcoded `.shift()` / `.to_edge()` values that don't adapt to content
- `ensure_fits()` only checks width, ignores vertical overflow
- No content budget system — scenes cram unlimited items on screen
- Auto-scale-down makes text too small when too many items are added

### 3. Visual Theme (Important)
- Solid color background with no depth
- Menlo (monospace) used for all text — not ideal for a math channel
- No consistent animation vocabulary (some Write, some FadeIn, inconsistent)
- No section dividers or visual rhythm between concepts
- Color scheme functional but not distinctive

### 4. Production Strategy (Important)
- No storyboarding before writing scripts
- No max-items-per-scene rule
- No progressive disclosure (dump all content at once)
- No scene duration estimation tied to narration length
- Scripts are essentially "stack text and formulas"

---

## Implementation Plan

### Phase 1: Narration Pipeline Rewrite
**Files:** `templates/narrate.py`

Changes:
- TTS-first approach: generate audio first, measure actual duration, then calculate video timing
- Enforce minimum gap (0.3s) between adjacent audio segments
- If TTS > slot time: split text into sub-sentences and distribute across available time
- Add silence padding (0.2s) before and after each segment
- Better voice selection: use `en-US-AndrewNeural` with rate=-10% for natural pace
- Quality check: warn if any segment exceeds 2x speedup

### Phase 2: Layout Engine Overhaul
**Files:** `templates/layout.py`

Changes:
- Add `SceneLayout` context manager that enforces layout rules
- Content budget: `max_items` parameter (default 5), auto-warn/raise on overflow
- `stack_down()` with auto-split: if items overflow, return split groups for sub-scenes
- Ban raw `.shift()` / `.to_edge()` in content zone (enforce via linter instructions)
- Add `content_zone()` that returns a rectangular region below the title
- Font auto-scaling: reduce font size before compressing spacing
- Add `progressive_reveal()` method: animate items one by one, remove oldest when budget exceeded

### Phase 3: Visual Theme Upgrade
**Files:** `templates/channel_branding.py`

Changes:
- Background: subtle dot grid pattern (like 3B1B but in our palette)
- Font: switch body text to `Source Sans 3` (professional sans-serif), keep Menlo for code/labels
- Section divider component: animated line + section number
- Animation vocabulary:
  - Titles → `Write` with slight scale
  - Body text → `FadeIn` from LEFT
  - Formulas → `Transform` from previous step
  - Results/highlights → `Indicate` (brief glow)
  - Scene transitions → `ly.clear()` with 0.5s fade
- Color refinement: deeper background, more saturated primary, softer accent
- Add subtle background gradient (radial, center slightly lighter)

### Phase 4: Production Standards
**Files:** `AGENTS.md`, `templates/template.py`

New rules:
1. **5-item rule:** No more than 5 visible elements per scene at any time
2. **Progressive disclosure:** Add items one at a time, remove old before adding new
3. **Storyboard first:** Every video plan must include a scene-by-scene storyboard with content budget
4. **Duration estimation:** ~12 words of narration ≈ 10 seconds of video
5. **Visual variety:** Each scene must use at least 2 different animation types
6. **Scene types library:** Use predefined scene patterns (title-slide, derivation, comparison, graph, recap)
7. **QA checklist:** After render, verify: no overlap, no overflow, audio sync, visual consistency

---

## Priority Order
1. ~~Phase 1 (Narration)~~ — ✅ DONE — narrate.py v2 with sequential timeline, gap enforcement
2. ~~Phase 2 (Layout)~~ — ✅ DONE — LayoutEngine v2 with content budget, progressive reveal, overflow detection
3. ~~Phase 3 (Theme)~~ — ✅ DONE — channel_branding.py v2 with dot grid, Source Sans 3, animation vocabulary
4. ~~Phase 4 (Standards)~~ — ✅ DONE — AGENTS.md updated with 12 mandatory quality rules

## Status: ALL 4 PHASES COMPLETE

### What was changed:
| File | Status | Key Changes |
|------|--------|-------------|
| `templates/narrate.py` | REWRITTEN | Sequential timeline (no amix), 0.3s min gap, 0.15s padding, speedup quality gate, smart sentence splitting |
| `templates/layout.py` | REWRITTEN | LayoutEngine v2 with 5-item budget, progressive_reveal(), stack_down() with overflow detection, formula_box(), section_divider() |
| `templates/channel_branding.py` | REWRITTEN | New palette (BG=#1A1832, PRIMARY=#5BC0EB), Source Sans 3 font, dot grid background, play_intro()/play_outro() helpers, next video card |
| `templates/template.py` | REWRITTEN | Quality rules in docstring, LayoutEngine import, proper example code |
| `AGENTS.md` | UPDATED | Quality Standards v2 (12 rules), Branding v2 docs, LayoutEngine v2 requirement |
| Font: Source Sans 3 | INSTALLED | ~/.local/share/fonts/SourceSans3.ttf (variable weight) |

### Next Steps:
1. Reinstall Manim (venv was lost) to test templates
2. Re-render Videos 1-24 with new pipeline (optional, user decision)
3. Start Linear Algebra series (Video 25+) with new templates
4. Consider re-rendering a test video to validate the full pipeline end-to-end

## Affected Videos
- Videos 1-24: Will be re-rendered after template overhaul
- Videos 25+: Will use new templates from the start (Linear Algebra)
