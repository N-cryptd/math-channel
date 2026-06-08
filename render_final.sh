#!/bin/bash
SCRIPT_DIR="/root/math-channel/scripts/pre-university"
RENDER_DIR="/root/math-channel/rendered"
LOG="$RENDER_DIR/render4.log"
echo "=== Started $(date) ===" > "$LOG"

render() {
    local num=$1 script=$2 cls=$3
    local dest="$RENDER_DIR/Video$(printf '%02d' $num).mp4"
    [ -f "$dest" ] && echo "[Video $num] SKIP" >> "$LOG" && return 0
    echo "[Video $num] Rendering $script..." >> "$LOG"
    cd "$SCRIPT_DIR"
    if manim -ql --disable_caching "$script" "$cls" >> "$LOG" 2>&1; then
        local mp4=$(find "$SCRIPT_DIR/media" -name "${cls}.mp4" 2>/dev/null | head -1)
        if [ -n "$mp4" ] && [ -f "$mp4" ]; then
            cp "$mp4" "$dest"
            echo "[Video $num] OK $(du -h "$dest" | cut -f1)" >> "$LOG"
        else
            echo "[Video $num] RENDER OK BUT NO MP4" >> "$LOG"
        fi
    else
        echo "[Video $num] FAILED" >> "$LOG"
    fi
}

render 09 "video-09-concavity.py"              "Video09_ConcavitySecondDeriv"
render 18 "video-18-series.py"                 "Video18_Series"
render 19 "video-19-convergence-tests.py"      "Video19_ConvergenceTests"
render 20 "video-20-power-series.py"           "Video20_PowerSeries"
render 21 "video-21-taylor-maclaurin.py"       "Video21_TaylorMaclaurin"
render 22 "video-22-parametric.py"             "Video22_Parametric"
render 23 "video-23-polar.py"                  "Video23_Polar"
render 24 "video-24-calc2-review.py"           "Video24_Calc2Review"

echo "=== Finished $(date) ===" >> "$LOG"
