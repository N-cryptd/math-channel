#!/usr/bin/env python3
import re
from pathlib import Path

# Parse existing SRT line by line
srt_path = Path("~/math-channel/media/videos/video-25-what-is-a-vector/480p15/Video25_WhatIsAVector.srt").expanduser()
lines = srt_path.read_text().strip().split('\n')
starts = []
duras = []
caps = []
i = 0
while i < len(lines):
    line = lines[i].strip()
    if line.isdigit():
        # sequence number
        i += 1
        # time line
        time_line = lines[i].strip()
        i += 1
        # caption lines until next number or empty
        caption_lines = []
        while i < len(lines) and not lines[i].strip().isdigit() and lines[i].strip() != '':
            caption_lines.append(lines[i].rstrip())  # keep internal spaces
            i += 1
        # parse time line
        m = re.match(r'(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})', time_line)
        if m:
            h1, m1, s1, ms1, h2, m2, s2, ms2 = m.groups()
            t1 = int(h1)*3600 + int(m1)*60 + int(s1) + int(ms1)/1000.0
            t2 = int(h2)*3600 + int(m2)*60 + int(s2) + int(ms2)/1000.0
            starts.append(t1)
            duras.append(t2 - t1)
            caps.append(' '.join(caption_lines))  # join with single space
        else:
            print(f"Failed to parse time line: {time_line}")
    else:
        i += 1

print(f"Parsed {len(starts)} captions from SRT")
for idx, (s, d, c) in enumerate(zip(starts, duras, caps), 1):
    print(f"{idx:2d}: start={s:6.2f}s dur={d:5.2f}s caption='{c[:50]}...'")

# Now measure natural TTS for each caption using edge-tts at -5%
import subprocess
import tempfile
import os
import json

def measure_natural_tts(text):
    """Return duration in seconds of edge-tts en-US-AndrewNeural --rate=-5% for given text."""
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
        wav_path = f.name
    try:
        # Use edge-tts CLI with correct syntax
        cmd = [
            'edge-tts',
            '--voice', 'en-US-AndrewNeural',
            '--rate=-5%',  # <-- NOTE: no space between = and value
            '--text', text,
            '--write-media', wav_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  edge-tts failed for caption: {result.stderr[:100]}")
            return None
        # Get duration via ffprobe
        cmd2 = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', wav_path]
        out = subprocess.run(cmd2, capture_output=True, text=True, timeout=10)
        if out.returncode != 0:
            print(f"  ffprobe failed: {out.stderr[:100]}")
            return None
        return float(out.stdout.strip())
    finally:
        if os.path.exists(wav_path):
            os.unlink(wav_path)

print("\nMeasuring natural TTS (edge-tts --rate=-5%)...")
naturals = []
for idx, cap in enumerate(caps, 1):
    dur = measure_natural_tts(cap)
    if dur is None:
        print(f"  {idx}: FAILED")
        naturals.append(0.0)
    else:
        naturals.append(dur)
        print(f"  {idx:2d}: {dur:5.2f}s")

# Write results to file for inspection
with open('/tmp/video25_analysis.txt', 'w') as f:
    f.write("Idx  Start   Dur   Natural  Notes\n")
    for i in range(len(starts)):
        f.write(f"{i+1:2d}  {starts[i]:6.2f}  {duras[i]:5.2f}  {naturals[i]:5.2f}  {caps[i][:30]}...\n")
print("\nWrote baseline to /tmp/video25_analysis.txt")