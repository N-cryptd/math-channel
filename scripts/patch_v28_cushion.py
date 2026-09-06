#!/usr/bin/env python3
"""Apply 0.7s pacing cushion to Video 28 pacing waits (t_aa9f7542).

The prior attempt's waits land 0.00-0.10s over the audit minimum
(1.08*natural + 0.3). Frame quantization at 480p15 (1/15s = 0.067s)
makes those margins unsafe. This patch adds +0.7s cushion everywhere,
landing slots at ~1.15-1.3x natural (recipe target ~1.25x).

Also fixes caption 27 (last): its slot = min(declared_end, video_end)
so declared must be >= 1.08*nat+0.3 = 8.75 -> declared 7.9 -> 9.0,
and its trailing wait 0.7 -> 2.0 keeps video_end >= declared.
"""
import re
import sys

PATH = "/root/math-channel/scripts/undergraduate/video-28-matrix-multiplication.py"

# caption N -> (natural_s, old_slot_s from audit t_475b35a7, old_wait_expected_in_file)
# For N=24 the wait(0.8) was ADDED (not replacing anything), for N=27 wait(0.7) added.
AUDIT = {
    2:  (11.74, 3.00, 10.5),
    3:  (5.30,  3.67, 3.4),
    4:  (6.98,  4.03, 5.2),
    5:  (9.89,  5.03, 9.0),
    6:  (8.33,  5.03, 5.8),
    7:  (10.10, 1.67, 10.1),
    8:  (8.78,  3.03, 7.8),
    9:  (9.12,  4.83, 7.4),
    10: (11.86, 4.83, 10.3),
    11: (8.98,  4.23, 7.3),
    12: (9.19,  4.30, 7.5),
    13: (7.54,  7.00, 3.5),
    14: (11.52, 3.55, 10.2),
    15: (11.40, 4.60, 9.6),
    16: (7.68,  4.80, 5.8),
    17: (8.38,  6.15, 4.3),
    18: (9.62,  4.30, 7.9),
    19: (5.81,  4.30, 3.8),
    20: (6.84,  4.60, 5.1),
    21: (8.47,  4.65, 5.8),
    22: (6.22,  3.50, 5.1),
    23: (9.14,  9.00, 3.2),
    24: (6.31,  6.35, 0.8),   # added by attempt; effective added wait = new value
    25: (10.18, 2.80, 10.5),
    26: (8.64,  7.25, 3.4),
    27: (7.82,  8.15, 0.7),   # added by attempt; slot comes from min(declared, video_end)
}
CUSHION = 0.7

with open(PATH) as f:
    src = f.read()

pat = re.compile(r"self\.wait\(([\d.]+)\)  # pacing: extends caption (\d+) slot")
lines = src.split("\n")
out = []
report = []
errors = []
seen = set()

for line in lines:
    m = pat.search(line)
    if not m:
        out.append(line)
        continue
    n = int(m.group(2))
    seen.add(n)
    if n not in AUDIT:
        errors.append(f"caption {n}: not in audit table")
        out.append(line)
        continue
    nat, old_slot, expected_old = AUDIT[n]
    old_val = float(m.group(1))
    if abs(old_val - expected_old) > 1e-9:
        errors.append(f"caption {n}: wait in file {old_val} != expected {expected_old}")
        out.append(line)
        continue
    if n == 27:
        new_val = 2.0  # covers video_end path: 8.15 + 2.0 = 10.15 >= declared 9.0
        slot_new = min(9.0, old_slot + new_val)
    elif n == 24:
        new_val = round(old_val + CUSHION, 1)  # 0.8 -> 1.5; all of it extends the slot
        slot_new = old_slot + new_val
    else:
        new_val = round(old_val + CUSHION, 1)
        slot_new = old_slot + (new_val - expected_old)
    need = 1.08 * nat + 0.3
    margin = slot_new - need
    if margin < 0.3:
        errors.append(f"caption {n}: slot {slot_new:.2f} < need {need:.2f} + 0.3 cushion (margin {margin:.2f})")
    report.append(
        f"cap{n:>2}: wait {old_val:>5} -> {new_val:>5}  nat {nat:>5}  "
        f"slot {old_slot:>5} -> {slot_new:>6.2f}  need {need:>6.2f}  margin +{margin:.2f}  "
        f"ratio {slot_new / nat:.2f}x"
    )
    out.append(line.replace(
        f"self.wait({m.group(1)})  # pacing: extends caption {n} slot",
        f"self.wait({new_val})  # pacing: extends caption {n} slot (natural {nat}s, slot {old_slot}->{slot_new:.2f}s, min {need:.2f}s)",
    ))

# Caption 27 declared duration 7.9 -> 9.0 (unique by context)
cap27_pat = re.compile(r'("Next time, we will learn about determinants\.\.\.", duration=)7\.9')
joined = "\n".join(out)
if not cap27_pat.search(joined):
    errors.append("caption 27 declared duration=7.9 not found at expected context")
else:
    joined = cap27_pat.sub(r"\g<1>9.0", joined)
    report.append("cap27: declared duration 7.9 -> 9.0 (last-caption slot = min(declared, video_end))")

missing = set(AUDIT) - seen
if missing:
    errors.append(f"pacing waits not found for captions: {sorted(missing)}")
if len(pat.findall(src)) != 26:
    errors.append(f"expected 26 pacing wait lines, found {len(pat.findall(src))}")

if errors:
    print("ABORT — file NOT modified:")
    for e in errors:
        print("  ERROR:", e)
    sys.exit(1)

with open(PATH, "w") as f:
    f.write(joined)

print("\n".join(report))
total = sum(v[0] for v in AUDIT.values())
print(f"\nOK: 27 waits updated, cap27 declared 9.0. All margins >= 0.3s, ratios 1.15-1.37x.")
print(f"Expected final narration sum ~{total:.0f}s natural.")
