#!/bin/bash
# Narrate all 24 videos with edge-tts
set -e

SCRIPT_DIR="/root/math-channel/scripts/pre-university"
RENDER_DIR="/root/math-channel/rendered"
NARRATE="/root/math-channel/templates/narrate.py"
LOG="$RENDER_DIR/narrate.log"
mkdir -p "$RENDER_DIR"

echo "=== Narration Started $(date) ===" > "$LOG"

for i in $(seq -w 1 24); do
    num=$((10#$i))
    src="$RENDER_DIR/Video${i}.mp4"
    dst="$RENDER_DIR/Video${i}_narrated.mp4"
    
    # Skip if already narrated
    [ -f "$dst" ] && echo "[Video $num] SKIP (already narrated)" >> "$LOG" && continue
    [ ! -f "$src" ] && echo "[Video $num] SKIP (no source)" >> "$LOG" && continue
    
    # Find matching SRT
    srt=$(find "$SCRIPT_DIR/media" -name "Video${i}_*.srt" -o -name "Video${num}_*.srt" 2>/dev/null | head -1)
    if [ -z "$srt" ]; then
        echo "[Video $num] SKIP (no SRT)" >> "$LOG"
        continue
    fi
    
    echo "[Video $num] Narrating with $srt..." >> "$LOG"
    
    if python3 "$NARRATE" --srt "$srt" --video "$src" --tts edge --voice en-US-AndrewNeural >> "$LOG" 2>&1; then
        echo "[Video $num] OK $(du -h "$dst" | cut -f1)" >> "$LOG"
    else
        echo "[Video $num] FAILED" >> "$LOG"
    fi
done

echo "=== Finished $(date) ===" >> "$LOG"
