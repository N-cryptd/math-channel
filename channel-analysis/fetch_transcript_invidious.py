#!/usr/bin/env python3
"""
Fetch YouTube video transcripts using Invidious public API (bypasses cloud IP blocks).
Returns plain text or timestamped text, similar to the youtube-transcript-api script.

Usage:
    python3 fetch_transcript_invidious.py <url_or_video_id> [--timestamps] [--language en]

Invidious instances are tried in order until one responds.
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

# Public Invidious instances that support the API
INVIDIOUS_INSTANCES = [
    "https://inv.nadeko.net",
    "https://invidious.nerdvpn.de",
    "https://invidious.jing.rocks",
    "https://invidious.privacyredirect.com",
    "https://iv.ggtyler.dev",
    "https://invidious.protokolla.fi",
]


def extract_video_id(url_or_id: str) -> str:
    """Extract the 11-character video ID from various YouTube URL formats."""
    url_or_id = url_or_id.strip()
    patterns = [
        r'(?:v=|youtu\.be/|shorts/|embed/|live/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id


def format_timestamp(seconds: float) -> str:
    """Convert seconds to MM:SS or HH:MM:SS format."""
    total = int(seconds)
    h, remainder = divmod(total, 3600)
    m, s = divmod(remainder, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def try_instance(instance: str, path: str, timeout: int = 10) -> bytes:
    """Make a request to an Invidious instance, return raw bytes or raise."""
    url = f"{instance}{path}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        raise ConnectionError(f"Instance {instance} failed: {e}")


def get_transcript(video_id: str, language: str = "en") -> list:
    """
    Fetch transcript via Invidious captions API.
    Returns list of dicts with 'text', 'start', 'duration' keys.
    """
    # Step 1: Get available captions
    captions_data = None
    captions_url = None

    for instance in INVIDIOUS_INSTANCES:
        try:
            raw = try_instance(instance, f"/api/v1/captions/{video_id}")
            captions_data = json.loads(raw)
            working_instance = instance
            break
        except (ConnectionError, json.JSONDecodeError):
            continue

    if not captions_data or "captions" not in captions_data:
        raise RuntimeError(f"No captions found for video {video_id} across all Invidious instances")

    # Step 2: Find the right language
    captions = captions_data["captions"]
    chosen = None

    # Prefer exact language match (not auto-generated)
    for cap in captions:
        if cap["languageCode"] == language and "auto" not in cap.get("label", "").lower():
            chosen = cap
            break

    # Fall back to any match including auto-generated
    if not chosen:
        for cap in captions:
            if cap["languageCode"] == language:
                chosen = cap
                break

    # Fall back to English if different language requested
    if not chosen:
        for cap in captions:
            if cap["languageCode"] == "en":
                chosen = cap
                break

    # Fall back to any available caption
    if not chosen and captions:
        chosen = captions[0]

    if not chosen:
        raise RuntimeError(f"No suitable captions found for video {video_id}")

    # Step 3: Fetch the actual caption content (SRT/VTT format)
    label = urllib.parse.quote(chosen["label"])
    for instance in INVIDIOUS_INSTANCES:
        try:
            raw = try_instance(instance, f"/api/v1/captions/{video_id}?label={label}")
            text = raw.decode("utf-8")
            return parse_vtt(text)
        except (ConnectionError, Exception):
            continue

    raise RuntimeError(f"Failed to fetch caption content from all instances")


def parse_vtt(text: str) -> list:
    """Parse WebVTT or SRT subtitle format into timestamped segments."""
    segments = []
    lines = text.strip().split("\n")
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Look for timestamp line (HH:MM:SS.mmm --> HH:MM:SS.mmm)
        if "-->" in line:
            parts = line.split("-->")
            if len(parts) == 2:
                try:
                    start = parse_time(parts[0].strip())
                    # Collect text lines until next timestamp or blank line
                    i += 1
                    text_lines = []
                    while i < len(lines):
                        next_line = lines[i].strip()
                        if not next_line or "-->" in next_line:
                            break
                        # Remove HTML tags
                        clean = re.sub(r'<[^>]+>', '', next_line)
                        if clean:
                            text_lines.append(clean)
                        i += 1

                    if text_lines:
                        segments.append({
                            "text": " ".join(text_lines),
                            "start": start,
                        })
                    continue
                except (ValueError, IndexError):
                    pass
        i += 1

    # Calculate durations
    for idx in range(len(segments)):
        if idx + 1 < len(segments):
            segments[idx]["duration"] = segments[idx + 1]["start"] - segments[idx]["start"]
        else:
            segments[idx]["duration"] = 5.0  # default last segment

    return segments


def parse_time(s: str) -> float:
    """Parse a VTT/SRT timestamp to seconds."""
    s = s.strip().replace(",", ".")
    # Handle HH:MM:SS.mmm or MM:SS.mmm or SS.mmm
    parts = s.split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    elif len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    else:
        return float(parts[0])


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcript via Invidious")
    parser.add_argument("url", help="YouTube URL or video ID")
    parser.add_argument("--language", "-l", default="en", help="Language code (default: en)")
    parser.add_argument("--timestamps", "-t", action="store_true", help="Include timestamps")
    parser.add_argument("--text-only", action="store_true", help="Plain text output")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)

    try:
        segments = get_transcript(video_id, args.language)
    except RuntimeError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    if not segments:
        print(json.dumps({"error": "Transcript was empty."}))
        sys.exit(1)

    full_text = " ".join(seg["text"] for seg in segments)
    timestamped = "\n".join(
        f"{format_timestamp(seg['start'])} {seg['text']}" for seg in segments
    )

    if args.text_only:
        print(timestamped if args.timestamps else full_text)
        return

    result = {
        "video_id": video_id,
        "segment_count": len(segments),
        "duration": format_timestamp(segments[-1]["start"] + segments[-1]["duration"]) if segments else "0:00",
        "full_text": full_text,
    }
    if args.timestamps:
        result["timestamped_text"] = timestamped

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
