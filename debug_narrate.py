#!/usr/bin/env python3
import re
from pathlib import Path

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

def debug_narrate_logic(starts, duras, naturals):
    n = len(starts)
    # Compute slot_end_i = min(start_i + dur_i, start_{i+1}) for i < n-1, for last: slot_end = start + dur
    slot_ends = []
    for i in range(n):
        if i < n-1:
            slot_end = min(starts[i] + duras[i], starts[i+1])
        else:
            slot_end = starts[i] + duras[i]
        slot_ends.append(slot_end)
    
    print("Idx  Start   Dur   SlotEnd   Natural")
    for i in range(n):
        print(f"{i+1:2d}  {starts[i]:6.2f}  {duras[i]:5.2f}   {slot_ends[i]:6.2f}    {naturals[i]:6.2f}")
    
    # Now simulate narrate.py
    last_end = 0.0
    print("\n--- Narrate.py simulation ---")
    print("Idx  SlotStart SlotEnd  LastEnd+Gap  ActualStart  Avail   Natural  Usage  Speedup  Skip?")
    for i in range(n):
        slot_start = starts[i]
        slot_end = slot_ends[i]
        gap_adjusted_last_end = last_end + MIN_SEGMENT_GAP
        actual_start = max(slot_start, gap_adjusted_last_end)
        avail = slot_end - actual_start
        skip = avail < MIN_SEGMENT_DUR
        if skip:
            usage = 0.0
            speedup = 0.0
            new_last_end = last_end  # unchanged per narrate.py? Actually narrate.py does not update last_end on skip
        else:
            if naturals[i] > 0:
                usage = naturals[i] / avail
                speedup = usage if usage > 1.0 else 0.0
            else:
                usage = 0.0
                speedup = 0.0
            # Update last_end: actual start + tts_dur (after speedup if any)
            # But for defect measurement, we want to see what would happen WITHOUT speedup fix
            # So use natural duration as tts_dur
            new_last_end = actual_start + naturals[i]
        print(f"{i+1:2d}  {slot_start:6.2f}  {slot_end:6.2f}   {gap_adjusted_last_end:6.2f}     {actual_start:6.2f}     {avail:5.2f}   {naturals[i]:6.2f}   {usage:5.2f}   {speedup:5.2f}    {'YES' if skip else 'NO'}")
        last_end = new_last_end

debug_narrate_logic(starts, duras, naturals)