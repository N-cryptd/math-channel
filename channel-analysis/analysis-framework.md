# Channel Analysis Framework

## Purpose
Systematically analyze competitor Manim math channels to extract actionable
improvements for our video production pipeline.

## Analysis Types

### Type A: Topic-Aligned Analysis (before each new video)
Run when the production agent is about to start a new video.
Focus: How did the best channels cover THIS specific topic?

Steps:
1. Identify the next video topic from PLANNING_STATE.md
2. Search for competitor videos on the same topic (see competitors.md)
3. Fetch transcripts from top 3-5 competitor videos on that topic
4. Analyze along 5 dimensions (see rubric below)
5. Write findings to improvements.md
6. The production agent incorporates findings into the video plan

### Type B: Trend Analysis (weekly sweep)
Run weekly to catch new competitor content and emerging techniques.
Focus: What are successful channels doing that we're not?

Steps:
1. Check recent uploads from Tier 1 channels (last 7 days)
2. Identify any new video topics, visual techniques, or format experiments
3. Check engagement metrics (likes/comments ratio — proxy for quality)
4. Note any format innovations (shorts, series structure, community features)
5. Append summary to improvements.md

## Analysis Rubric (5 Dimensions)

For each competitor video analyzed, rate and note:

### 1. Structure (0-10)
- How is the video organized? (hook → intuition → formal → examples → conclusion?)
- Does it have clear sections? How does it handle transitions?
- What's the intro format? (cold open? question? preview?)

### 2. Pacing (0-10)
- How long is the video? Is the pace comfortable?
- How much time on intuition vs. formalism?
- Are there "breathing moments" or is it dense throughout?
- How does it handle the "so what?" moment?

### 3. Visual Techniques (0-10)
- What Manim techniques are used? (Transforms, color coding, 3D, motion?)
- How is color used for meaning? (e.g., 3B1B: basis vectors in different colors)
- Are there unique visual metaphors? (e.g., matrix as grid transformation)
- What's the level of visual complexity? (minimal vs. rich)
- Are there visual proofs or just animated equations?

### 4. Narration Style (0-10)
- What's the tone? (conversational, formal, enthusiastic, calm?)
- How are complex ideas explained? (analogies? step-by-step? visual-first?)
- How are proofs handled? (rigorous? sketch? visual-only?)
- Is there humor or storytelling?

### 5. Engagement Hooks (0-10)
- Does the video start with a compelling question or problem?
- Are there "aha moments" built in?
- Does it reference real-world applications?
- Does it leave the viewer wanting more? (cliffhangers, teasers)
- How does it connect to previous/future videos in the series?

## Output Format for Each Analysis

```markdown
## YYYY-MM-DD — [Topic Name]
Source: [Channel Name] — [Video Title] (URL)
Dimensions: Structure X/10 | Pacing X/10 | Visuals X/10 | Narration X/10 | Hooks X/10

### Key Insights
- [Specific actionable observation 1]
- [Specific actionable observation 2]

### Techniques to Adopt
- [Concrete technique we can use in our video]

### Techniques to Avoid
- [What they did poorly or that doesn't fit our style]

### Transcript Excerpts
- [Key transcript segments showing their approach]
```

## Search Strategy for Finding Topic-Aligned Videos

Use YouTube search with these patterns:
- "{topic name} 3blue1brown" or "{topic name} linear algebra"
- "{topic name} explained manim"
- "essence of linear algebra {topic}"
- "{topic name} bri the math guy"
- "{topic name} vcubingx"

If no direct match, search broader:
- "{topic name} animation math"
- "{topic name} visual proof"
- "{topic name} geometric intuition"
