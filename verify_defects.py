#!/usr/bin/env python3
# Recreate narrate.py slot logic to verify defect rows
MIN_SEGMENT_GAP = 0.3
MIN_SEGMENT_DUR = 1.5

# Data from SRT parse + natural TTS measurement
starts = [0.00, 6.27, 11.70, 18.73, 20.40, 28.03, 29.23, 30.90, 33.90, 38.73, 52.13, 57.43, 68.33, 73.03, 86.23, 87.93, 90.13, 93.63, 106.13, 114.43]
duras = [8.00, 12.00, 6.00, 10.00, 8.00, 15.00, 6.00, 6.00, 8.00, 14.00, 12.00, 12.00, 8.00, 16.00, 10.00, 8.00, 8.00, 12.00, 5.00, 10.00]
naturals = [6.55, 9.26, 5.71, 6.79, 6.98, 8.90, 3.62, 3.46, 4.68, 10.54, 6.19, 9.26, 4.27, 12.55, 6.94, 6.96, 6.67, 8.98, 2.71, 8.47]
captions = [
    "Welcome to Linear Algebra. Today we answer a fundamental question: what exactly is a vector?",
    "Vectors show up everywhere: physics uses them for forces and velocity, computer graphics for positions, and data science for features.",
    "At their core, a vector is simply a quantity with both magnitude and direction.",
    "Let's start with the most intuitive picture. On a number line, a vector is just a displacement from zero.",
    "This arrow represents the number 3. It tells us: start at zero and move 3 units to the right.",
    "To work with vectors mathematically, we describe them using components. Every vector can be broken down into an x-part and a y-part.",
    "The x-component is 2, the horizontal distance.",
    "The y-component is 3, the vertical distance.",
    "We write the vector as a column: v equals the column 2, 3.",
    "Equivalently, v equals 2 times i-hat plus 3 times j-hat. I-hat is the unit vector along x. J-hat is the unit vector along y.",
    "How long is a vector? The magnitude, or length, comes straight from the Pythagorean theorem.",
    "The magnitude of v is the square root of x squared plus y squared. For our 3-4-5 triangle, that gives us exactly 5.",
    "How do we add two vectors? The rule is simple: tip to tail.",
    "Now we move vector b so its tail sits at the tip of vector a. Think of it like walking: first walk along a, then walk along b. Component-wise, we just add the x's and add the y's.",
    "What happens when we multiply a vector by a plain number, called a scalar? It stretches or flips the vector.",
    "Multiply by 2: the vector stretches to twice its length, same direction. Each component gets doubled.",
    "Multiply by negative 1: the vector flips to point the opposite way. Same length, opposite direction.",
    "All scalar multiples of a vector lie on the same line through the origin. This is a crucial insight that we will build on throughout linear algebra.",
    "Let's recap what we've learned about vectors.",
    "But what if we combine scalars and vectors freely? What set of points can we reach? That is the span, and it is the topic of our next video."
]

# Compute slot_end_i = min(start_i + dur_i, start_{i+1}) for i < n-1, for last: slot_end = start + dur
n = len(starts)
slot_ends = []
for i in range(n):
    if i < n-1:
        slot_end = min(starts[i] + duras[i], starts[i+1])
    else:
        slot_end = starts[i] + duras[i]
    slot_ends.append(slot_end)

# Now compute available_i per narrate.py
last_end = 0.0
avails = []
actual_starts = []
usage = []
speedups = []
skips = []
for i in range(n):
    slot_start = starts[i]
    slot_end = slot_ends[i]
    actual_start = max(slot_start, last_end + MIN_SEGMENT_GAP)
    actual_starts.append(actual_start)
    avail = slot_end - actual_start
    avails.append(avail)
    if avail < MIN_SEGMENT_DUR:
        skips.append(True)
        usage.append(0.0)
        speedups.append(0.0)
    else:
        skips.append(False)
        if naturals[i] > 0:
            u = naturals[i] / avail
            usage.append(u)
            speedups.append(u if u > 1.0 else 0.0)  # speedup factor if >1x
        else:
            usage.append(0.0)
            speedups.append(0.0)
    # Update last_end if not skipped
    if not skips[i]:
        last_end = actual_start + naturals[i]  # tts_dur after speedup? Actually narrate.py recalculates after speedup, but for usage calc we use natural
        # For simplicity, we assume no speedup yet in this analysis (we're measuring current state)
        # To match defect rows, we should use the natural duration as the tts_dur (since no speedup applied yet in measurement)
        # Actually the defect rows are from the *original* render without any speedup fix, so tts_dur = natural
        # So last_end should be actual_start + natural
        last_end = actual_start + naturals[i]
    else:
        # skipped, last_end unchanged? Actually narrate.py: if skipped, it doesn't update last_end? Let me check.
        # In narrate.py: if available < MIN_SEGMENT_DUR: log skip and continue (does not update last_end)
        pass

# Print table
print("Idx  Start   Dur   Natural  Slot_End  Actual_Start  Avail   Usage   Speedup  Skip?  Caption (truncated)")
print("="*120)
for i in range(n):
    print(f"{i+1:2d}  {starts[i]:6.2f}  {duras[i]:5.2f}  {naturals[i]:6.2f}   {slot_ends[i]:6.2f}    {actual_starts[i]:6.2f}     {avails[i]:5.2f}   {usage[i]:5.2f}   {speedups[i]:5.2f}    {'YES' if skips[i] else 'NO'}   {captions[i][:40]}")

# Compare to defect rows from card:
# Defect rows (seg# slot/avail/nat sec → speedup):
# #0 6.27/5.97/6.55 1.10x; #1 5.43/5.13/9.26 1.80x; #3 1.67/1.37/6.79 4.97x SKIPRISK; #4 7.63/7.33/6.98 0.95x(slot<1.08nat+0.3); #5 1.20/0.90/8.90 9.89x SKIPRISK; #6 1.67/1.37/3.62 2.65x SKIPRISK; #7 3.00/2.70/3.46 1.28x; #8 4.83/4.53/4.68 1.03x; #10 5.30/5.00/6.19 1.24x; #12 4.70/4.40/4.27 0.97x; #13 13.20/12.90/12.55 0.97x; #14 1.70/1.40/6.94 4.95x SKIPRISK; #15 2.20/1.90/6.96 3.66x; #16 3.50/3.20/6.67 2.08x.
print("\n\nDefect rows from card (1-indexed seg#):")
print("Idx  Card_slot  Card_avail  Card_nat  Card_speedup  Our_slot  Our_avail  Our_nat  Our_speedup  Match?")
print("-"*90)
# Map card indices to our indices (card #0 = our idx0, etc.)
card_data = [
    (0, 6.27, 5.97, 6.55, 1.10),
    (1, 5.43, 5.13, 9.26, 1.80),
    (2, None, None, None, None),  # #2 not listed in card? Actually card #2 is missing; they went #0,#1,#3...
    (3, 1.67, 1.37, 6.79, 4.97),
    (4, 7.63, 7.33, 6.98, 0.95),
    (5, 1.20, 0.90, 8.90, 9.89),
    (6, 1.67, 1.37, 3.62, 2.65),
    (7, 3.00, 2.70, 3.46, 1.28),
    (8, 4.83, 4.53, 4.68, 1.03),
    (9, None, None, None, None),  # #9 missing
    (10,5.30,5.00,6.19,1.24),
    (11,None,None,None,None),  # #11 missing
    (12,4.70,4.40,4.27,0.97),
    (13,13.20,12.90,12.55,0.97),
    (14,1.70,1.40,6.94,4.95),
    (15,2.20,1.90,6.96,3.66),
    (16,3.50,3.20,6.67,2.08),
    (17,None,None,None,None),  # #17 missing
    (18,None,None,None,None),  # #18 missing
    (19,None,None,None,None)   # #19 missing
]
for card_idx, card_slot, card_avail, card_nat, card_speed in card_data:
    if card_idx is None or card_slot is None:
        continue
    our_idx = card_idx  # same numbering
    if our_idx >= n:
        continue
    match = (abs(slot_ends[our_idx] - card_slot) < 0.02 and 
             abs(avails[our_idx] - card_avail) < 0.02 and
             abs(naturals[our_idx] - card_nat) < 0.02 and
             abs((speedups[our_idx] if speedups[our_idx] > 0 else usage[our_idx]) - card_speed) < 0.02)
    print(f"{our_idx+1:2d}  {card_slot:6.2f}   {card_avail:6.2f}   {card_nat:6.2f}      {card_speed:6.2f}       {slot_ends[our_idx]:6.2f}   {avails[our_idx]:6.2f}   {naturals[our_idx]:6.2f}      {(speedups[our_idx] if speedups[our_idx] > 0 else usage[our_idx]):6.2f}    {'YES' if match else 'NO'}")