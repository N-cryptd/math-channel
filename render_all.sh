#!/bin/bash
# Render videos 02-16 and 18-24 at 480p15
set -e

SCRIPT_DIR="/root/math-channel/scripts/pre-university"
RENDER_DIR="/root/math-channel/rendered"
mkdir -p "$RENDER_DIR"

declare -A VIDEOS
VIDEOS[02]="video-02-power-rule.py:Video02_PowerRule"
VIDEOS[03]="video-03-product-quotient.py:Video03_ProductQuotient"
VIDEOS[04]="video-04-chain-rule.py:Video04_ChainRule"
VIDEOS[05]="video-05-implicit-related.py:Video05_ImplicitRelated"
VIDEOS[06]="video-06-exp-log.py:Video06_ExpLog"
VIDEOS[07]="video-07-trig-derivatives.py:Video07_TrigDerivatives"
VIDEOS[08]="video-08-mvt-applications.py:Video08_MVTApplications"
VIDEOS[09]="video-09-concavity.py:Video09_Concavity"
VIDEOS[10]="video-10-curve-sketching.py:Video10_CurveSketching"
VIDEOS[11]="video-11-lhopital.py:Video11_LHopital"
VIDEOS[12]="video-12-intro-integration.py:Video12_IntroIntegration"
VIDEOS[13]="video-13-antiderivatives.py:Video13_Antiderivatives"
VIDEOS[14]="video-14-u-substitution.py:Video14_USubstitution"
VIDEOS[15]="video-15-integration-by-parts.py:Video15_IntegrationByParts"
VIDEOS[16]="video-16-applications.py:Video16_Applications"
VIDEOS[17]="video-17-sequences.py:Video17_Sequences"
VIDEOS[18]="video-18-series.py:Video18_Series"
VIDEOS[19]="video-19-convergence-tests.py:Video19_ConvergenceTests"
VIDEOS[20]="video-20-power-series.py:Video20_PowerSeries"
VIDEOS[21]="video-21-taylor-maclaurin.py:Video21_TaylorMaclaurin"
VIDEOS[22]="video-22-parametric.py:Video22_Parametric"
VIDEOS[23]="video-23-polar.py:Video23_Polar"
VIDEOS[24]="video-24-calc2-review.py:Video24_Calc2Review"

LOG="$RENDER_DIR/render2.log"
echo "=== Render Started: $(date) ===" > "$LOG"

OK=0
FAIL=0

for num in 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24; do
    IFS=':' read -r script class <<< "${VIDEOS[$num]}"
    echo "[Video $num] Starting $script..." >> "$LOG"
    
    cd "$SCRIPT_DIR"
    if manim -ql --disable_caching "$script" "$class" >> "$LOG" 2>&1; then
        # Find and copy the mp4
        mp4=$(find "$SCRIPT_DIR/media" -name "${class}.mp4" 2>/dev/null | head -1)
        if [ -n "$mp4" ] && [ -f "$mp4" ]; then
            cp "$mp4" "$RENDER_DIR/Video${num}.mp4"
            echo "[Video $num] OK -> $RENDER_DIR/Video${num}.mp4" >> "$LOG"
            ((OK++))
        else
            echo "[Video $num] RENDERED BUT NO MP4 FOUND" >> "$LOG"
            ((FAIL++))
        fi
    else
        echo "[Video $num] FAILED" >> "$LOG"
        tail -3 "$LOG"
        ((FAIL++))
    fi
done

echo "" >> "$LOG"
echo "=== Results: $OK OK, $FAIL FAILED ===" >> "$LOG"
echo "=== Finished: $(date) ===" >> "$LOG"
echo "Results: $OK OK, $FAIL FAILED"
