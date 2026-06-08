#!/bin/bash
# Transfer all 24 narrated videos to phone
RENDER_DIR="/root/math-channel/rendered"
PHONE="u0_a391@100.100.168.44"
PHONE_DIR="/sdcard/Download/math-channel"
PORT=8022

echo "=== Transfer Started $(date) ==="

# Create target dir on phone
ssh -p $PORT "$PHONE" "mkdir -p $PHONE_DIR" 2>&1

count=0
fail=0
for f in $RENDER_DIR/Video*_narrated.mp4; do
    name=$(basename "$f")
    echo "[$((count+1))/24] $name..."
    if scp -P $PORT "$f" "$PHONE:$PHONE_DIR/$name" 2>&1; then
        count=$((count+1))
    else
        echo "  FAILED: $name"
        fail=$((fail+1))
    fi
done

echo "=== Done: $count transferred, $fail failed ($(date)) ==="
