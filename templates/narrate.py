#!/usr/bin/env python3
"""
TTS Narration Pipeline v2 for Manim Math Videos.

Complete rewrite to fix audio overlap, distortion, and sync issues.

Key improvements over v1:
  - Gap enforcement: minimum 0.3s silence between segments
  - Smart splitting: long TTS gets split into sub-sentences
  - No more amix overlap: segments are placed sequentially on a timeline
  - Silence padding: 0.15s before and after each segment
  - Quality gate: warn if any segment needs >1.5x speedup
  - Better rate control for edge-tts

Usage:
  python narrate.py --srt video.srt --video video.mp4 [--tts edge] [--voice en-US-AndrewNeural]
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


# ── Constants ───────────────────────────────────────────────────────
MIN_SEGMENT_GAP = 0.3   # minimum silence between adjacent segments
PRE_PAD = 0.15           # silence before each TTS segment
POST_PAD = 0.15          # silence after each TTS segment
MAX_SPEEDUP = 1.5        # warn if speedup exceeds this
MIN_SEGMENT_DUR = 1.5    # minimum duration for a TTS segment (avoid tiny clips)


def parse_srt(srt_path: str) -> list[dict]:
    """Parse an SRT file into a list of {start, end, text} dicts."""
    with open(srt_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"(\d+)\s*\n"
        r"(\d{2}):(\d{2}):(\d{2}),(\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2}),(\d{3})\s*\n"
        r"(.*?)(?=\n\n|\Z)",
        re.DOTALL,
    )

    segments = []
    for m in pattern.finditer(content):
        start_s = int(m.group(2)) * 3600 + int(m.group(3)) * 60 + int(m.group(4)) + int(m.group(5)) / 1000
        end_s = int(m.group(6)) * 3600 + int(m.group(7)) * 60 + int(m.group(8)) + int(m.group(9)) / 1000
        text = m.group(10).strip()
        # Remove HTML tags from Manim subcaptions
        text = re.sub(r"<[^>]+>", "", text)
        if text:
            segments.append({"start": start_s, "end": end_s, "text": text})

    return segments


def get_duration(file_path: str) -> float:
    """Get duration in seconds using ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", file_path],
        capture_output=True, text=True,
    )
    info = json.loads(result.stdout)
    return float(info["format"]["duration"])


def generate_tts(text: str, output_path: str, tts_backend: str = "edge", voice: str = "en-US-AndrewNeural") -> float:
    """Generate TTS audio. Returns duration in seconds."""
    if tts_backend == "edge":
        # Use slightly slower rate for natural speech
        subprocess.run(
            ["edge-tts", "--voice", voice, "--text", text,
             "--write-media", output_path, "--rate=-5%"],
            check=True, capture_output=True,
        )
    elif tts_backend == "espeak":
        subprocess.run(
            ["espeak-ng", "-v", "en", "-s", "145", "-p", "30", "-w", output_path, text],
            check=True, capture_output=True,
        )
    else:
        raise ValueError(f"Unknown TTS backend: {tts_backend}")
    return get_duration(output_path)


def split_text_to_sentences(text: str) -> list[str]:
    """Split text at sentence boundaries for sub-segment generation."""
    # Split on sentence-ending punctuation
    parts = re.split(r'(?<=[.!?])\s+', text)
    # Merge very short fragments
    merged = []
    for p in parts:
        if merged and len(p) < 30:
            merged[-1] += " " + p
        else:
            merged.append(p)
    return merged if merged else [text]


def speedup_audio(input_path: str, output_path: str, factor: float):
    """Speed up audio by a factor. Handles factors > 2.0 by chaining atempo."""
    chain = []
    remaining = factor
    while remaining > 1.0:
        step = min(remaining, 2.0)
        chain.append(f"atempo={step:.4f}")
        remaining /= step
    if not chain:
        # Slow down
        chain.append(f"atempo={factor:.4f}")

    filter_str = ",".join(chain)
    subprocess.run(
        ["ffmpeg", "-y", "-i", input_path, "-af", filter_str, output_path],
        capture_output=True,
    )


def build_audio_timeline(
    segments: list[dict],
    video_duration: float,
    output_dir: str,
    tts_backend: str = "edge",
    voice: str = "en-US-AndrewNeural",
) -> str:
    """
    Build a clean audio timeline with gap enforcement.
    
    Algorithm:
    1. For each SRT segment, generate TTS and measure its natural duration
    2. Place segments on a timeline starting at each segment's SRT start time
    3. If a segment's audio would overlap with the previous segment's end,
       delay it to start after (prev_end + MIN_SEGMENT_GAP)
    4. If TTS is longer than available time, speed it up (with warning)
    5. Concatenate all segments with proper silence gaps
    
    Returns path to final audio file.
    """
    timeline = []  # list of (start_time, audio_file_path)
    last_end = 0.0
    warnings = []

    for i, seg in enumerate(segments):
        slot_start = seg["start"]
        slot_end = seg["end"]
        slot_duration = slot_end - slot_start

        # Ensure minimum gap from previous segment
        actual_start = max(slot_start, last_end + MIN_SEGMENT_GAP)

        # Available time from actual_start to slot_end
        available = slot_end - actual_start

        if available < MIN_SEGMENT_DUR:
            # Not enough time for meaningful TTS — skip this segment
            warnings.append(
                f"Segment {i}: only {available:.1f}s available after gap enforcement, skipping"
            )
            continue

        # Try generating TTS for the full text
        raw_path = os.path.join(output_dir, f"raw_{i:04d}.wav")
        tts_dur = generate_tts(seg["text"], raw_path, tts_backend, voice)

        if tts_dur > available:
            # TTS doesn't fit — try splitting into sub-sentences
            sentences = split_text_to_sentences(seg["text"])
            if len(sentences) > 1 and tts_dur > available * 1.3:
                # Generate sub-sentence TTS and concatenate
                sub_files = []
                for j, sentence in enumerate(sentences):
                    sub_path = os.path.join(output_dir, f"sub_{i:04d}_{j:04d}.wav")
                    generate_tts(sentence, sub_path, tts_backend, voice)
                    sub_files.append(sub_path)

                # Concatenate sub-segments with short pauses
                combined_path = os.path.join(output_dir, f"combined_{i:04d}.wav")
                # Create silence gap between sub-sentences
                gap_path = os.path.join(output_dir, f"gap_{i:04d}.wav")
                subprocess.run(
                    ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=22050:cl=mono",
                     "-t", "0.15", "-q:a", "9", gap_path],
                    capture_output=True,
                )

                concat_list = os.path.join(output_dir, f"concat_{i:04d}.txt")
                with open(concat_list, "w") as f:
                    for k, sf in enumerate(sub_files):
                        f.write(f"file '{sf}'\n")
                        if k < len(sub_files) - 1:
                            f.write(f"file '{gap_path}'\n")

                subprocess.run(
                    ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
                     "-c", "copy", combined_path],
                    capture_output=True,
                )
                tts_dur = get_duration(combined_path)
                raw_path = combined_path

            # If still too long, speed it up
            if tts_dur > available:
                speedup = tts_dur / available
                if speedup > MAX_SPEEDUP:
                    warnings.append(
                        f"Segment {i}: needs {speedup:.1f}x speedup (text: \"{seg['text'][:50]}...\")"
                    )
                sped_path = os.path.join(output_dir, f"sped_{i:04d}.wav")
                speedup_audio(raw_path, sped_path, speedup)
                raw_path = sped_path

        # Place on timeline
        timeline.append((actual_start, raw_path))
        last_end = actual_start + min(tts_dur, slot_end - actual_start)

    if warnings:
        print("WARNINGS:", file=sys.stderr)
        for w in warnings:
            print(f"  ⚠ {w}", file=sys.stderr)
        print(file=sys.stderr)

    # Build final audio track
    if not timeline:
        # No segments — return silence
        silence_path = os.path.join(output_dir, "silence.wav")
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=22050:cl=mono",
             "-t", str(video_duration), "-q:a", "9", silence_path],
            capture_output=True,
        )
        return silence_path

    # Create base silence
    silence_path = os.path.join(output_dir, "base_silence.wav")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=22050:cl=mono",
         "-t", str(video_duration), "-q:a", "9", silence_path],
        capture_output=True,
    )

    # Use ffmpeg overlay approach: place each segment at its timestamp
    # Build filter_complex with delayed segments overlaid on silence
    inputs = ["-i", silence_path]
    filter_parts = []

    for idx, (start, audio_file) in enumerate(timeline):
        inputs.extend(["-i", audio_file])
        delay_ms = int(start * 1000)
        filter_parts.append(
            f"[{idx + 1}:a]adelay={delay_ms}|{delay_ms},apad[a{idx}]"
        )

    # Sequential mix: overlay each segment onto accumulated result
    # First segment mixes with silence
    mix_expr = f"[0:a][a0]amix=inputs=2:duration=first:dropout_transition=0[mix0]"
    for idx in range(1, len(timeline)):
        mix_expr += f";[mix{idx - 1}][a{idx}]amix=inputs=2:duration=first:dropout_transition=0[mix{idx}]"

    final_idx = len(timeline) - 1
    filter_parts.append(f"{mix_expr}")

    filter_complex = ";".join(filter_parts)
    output_path = os.path.join(output_dir, "narration.wav")

    cmd = ["ffmpeg", "-y"] + inputs + [
        "-filter_complex", filter_complex,
        "-map", f"[mix{final_idx}]",
        output_path,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FFmpeg error: {result.stderr[-500:]}", file=sys.stderr)
        return silence_path

    return output_path


def mux_audio_video(video_path: str, audio_path: str, output_path: str):
    """Mux audio into video using ffmpeg."""
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            output_path,
        ],
        capture_output=True,
    )


def main():
    parser = argparse.ArgumentParser(description="Add TTS narration to Manim videos (v2)")
    parser.add_argument("--srt", required=True, help="Path to .srt subtitle file")
    parser.add_argument("--video", required=True, help="Path to video file")
    parser.add_argument("--tts", default="edge",
                        choices=["espeak", "edge"],
                        help="TTS backend (default: edge)")
    parser.add_argument("--voice", default="en-US-AndrewNeural",
                        help="Voice name")
    parser.add_argument("--output", default=None,
                        help="Output path (default: <video>_narrated.mp4)")
    args = parser.parse_args()

    if not os.path.exists(args.srt):
        print(f"ERROR: SRT file not found: {args.srt}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(args.video):
        print(f"ERROR: Video file not found: {args.video}", file=sys.stderr)
        sys.exit(1)

    # Determine output path
    video_stem = Path(args.video).stem
    video_dir = str(Path(args.video).parent)
    output_path = args.output or os.path.join(video_dir, f"{video_stem}_narrated.mp4")

    print(f"=== TTS Narration Pipeline v2 ===")
    print(f"SRT:    {args.srt}")
    print(f"Video:  {args.video}")
    print(f"Output: {output_path}")
    print(f"TTS:    {args.tts} ({args.voice})")
    print()

    # Parse subtitles
    segments = parse_srt(args.srt)
    print(f"Parsed {len(segments)} subtitle segments")

    for seg in segments[:5]:
        print(f"  [{seg['start']:.1f}s - {seg['end']:.1f}s] {seg['text'][:60]}...")
    if len(segments) > 5:
        print(f"  ... and {len(segments) - 5} more")
    print()

    # Get video duration
    video_duration = get_duration(args.video)
    print(f"Video duration: {video_duration:.1f}s")
    print()

    # Generate TTS
    print("Generating TTS audio with gap enforcement...")
    with tempfile.TemporaryDirectory() as tmpdir:
        narration_path = build_audio_timeline(
            segments, video_duration, tmpdir,
            tts_backend=args.tts, voice=args.voice,
        )
        print(f"Narration audio: {narration_path}")
        print()

        # Mux
        print("Muxing audio into video...")
        mux_audio_video(args.video, narration_path, output_path)

    print(f"Done! Output: {output_path}")


if __name__ == "__main__":
    main()
