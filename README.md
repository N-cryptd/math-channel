# Math Channel — Production Pipeline

## Quick Start (per video)

```bash
# 1. Write the plan
vim planning/video-XX-topic.md

# 2. Write the Manim script from template
cp templates/template.py scripts/<playlist>/video-XX-topic.py

# 3. Draft render (fast, low quality)
manim -ql scripts/<playlist>/video-XX-topic.py VideoXX_Topic

# 4. Review — take still frames
manim -ql --format=png -s scripts/<playlist>/video-XX-topic.py VideoXX_Topic

# 5. Production render (slow, high quality)
manim -qh scripts/<playlist>/video-XX-topic.py VideoXX_Topic

# 6. Stitch scenes into final video (if multi-scene files)
# ffmpeg concat (see concat.txt)
```

## Project Structure

```
math-channel/
  planning/           # Video plans, curriculum, strategy
  scripts/
    pre-university/   # Arithmetic, Algebra, Geometry, Trig, Pre-calc
    undergraduate/    # Calculus, Linear Algebra, ODEs, Probability, etc.
    graduate/         # Measure Theory, Functional Analysis, etc.
  templates/          # Reusable script templates
  assets/
    audio/            # Background music, sound effects
    fonts/            # Custom fonts if needed
    thumbnails/       # Video thumbnails
```

## Naming Convention

- Plan files: `video-NN-topic-name.md` (NN = playlist-internal number)
- Script files: `video-NN-topic-name.py` (matches plan)
- Scene classes: `VideoNN_TopicName` (CamelCase, no spaces)
- Final videos: `NN-topic-name.mp4` in the script directory

## Scene Per File Rule

Each video is ONE Python file with ONE Scene class.
The class method `construct()` calls scene methods in sequence.
This keeps each video self-contained and independently renderable.

## Quality Checklist (before publishing)

- [ ] Background color set in every scene
- [ ] Subtitles on every animation (`self.add_subcaption`)
- [ ] `self.wait()` after every reveal
- [ ] No text overlap (use buff >= 0.5)
- [ ] Color constants used (no hardcoded colors)
- [ ] Opacity layering applied (primary 1.0, context 0.4, structure 0.15)
- [ ] Clean exit at scene end (FadeOut all mobjects)
- [ ] No more than 5-6 elements visible at once
- [ ] Font is Menlo monospace throughout
- [ ] Raw strings for LaTeX (r"\frac{1}{2}")
- [ ] Video starts with hook, ends with preview of next
