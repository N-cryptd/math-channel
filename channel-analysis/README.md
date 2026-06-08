# Channel Analysis System

## Infrastructure

All analysis scripts use **Tor + Playwright** to bypass YouTube's cloud IP blocking.

### Prerequisites
1. `systemctl start tor` — Tor must be running (auto-starts on boot)
2. `playwright` + `PySocks` installed in Hermes venv
3. Scripts use `/usr/local/lib/hermes-agent/venv/bin/python3` 

### Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `fetch_channel_videos.py` | Get channel's video list (titles, IDs, thumbnails) | `python3 fetch_channel_videos.py @3blue1brown --limit 30` |
| `fetch_video_metadata.py` | Get single video metadata + screenshot | `python3 fetch_video_metadata.py VIDEO_ID --screenshot` |
| `fetch_transcript_tor.py` | Get video transcript (if available via Tor) | `python3 fetch_transcript_tor.py VIDEO_ID --text-only` |

### Competitor Channels (see competitors.md)

**Tier 1** — Direct competitors (full math curriculum + Manim):
- 3Blue1Brown (@3blue1brown) — 234 videos, 8.34M subs
- Mathologer (@mathologer) — Manim + traditional
- Zach Star (@zachstar) — Math/engineering

**Tier 2** — Partial overlap / inspiration:
- Looking Glass Universe (@lookingglassun) — Quantum
- Steve Brunton (@Eigensteve) — Applied math
- Reducible (@Reducible) — CS/math
- The Math Sorcerer (@themathsorcerer) — Pure math
- Socratica (@Socratica) — Math basics
- Inigo Quilez (@iquilezles) — Math+graphics
- Sabine Hossenfelder (@SabineHossenfelder) — Physics

### Analysis Types

**Type A: Video-Level Analysis** (per video)
- Visual style: colors, background, text, animation quality
- Title format: wording, length, punctuation patterns
- Thumbnail analysis: design, text overlay, color palette
- Engagement: views, likes ratio, comments patterns

**Type B: Channel-Level Analysis** (per channel)  
- Content strategy: topic selection, sequencing, curriculum structure
- Upload frequency and consistency
- Video length patterns
- Playlist organization
- Thumbnail consistency

**Type C: Cross-Channel Comparison**
- Common topic coverage gaps
- Title optimization patterns across top performers
- Visual style trends
- Audience size vs. content depth correlation

### Output Files

| File | Updated by | Used by |
|------|-----------|---------|
| `competitors.md` | Initial setup + weekly cron | Analysis agent |
| `improvements.md` | Analysis agent | Production agent (via AGENTS.md) |
| `analyses/` | Analysis agent | Historical reference |
| `screenshots/` | Metadata fetcher | Visual analysis |

### Cron Integration

The **weekly competitor analysis cron** (Wednesdays 10:00 CEST) runs the full sweep:
1. Fetches latest videos from each competitor channel
2. Compares topic coverage against our curriculum
3. Analyzes visual style from screenshots
4. Researches competitor techniques via web search
5. Writes actionable improvements to `improvements.md`

The **daily production cron** reads `improvements.md` before each new video.
