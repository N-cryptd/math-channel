#!/usr/bin/env python3
"""Narrate Video 200: Gaussian Curvature"""
import subprocess, os, shutil

video = "/root/math-channel/media/videos/video-200-gaussian-curvature/480p15/Video200_GaussianCurvature.mp4"
srt = "/root/math-channel/media/videos/video-200-gaussian-curvature/480p15/Video200_GaussianCurvature.srt"
out = "/root/math-channel/media/videos/video-200-gaussian-curvature/480p15/Video200_GaussianCurvature_narrated.mp4"
narrate_script = "/root/math-channel/templates/narrate.py"
rendered_dir = "/root/math-channel/rendered"

print(f"Video exists: {os.path.exists(video)}")
print(f"SRT exists: {os.path.exists(srt)}")

# Run narrate.py
result = subprocess.run(
    ["python3", narrate_script, "--srt", srt, "--video", video,
     "--tts", "edge", "--voice", "en-US-AndrewNeural", "--output", out],
    capture_output=True, text=True, cwd="/root/math-channel"
)
print("=== narrate.py stdout ===")
print(result.stdout)
if result.stderr:
    print("=== narrate.py stderr ===")
    print(result.stderr)
print(f"Exit code: {result.returncode}")

# Check output
if os.path.exists(out):
    size = os.path.getsize(out)
    print(f"\nNarrated video: {out}")
    print(f"Size: {size / 1024 / 1024:.1f} MB")

    # Get duration
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", out],
        capture_output=True, text=True
    )
    if probe.stdout.strip():
        print(f"Duration: {float(probe.stdout.strip()):.1f}s")

    # Copy to rendered/
    if os.path.isdir(rendered_dir):
        dest = os.path.join(rendered_dir, "Video200_GaussianCurvature_narrated.mp4")
        shutil.copy2(out, dest)
        print(f"Copied to: {dest}")
else:
    print(f"\nERROR: Narrated output not found at {out}")
    print("Render was successful but narration failed.")
