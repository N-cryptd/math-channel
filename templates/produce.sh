#!/usr/bin/env bash
# Automated production pipeline for Math Channel videos.
# Usage:
#   ./produce.sh Video03_ProductQuotient ql   # draft render + narrate
#   ./produce.sh Video03_ProductQuotient qh   # production render + narrate
#   ./produce.sh all ql                        # draft all videos in calculus playlist

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

QUALITY="${2:-ql}"
CLASS_NAME="${1:-}"

if [ -z "$CLASS_NAME" ]; then
    echo "Usage: $0 <VideoClassName|all> [ql|qh|qm]"
    exit 1
fi

produce_video() {
    local class="$1"
    local quality="$2"

    echo "=== Producing: $class ($quality) ==="

    # Find the script file containing this class
    local script_file
    script_file=$(grep -rl "class $class" "$PROJECT_DIR/scripts/" --include="*.py" | head -1)

    if [ -z "$script_file" ]; then
        echo "ERROR: Could not find script containing class $class" >&2
        return 1
    fi

    echo "  Script: $script_file"

    # Render
    cd "$PROJECT_DIR"
    manim -"$quality" "$script_file" "$class" 2>&1 | tail -3

    # Determine output paths
    local video_dir="media/videos"
    local quality_name=""
    case "$quality" in
        ql) quality_name="480p15" ;;
        qm) quality_name="720p30" ;;
        qh) quality_name="1080p60" ;;
        *) quality_name="480p15" ;;
    esac

    # Find the video and srt files
    local video_path
    video_path=$(find "$video_dir" -name "${class}.mp4" -path "*/${quality_name}/*" 2>/dev/null | head -1)

    if [ -z "$video_path" ]; then
        echo "  WARNING: Video not found (maybe subdirectory mismatch)" >&2
        return 1
    fi

    local srt_path="${video_path%.mp4}.srt"

    if [ -f "$srt_path" ]; then
        echo "  Narrating with narrate.py v2 (sequential timeline)..."
        python3 "$SCRIPT_DIR/narrate.py" \
            --srt "$srt_path" \
            --video "$video_path" \
            --tts edge \
            --voice en-US-AndrewNeural \
            --output "${video_path%.mp4}_narrated.mp4" 2>&1
    else
        echo "  WARNING: No SRT file found at $srt_path, skipping narration" >&2
    fi

    echo "  Done! ${video_path%.mp4}_narrated.mp4"
    echo ""
}

if [ "$CLASS_NAME" = "all" ]; then
    echo "=== Producing all Calculus I videos ==="
    for class in Video01_TangentProblem Video02_PowerRule Video03_ProductQuotient Video04_ChainRule Video05_ImplicitRelated Video06_ExpLogDerivatives Video07_TrigonometricDerivatives Video08_MVTApplications Video09_ConcavitySecondDeriv Video10_CurveSketching Video11_LHopital Video12_IntroIntegration Video13_Antiderivatives Video14_USubstitution Video15_IntegrationByParts Video16_Applications; do
        produce_video "$class" "$QUALITY"
    done
    echo "=== All videos produced ==="
else
    produce_video "$CLASS_NAME" "$QUALITY"
fi