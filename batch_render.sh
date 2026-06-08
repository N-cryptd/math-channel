#!/bin/bash
# Batch render all 16 Calculus I videos at 480p15 for validation
set -e

SCRIPT_DIR="/root/math-channel/scripts/pre-university"
OUTPUT_DIR="/root/math-channel/rendered"
mkdir -p "$OUTPUT_DIR"

# Video files and their class names
declare -A VIDEOS
VIDEOS[01]="video-01-tangent-problem.py:Video01_TangentProblem"
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

OK=0
FAIL=0
LOG="$OUTPUT_DIR/batch_render.log"

echo "=== Batch Render Started: $(date) ===" > "$LOG"

for num in $(printf "%02d " {1..16}); do
    IFS=':' read -r script class <<< "${VIDEOS[$num]}"
    echo ""
    echo "──────────────────────────────────────────"
    echo "  Video $num: $script ($class)"
    echo "──────────────────────────────────────────"
    
    if manim -ql --disable_caching "$SCRIPT_DIR/$script" "$class" >> "$LOG" 2>&1; then
        # Find the rendered mp4
        mp4=$(find "$SCRIPT_DIR/media" -name "${class}.mp4" -newer "$LOG" -o -name "${class}.mp4" 2>/dev/null | head -1)
        if [ -n "$mp4" ]; then
            cp "$mp4" "$OUTPUT_DIR/Video${num}.mp4"
            echo "  ✓ Rendered -> $OUTPUT_DIR/Video${num}.mp4"
            ((OK++))
        else
            echo "  ✗ Render OK but mp4 not found"
            ((FAIL++))
        fi
    else
        echo "  ✗ FAILED — see $LOG"
        tail -5 "$LOG"
        ((FAIL++))
    fi
done

echo ""
echo "========================================="
echo "  Results: $OK OK, $FAIL FAILED"
echo "  Finished: $(date)"
echo "========================================="
echo "Results: $OK OK, $FAIL FAILED" >> "$LOG"
