#!/bin/bash
set -e
cd /root/math-channel

echo "=== Narrating Video 207 ==="
python3 templates/narrate.py \
    --srt media/videos/video-207-homotopy/480p15/Video207_Homotopy.srt \
    --video media/videos/video-207-homotopy/480p15/Video207_Homotopy.mp4 \
    --tts edge \
    --voice en-US-AndrewNeural \
    --output media/videos/video-207-homotopy/480p15/Video207_Homotopy_narrated.mp4

echo "=== Copying to rendered/ ==="
cp media/videos/video-207-homotopy/480p15/Video207_Homotopy_narrated.mp4 rendered/Video207_Homotopy_narrated.mp4

echo "=== Stats ==="
ls -la rendered/Video207_Homotopy_narrated.mp4
ffprobe -v quiet -print_format json -show_format rendered/Video207_Homotopy_narrated.mp4 2>&1 | head -20

echo "=== DONE ==="
