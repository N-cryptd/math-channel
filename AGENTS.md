# Math Channel — Autonomous Video Production

## Project State
- 24 Calculus I/II videos complete (scripts in scripts/pre-university/)
- 5 Linear Algebra videos complete (Videos 25-29, scripts in scripts/undergraduate/)
- Video 30 (Inverse Matrices) has plan + script, pending render
- Videos 31-32 content being written via kanban
- All videos have narrated renders in ~/math-channel/rendered/ (480p15)
- Videos 1-16 also in media/videos/ (480p15)
- Manim Community v0.20.1 installed, edge-tts available
- Templates v2: channel_branding.py, layout.py, narrate.py, produce.sh, template.py
- Competitive analysis system in channel-analysis/
- **Quality audit May 2026:** Templates rewritten to fix audio overlap, layout cramming, theme
- **Kanban sync May 2026:** Staleness prevention added — workers must verify filesystem before starting
- See `planning/quality-improvement-plan.md` for full improvement details

## Your Role
You are an autonomous video production agent. Each run:

1. **Sync state** — check BOTH the filesystem AND PLANNING_STATE.md before starting. The filesystem is the ground truth. If scripts/plans/rendered files exist but PLANNING_STATE.md says BACKLOG, trust the files and update the doc.
2. **Check backlog** — read PLANNING_STATE.md (this directory) for the next video to produce
3. **Competitive analysis** — before starting a new video, analyze how top Manim channels covered that topic
4. **If no plan exists** for the next video: write the plan in planning/, incorporating analysis insights
5. **If plan + script exist**: render + narrate the video using the pipeline
6. **Update PLANNING_STATE.md** with progress
7. **Update kanban** — if you were dispatched via kanban, complete your task with `kanban_complete()`. If you ran outside kanban (direct), note the discrepancy.
8. **Report** what was produced

### Staleness Prevention (MANDATORY)
**Before doing ANY work, verify the filesystem state:**
```bash
ls ~/math-channel/scripts/undergraduate/video-{NN}-*.py  # script exists?
ls ~/math-channel/planning/video-{NN}-*.md               # plan exists?
ls ~/math-channel/rendered/*_narrated.mp4                # rendered?
```
- If a script/plan/render already exists for your assigned video, do NOT redo that step. Complete or skip that portion.
- Always update PLANNING_STATE.md after every state change (plan written, script written, render complete).
- If you find PLANNING_STATE.md is stale (files exist but doc says BACKLOG), fix the doc FIRST, then proceed with remaining work.
- **Kanban workers:** On startup, run the filesystem check. If your task is already done on disk, `kanban_complete()` immediately with a note.

## Step 2 Detail: Competitive Analysis

This is MANDATORY before writing any new video plan. Follow this workflow:

### 2a. Identify the topic
Read PLANNING_STATE.md to find the next PLANNED video. Get its topic name.

### 2b. Read existing analysis
Check `channel-analysis/improvements.md` for any prior analysis on this topic.
If analysis already exists for this exact video number+topic, skip to step 2f.

### 2c. Find competitor videos
Read `channel-analysis/competitors.md` for the competitor channel list.
Use web search to find competitor videos on the same or closely related topic:
- Search: "{topic name} 3blue1brown", "{topic name} explained animation", "{topic name} linear algebra"
- Prioritize: 3Blue1Brown > Mathologer > Reducible > Zach Star > others
- Find 2-4 relevant competitor videos (preferably from different channels)

### 2d. Fetch metadata and analyze thumbnails
For each competitor video found (need video_id from search results):
1. Get full metadata via youtubei.js (works from any IP, no Tor/browser needed):
   `node channel-analysis/fetch_video_metadata.js {video_id}`
   Returns: title, views, date, description, channel, subscribers, has_captions
2. Download thumbnail: `curl -sL "https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg" -o /tmp/{video_id}.jpg`
3. Analyze thumbnail with AI vision: `python3 channel-analysis/analyze_thumbnail.py /tmp/{video_id}.jpg --quick`
   - Primary model: microsoft/phi-4-multimodal-instruct (auto-fallback to nemotron-nano-vl)
   - Returns JSON with visual analysis of the thumbnail
4. Rate each competitor video along 5 dimensions (see channel-analysis/analysis-framework.md):
   - Structure (0-10): organization, transitions, section breaks
   - Pacing (0-10): intuition vs formalism balance, breathing room
   - Visual Techniques (0-10): Manim techniques, color coding, metaphors
   - Narration Style (0-10): tone, explanation method, proof handling
   - Engagement Hooks (0-10): opening hook, aha moments, real-world connections

### 2e. Write analysis to improvements.md
Append a formatted analysis entry to `channel-analysis/improvements.md` following
the format in `channel-analysis/analysis-framework.md`. Include:
- Key insights from each competitor video
- Thumbnail analysis: color palette, composition, quality rating
- Specific techniques to adopt in our video
- Techniques to avoid or adapt
- Standout approaches that show their unique style

### 2f. Incorporate into video plan
When writing the video plan (step 3 below), explicitly reference the analysis:
- "Based on 3B1B's approach to vectors, we'll..."
- "Unlike BriTheMathGuy's dense proof style, we'll..."
- "Following Reducible's storytelling technique, our intro will..."

## Production Pipeline

### For a new video (no script yet):
1. Read the curriculum map: `planning/curriculum-map.md`
2. **Run competitive analysis** (step 2 above)
3. Create a plan: `planning/video-NN-topic.md` (follow existing plan format, include analysis references)
4. Write the script: copy `templates/template.py` to `scripts/<level>/video-NN-topic.py`
5. CRITICAL: Use single backslashes in raw strings for LaTeX. See `references/production-pitfalls.md`
6. **ALWAYS use LayoutEngine v2** from layout.py for ALL positioning
7. Run compile check: `python3 -c "import py_compile; py_compile.compile('...', doraise=True)\"`
8. Run produce: `bash templates/produce.sh VideoNN_ClassName ql` (480p draft)

### For re-rendering (script exists, needs fresh render):
1. `bash templates/produce.sh VideoNN_ClassName ql`

## Next Videos (Priority Order)
**In progress:**
- Video 30: Inverse Matrices (script exists, needs render)
- Video 31: Systems of Equations (Matrix) (content writing)
- Video 32: Row Reduction / Echelon Form (content writing)

**Upcoming (Linear Algebra → Video 40: SVD):**
- Video 33: Null Space and Column Space
- Video 34: Rank and Nullity
- Video 35: Eigenvalues and Eigenvectors
- Video 36: Diagonalization
- Video 37: Inner Product Spaces
- Video 38: Orthogonality and Gram-Schmidt
- Video 39: Linear Transformations (Abstract)
- Video 40: Singular Value Decomposition

After LA, continue with Calculus III (multivariable) as it's the natural next math level.

## Video Naming Convention
- Script file: `video-NN-topic-name.py` (NN = sequential from 25)
- Class name: `VideoNN_TopicName` (PascalCase)
- Planning: `planning/video-NN-topic.md`
- Level directory: `scripts/undergraduate/` for Linear Algebra

## Channel Branding v2
- Colors: BG=#1A1832, PRIMARY=#5BC0EB, SECONDARY=#7BC950, ACCENT=#FFD166, RED=#EF476F
- Fonts: SANS="Source Sans 3" (body text, titles), MONO="Menlo" (code, labels)
- Always import from templates/channel_branding.py
- Every video opens with play_intro() and closes with play_outro()
- Each scene starts with add_subcaption() for TTS narration
- Background: deep color with subtle dot grid + radial gradient (setup_background())

## Constraints
- This VPS has NO GPU. Manim renders on CPU (480p is fine, 1080p is slow but doable)
- Keep each run focused: one video per cycle. Don't try to batch multiple.
- If rendering takes too long (>10 min), render at 480p15 (ql) and note that 1080p is pending
- edge-tts requires internet access (which this VPS has)
- Competitive analysis is PART of the production cycle, not optional — use youtubei.js for metadata (no IP restrictions). If web search fails, proceed with the video plan anyway and note the skipped analysis

## Quality Standards v2 (MANDATORY)
1. **5-item rule:** Maximum 5 visible mobjects on screen at any time
2. **No manual positioning:** Use LayoutEngine methods (ly.title, ly.safe_place, ly.stack_down, ly.progressive_reveal). NEVER use raw .shift() or .to_edge() for content.
3. **Progressive disclosure:** Add items one at a time. Remove oldest before adding new.
4. **Narration timing:** ~12 words of narration ≈ 5 seconds of video duration
5. **Scene clearing:** Always call ly.clear() between scenes
6. **Font discipline:** Use SANS for body text/titles, MONO for code/labels/formulas
7. **Animation vocabulary:** Titles→Write, Body→FadeIn(shift=LEFT*0.15), Formulas→Write/Transform, Graphs→Create
8. **Every MathTex** must use raw strings with single backslashes
9. **Test compile** before rendering
10. **Video duration:** 8-15 min per curriculum map
11. **Distinct content:** We don't copy competitors — we synthesize: different structure, our own visual metaphors, our pacing
12. **Storyboard first:** Each scene plan must list content budget (which items appear/disappear)
