#!/usr/bin/env python3
"""
Fetch YouTube video transcripts via Tor SOCKS5 proxy.
Uses requests library with socks transport for reliable HTTPS-over-SOCKS.

Usage:
    python3 fetch_transcript_tor.py <url_or_video_id> [--timestamps] [--language en]
    
Requirements:
    - tor service running (systemctl start tor)  
    - PySocks and requests installed

Output (JSON by default):
    {"video_id": "...", "segment_count": N, "duration": "...", "full_text": "..."}
    With --timestamps: includes "timestamped_text" field
    With --text-only: outputs plain text directly
"""

import argparse
import json
import re
import sys
import urllib.parse

import requests


def extract_video_id(url_or_id: str) -> str:
    """Extract 11-char video ID from URL or bare ID."""
    url_or_id = url_or_id.strip()
    patterns = [
        r'(?:v=|youtu\.be/|shorts/|embed/|live/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]
    for p in patterns:
        m = re.search(p, url_or_id)
        if m:
            return m.group(1)
    return url_or_id


def fmt_time(seconds: float) -> str:
    t = int(seconds)
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def make_session():
    """Create a requests session routed through Tor SOCKS5."""
    session = requests.Session()
    session.proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    })
    return session


def get_caption_tracks(session, video_id: str):
    """Fetch caption track list via innerTube player API."""
    payload = {
        "videoId": video_id,
        "context": {
            "client": {
                "clientName": "WEB",
                "clientVersion": "2.20260521.00.00",
                "hl": "en",
                "gl": "US",
            }
        }
    }
    resp = session.post(
        "https://www.youtube.com/youtubei/v1/player?prettyPrint=false",
        json=payload, timeout=30
    )
    data = resp.json()
    
    ps = data.get("playabilityStatus", {})
    if ps.get("status") != "OK":
        raise RuntimeError(f"Video not playable: {ps.get('status')} - {ps.get('reason', '')}")
    
    captions = data.get("captions", {})
    renderer = captions.get("playerCaptionsTracklistRenderer", {})
    return renderer.get("captionTracks", [])


def fetch_caption_content(session, base_url: str):
    """Fetch and parse caption segments from timedtext URL."""
    resp = session.get(base_url + "&fmt=json3", timeout=30)
    td = resp.json()
    events = [e for e in td.get("events", []) if "segs" in e]
    
    segments = []
    for e in events:
        text = "".join(s.get("utf8", "") for s in e["segs"]).strip()
        if text and text != "\n":
            segments.append({
                "start": e.get("tStartMs", 0) / 1000.0,
                "text": text,
            })
    return segments


def pick_track(tracks, lang: str):
    """Select best caption track for requested language."""
    # Exact match, non-auto
    for t in tracks:
        if t.get("languageCode") == lang and "auto" not in t.get("name", {}).get("simpleText", "").lower():
            return t
    # Any match
    for t in tracks:
        if t.get("languageCode") == lang:
            return t
    # English fallback
    if lang != "en":
        return pick_track(tracks, "en")
    return tracks[0] if tracks else None


def main():
    p = argparse.ArgumentParser(description="Fetch YouTube transcript via Tor proxy")
    p.add_argument("url", help="YouTube URL or video ID")
    p.add_argument("-l", "--language", default="en", help="Language code (default: en)")
    p.add_argument("-t", "--timestamps", action="store_true", help="Include timestamps")
    p.add_argument("--text-only", action="store_true", help="Plain text output")
    args = p.parse_args()

    video_id = extract_video_id(args.url)
    session = make_session()

    # Verify Tor connectivity
    try:
        r = session.get("https://check.torproject.org/api/ip", timeout=10)
        if not r.json().get("IsTor"):
            print(json.dumps({"error": "Not routing through Tor. Check tor service."}))
            sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"Tor not reachable: {e}. Run: systemctl start tor"}))
        sys.exit(1)

    try:
        tracks = get_caption_tracks(session, video_id)
    except RuntimeError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"Fetch failed: {e}"}))
        sys.exit(1)

    if not tracks:
        print(json.dumps({"error": f"No captions for {video_id}"}))
        sys.exit(1)

    track = pick_track(tracks, args.language)
    if not track:
        print(json.dumps({"error": f"No '{args.language}' captions for {video_id}"}))
        sys.exit(1)

    try:
        segments = fetch_caption_content(session, track["baseUrl"])
    except Exception as e:
        print(json.dumps({"error": f"Caption fetch failed: {e}"}))
        sys.exit(1)

    if not segments:
        print(json.dumps({"error": "Transcript was empty."}))
        sys.exit(1)

    full_text = " ".join(s["text"] for s in segments)
    timestamped = "\n".join(f"{fmt_time(s['start'])} {s['text']}" for s in segments)

    if args.text_only:
        print(timestamped if args.timestamps else full_text)
        return

    result = {
        "video_id": video_id,
        "language": track.get("languageCode", args.language),
        "track_name": track.get("name", {}).get("simpleText", ""),
        "segment_count": len(segments),
        "duration": fmt_time(segments[-1]["start"] + 5),
        "full_text": full_text,
    }
    if args.timestamps:
        result["timestamped_text"] = timestamped

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
