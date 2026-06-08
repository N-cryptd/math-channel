#!/usr/bin/env python3
"""
Run a full competitive analysis sweep:
1. Fetch competitor channel video lists (youtubei.js — no IP restrictions)
2. Get individual video metadata (youtubei.js — no IP restrictions)
3. Download thumbnails (direct from ytimg.com)
4. Analyze thumbnails with AI vision (Phi-4 multimodal on NVIDIA NIM)
5. Write actionable improvement entries to improvements.md

Usage:
    python3 run_analysis.py [--channels "@3blue1brown @mathologer"] [--top-n 3]

Designed to be called by the weekly analysis cron job.
No Tor, no browser, no login required — works from any IP.
"""

import json, subprocess, sys, os, argparse, urllib.request
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
IMPROVEMENTS_FILE = BASE_DIR / "improvements.md"
THUMBNAIL_DIR = BASE_DIR / "thumbnails"
NODE_SCRIPT = BASE_DIR / "fetch_video_metadata.js"
CHANNEL_SCRIPT = BASE_DIR / "fetch_channel_videos.js"
THUMB_SCRIPT = BASE_DIR / "analyze_thumbnail.py"

DEFAULT_CHANNELS = ["@3blue1brown", "@mathologer", "@zachstar", "@drpeyam", "@socratica"]


def run_node(script, args, timeout=120):
    """Run a Node.js script and return parsed JSON output."""
    cmd = ["node", str(script)] + args
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=str(BASE_DIR))
    if result.returncode != 0:
        stderr = result.stderr.split('\n')[0][:100]
        print(f"  [WARN] {script.name}: {stderr}")
        return []
    # Find JSON in output (ignore stderr lines)
    lines = result.stdout.strip().split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('[') or line.strip().startswith('{'):
            try:
                data = json.loads('\n'.join(lines[i:]))
                return data if isinstance(data, list) else [data]
            except json.JSONDecodeError:
                continue
    return []


def fetch_channel_videos(channel_handle, limit=20):
    """Fetch video list from a channel via youtubei.js."""
    return run_node(CHANNEL_SCRIPT, [channel_handle, "--limit", str(limit)], timeout=30)


def fetch_video_metadata(video_ids):
    """Fetch individual video metadata via youtubei.js."""
    if not video_ids:
        return []
    return run_node(NODE_SCRIPT, video_ids, timeout=90)


def download_thumbnail(video_id):
    """Download thumbnail directly (no Tor needed)."""
    THUMBNAIL_DIR.mkdir(exist_ok=True)
    path = THUMBNAIL_DIR / f"{video_id}.jpg"
    if path.exists() and path.stat().st_size > 1000:
        return str(path)
    for quality in ["maxresdefault", "hqdefault", "mqdefault"]:
        url = f"https://i.ytimg.com/vi/{video_id}/{quality}.jpg"
        try:
            urllib.request.urlretrieve(url, path)
            if path.stat().st_size > 1000:
                return str(path)
        except Exception:
            continue
    return None


def analyze_thumbnail(thumbnail_path):
    """Analyze thumbnail with AI vision (Phi-4 multimodal)."""
    if not thumbnail_path:
        return None
    cmd = ["python3", str(THUMB_SCRIPT), thumbnail_path, "--quick"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return None


def write_improvement(analysis, metadata, channel_name):
    """Write an improvement entry to improvements.md."""
    if not analysis or not metadata:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    title = metadata.get("title", "Unknown")
    views = metadata.get("views", "?")

    with open(IMPROVEMENTS_FILE, "a") as f:
        f.write(f"\n## [{timestamp}] {channel_name} — {title}\n\n")
        f.write(f"**URL:** {metadata.get('url', '')}\n")
        f.write(f"**Views:** {views} | **Date:** {metadata.get('date', '?')}\n")
        f.write(f"**Duration:** {metadata.get('duration_seconds', '?')}s | **Captions:** {metadata.get('has_captions', '?')}\n\n")

        raw = analysis.get("raw_analysis", "")
        if raw:
            f.write(f"**Visual Analysis ({analysis.get('model_used', '?')}):**\n{raw}\n\n")

        f.write("---\n")

    print(f"  [+] {title[:50]} ({views})")


def main():
    parser = argparse.ArgumentParser(description="Run competitive analysis sweep")
    parser.add_argument("--channels", nargs="*", default=DEFAULT_CHANNELS)
    parser.add_argument("--top-n", type=int, default=3, help="Top N videos per channel")
    args = parser.parse_args()

    print(f"=== Competitive Analysis — {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")
    print(f"Channels: {', '.join(args.channels)}")
    print(f"Top {args.top_n} per channel\n")

    total = 0

    for channel in args.channels:
        print(f"--- {channel} ---")

        # Step 1: Channel video list
        videos = fetch_channel_videos(channel, limit=args.top_n + 2)
        if not videos:
            print("  No videos found")
            continue
        print(f"  {len(videos)} videos found")

        # Step 2: Metadata for top N
        video_ids = [v["video_id"] for v in videos[:args.top_n] if v.get("video_id")]
        metadata_list = fetch_video_metadata(video_ids)
        meta_map = {m["video_id"]: m for m in metadata_list if m.get("video_id")}

        for vid in videos[:args.top_n]:
            vid_id = vid.get("video_id")
            if not vid_id:
                continue

            print(f"  [{vid_id}] {vid.get('title', '?')[:50]} ({vid.get('views', '?')})")

            # Step 3: Thumbnail analysis
            thumb = download_thumbnail(vid_id)
            analysis = analyze_thumbnail(thumb)

            # Step 4: Write improvement
            meta = meta_map.get(vid_id, {})
            meta.update(vid)  # Merge channel fetch data with metadata
            write_improvement(analysis, meta, channel)
            total += 1

    print(f"\n=== Done: {total} entries → {IMPROVEMENTS_FILE} ===")


if __name__ == "__main__":
    main()
