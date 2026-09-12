#!/usr/bin/env python3
"""Spot-check pacing of shipped renders in never-audited cohorts.
Method (per improvement-tracker.md audits): slot span = start-to-start SRT
interval; natural = DIRECT single-clip edge-tts en-US-AndrewNeural --rate=-5%.
DEFECT if span < 1.08 * natural + 0.3. SKIP-RISK if available < 1.5s.
"""
import re, subprocess, sys, tempfile, os

SRTs = sys.argv[1:]
VIDEOS = "/root/math-channel/rendered"

def parse_srt(path):
    txt = open(path, encoding="utf-8").read()
    blocks = re.split(r"\n\s*\n", txt.strip())
    rows = []
    for b in blocks:
        lines = [l for l in b.splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        m = re.match(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)", lines[1])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        start = g[0]*3600 + g[1]*60 + g[2] + g[3]/1000
        end = g[4]*3600 + g[5]*60 + g[6] + g[7]/1000
        text = " ".join(lines[2:])
        rows.append((start, end, text))
    return rows

def tts_duration(text):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        out = f.name
    try:
        subprocess.run(
            ["edge-tts", "--voice", "en-US-AndrewNeural", "--rate=-5%",
             "--text", text, "--write-media", out],
            check=True, capture_output=True, timeout=120)
        r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries",
                            "format=duration", "-of", "csv=p=0", out],
                           capture_output=True, text=True, check=True)
        return float(r.stdout.strip())
    finally:
        os.unlink(out)

def video_duration(path):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries",
                        "format=duration", "-of", "csv=p=0", path],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())

for srt in SRTs:
    name = os.path.basename(srt).replace(".srt", "")
    mp4 = os.path.join(VIDEOS, name + "_narrated.mp4")
    if not os.path.exists(mp4):
        print(f"{name}: NO RENDER FOUND"); continue
    vdur = video_duration(mp4)
    rows = parse_srt(srt)
    print(f"\n=== {name}  ({vdur:.1f}s video, {len(rows)} captions) ===")
    ndef = 0
    for i, (start, end, text) in enumerate(rows):
        span = (rows[i+1][0] if i+1 < len(rows) else vdur) - start
        nat = tts_duration(text)
        ratio = nat / span if span > 0 else 99
        flag = ""
        if span < 1.08 * nat + 0.3:
            flag = "DEFECT"; ndef += 1
        if span < 1.5:
            flag += " SKIP-RISK"
        print(f"  cap{i}: span {span:6.2f}s  natural {nat:6.2f}s  ratio {ratio:5.2f}x  {flag}")
    print(f"  --> {ndef}/{len(rows)} defective")
