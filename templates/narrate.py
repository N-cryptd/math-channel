#!/usr/bin/env python3
"""
TTS Narration Pipeline v3 for Manim Math Videos.

v3: Pure concat-based assembly — eliminates ALL audio overlap.
Replaced v2's amix mixing (which still caused overlap despite gap enforcement)
with ffmpeg concat demuxer — segments are placed sequentially so overlap is
physically impossible. Also fixed tts_dur not being recalculated after speedup.

Key improvements:
  - NO amix: pure concat demuxer (silence → clip → silence → clip → ...)
  - Gap enforcement: minimum 0.3s silence between segments
  - Smart splitting: long TTS gets split into sub-sentences
  - Duration verification: warns if final audio doesn't match video duration
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
    
    v3: Pure concat-based assembly — NO amix. Overlap is physically impossible
    because segments are concatenated sequentially (silence → clip → silence → ...).
    
    Algorithm:
    1. For each SRT segment, generate TTS and measure its natural duration
    2. Place segments on a timeline starting at each segment's SRT start time
    3. If a segment's audio would overlap with the previous segment's end,
       delay it to start after (prev_end + MIN_SEGMENT_GAP)
    4. If TTS is longer than available time, speed it up (with warning)
    5. Concatenate silence gaps + TTS clips sequentially (no mixing)
    
    Returns path to final audio file.
    """
    timeline = []  # list of (start_time, audio_file_path, audio_duration)
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
                # FIX: recalculate duration after speedup
                tts_dur = get_duration(sped_path)

        # Place on timeline (now track actual audio duration)
        timeline.append((actual_start, raw_path, tts_dur))
        last_end = actual_start + tts_dur

    if warnings:
        print("WARNINGS:", file=sys.stderr)
        for w in warnings:
            print(f"  ⚠ {w}", file=sys.stderr)
        print(file=sys.stderr)

    # Build final audio track using pure concat (NO amix — zero overlap risk)
    output_path = os.path.join(output_dir, "narration.wav")

    if not timeline:
        # No segments — return silence for full video duration
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=22050:cl=mono",
             "-t", str(video_duration), "-q:a", "9", output_path],
            capture_output=True,
        )
        return output_path

    # Normalize all audio clips to uniform format (22050Hz mono PCM)
    # This is required for the concat demuxer to work correctly
    norm_clips = []
    for idx, (start, audio_file, dur) in enumerate(timeline):
        norm_path = os.path.join(output_dir, f"norm_{idx:04d}.wav")
        subprocess.run(
            ["ffmpeg", "-y", "-i", audio_file,
             "-ar", "22050", "-ac", "1", "-c:a", "pcm_s16le",
             norm_path],
            capture_output=True,
        )
        norm_clips.append((start, norm_path, dur))

    # Build concat list: silence → clip → silence → clip → ... → final silence
    concat_list_path = os.path.join(output_dir, "final_concat.txt")
    concat_entries = []
    cursor = 0.0  # tracks current position in the timeline

    for idx, (start, norm_path, dur) in enumerate(norm_clips):
        # Silence gap before this segment
        gap = start - cursor
        if gap > 0.01:  # only add silence if gap > 10ms
            silence_path = os.path.join(output_dir, f"silence_{idx:04d}.wav")
            subprocess.run(
                ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=22050:cl=mono",
                 "-t", f"{gap:.3f}", "-c:a", "pcm_s16le", silence_path],
                capture_output=True,
            )
            concat_entries.append(silence_path)

        # The TTS clip itself
        concat_entries.append(norm_path)

        # Advance cursor past this clip
        cursor = start + dur

    # Final silence to fill remaining video duration
    remaining = video_duration - cursor
    if remaining > 0.01:
        final_silence_path = os.path.join(output_dir, "final_silence.wav")
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=22050:cl=mono",
             "-t", f"{remaining:.3f}", "-c:a", "pcm_s16le", final_silence_path],
            capture_output=True,
        )
        concat_entries.append(final_silence_path)

    # Write concat list
    with open(concat_list_path, "w") as f:
        for entry in concat_entries:
            f.write(f"file '{entry}'\n")

    # Concatenate everything sequentially — physically impossible to overlap
    result = subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
         "-i", concat_list_path,
         "-c:a", "pcm_s16le", output_path],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"FFmpeg concat error: {result.stderr[-500:]}", file=sys.stderr)
        # Fallback: return silence
        fallback = os.path.join(output_dir, "silence.wav")
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=22050:cl=mono",
             "-t", str(video_duration), "-q:a", "9", fallback],
            capture_output=True,
        )
        return fallback

    # Verify total duration is reasonable
    actual_dur = get_duration(output_path)
    if abs(actual_dur - video_duration) > 1.0:
        warnings.append(
            f"Duration mismatch: audio={actual_dur:.1f}s, video={video_duration:.1f}s"
        )
        print(f"  ⚠ Duration mismatch: audio={actual_dur:.1f}s vs video={video_duration:.1f}s",
              file=sys.stderr)

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
