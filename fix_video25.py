#!/usr/bin/env python3
import re
from pathlib import Path

# Natural TTS durations we measured (in order)
naturals = [6.55, 9.26, 5.71, 6.79, 6.98, 8.90, 3.62, 3.46, 4.68, 10.54, 6.19, 9.26, 4.27, 12.55, 6.94, 6.96, 6.67, 8.98, 2.71, 8.47]

# Read the original script
script_path = Path("~/math-channel/scripts/undergraduate/video-25-what-is-a-vector.py").expanduser()
original = script_path.read_text()

# 1. Ensure scene2c_2d_view is called in construct()
# Find the construct method and insert after scene2_geometric_view()
# We'll do a simple replacement: after "self.scene2_geometric_view()" insert "\n        self.scene2c_2d_view()"
# But we need to be careful about indentation.
# Let's do a more robust replacement using regex.

# First, let's see if scene2c_2d_view is already called (it shouldn't be)
if "self.scene2c_2d_view()" in original:
    print("scene2c_2d_view already called")
else:
    # Insert after scene2_geometric_view line
    # Find the line containing self.scene2_geometric_view()
    lines = original.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.strip() == "self.scene2_geometric_view()":
            # Insert the call after this line, same indentation
            indent = len(line) - len(line.lstrip())
            new_lines.append(" " * indent + "self.scene2c_2d_view()")
    original = '\n'.join(new_lines)
    print("Added call to scene2c_2d_view()")

# 2. Map each add_subcaption to its natural duration
# We'll find all add_subcaption calls and replace their duration argument.
# Pattern: self.add_subcaption( ... , duration=X, ... ) or self.add_subcaption( ... , X, ... )
# The duration is either the second positional argument or a keyword argument.
# To keep it simple, we'll assume the duration is the second argument (after the text).
# Looking at the script, they all use: self.add_subcaption(\n    \"\"\"...\"\"\",\n    duration=Y,\n)
# So we can replace the duration=Y part.

# Let's find all add_subcaption blocks and replace the duration.
# We'll do it by finding the text and the duration number separately.

# First, extract all captions in order to map index to natural.
# We'll reuse the caption list from earlier.
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

# Verify we have 21 captions now (with scene2c included)
print(f"Expecting 21 captions, have {len(captions)}")

# Function to replace duration in an add_subcaption call
def replace_duration_in_add_subcaption(match, caption_idx):
    # match group 0: entire add_subcaption(...) call
    # We'll replace the duration=X or the second argument
    text = match.group(0)
    # Look for duration= followed by number
    # Pattern: duration=\s*(\d+\.?\d*)
    def repl_duration(m):
        # m.group(1) is the current duration value
        cur_dur = float(m.group(1))
        # We want to set it to at least natural * 1.2 (to give plenty of room)
        # But also we don't want to make it unreasonably long; cap at maybe 20s?
        target = naturals[caption_idx] * 1.2
        # If current duration is already >= target, keep it
        if cur_dur >= target:
            return m.group(0)  # keep original
        else:
            # Replace with target, rounded to 1 decimal
            new_dur = round(target, 1)
            # Ensure we don't go below a minimum of 2.0s maybe
            new_dur = max(new_dur, 2.0)
            return f'duration={new_dur}'
    # Replace duration=X
    text = re.sub(r'duration\s*=\s*(\d+\.?\d*)', repl_duration, text)
    # Also handle if duration is second positional argument: ... , X, )
    # This is trickier; we'll assume keyword form for simplicity.
    # Looking at the script, they all use duration= keyword.
    return text

# Apply the replacement for each add_subcaption call
# We need to know the caption index for each match.
# We'll find all matches and replace them in order.
pattern = r'self\.add_subcaption\s*\([^)]*\)'
matches = list(re.finditer(pattern, original, re.DOTALL))
print(f"Found {len(matches)} add_subcaption calls")

# We'll process from the end to avoid index shifting when replacing
# But since we're replacing duration only and not changing length much, we can do forward.
# Actually to be safe, we'll build a new string by replacing matches from the end.
parts = []
last_end = 0
for idx, match in enumerate(matches):
    if idx >= len(captions):
        print(f"Warning: more add_subcaption calls ({len(matches)}) than captions ({len(captions)}). Using last caption's natural.")
        caption_idx = len(captions) - 1
    else:
        caption_idx = idx
    parts.append(original[last_end:match.start()])
    parts.append(replace_duration_in_add_subcaption(match, caption_idx))
    last_end = match.end()
parts.append(original[last_end:])
original = ''.join(parts)
print("Updated add_subcaption durations to be at least 1.2x natural TTS")

# 3. Increase wait times before ly.clear()
# We'll look for ly.clear() calls and adjust the wait time in the preceding statement.
# Pattern: look for lines like:
#   self.wait(X.X)
#   self.ly.clear()
# or
#   self.ly.clear(run_time=X.X)
# We'll increase X.X by 2.0 seconds.
#
# Approach: scan lines, when we see ly.clear(), look backward for a wait() call.
# If found, increase its argument by 2.0.
# If not found, insert a wait(2.0) line before ly.clear().

lines = original.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i].rstrip()
    new_lines.append(line)
    if 'ly.clear()' in line and 'self.ly.clear()' in line:
        # Look backward for a wait() call in the previous non-empty line(s)
        j = len(new_lines) - 2  # start from line before the one we just added
        while j >= 0 and new_lines[j].strip() == '':
            j -= 1
        if j >= 0 and 'wait(' in new_lines[j] and 'self.wait(' in new_lines[j]:
            # Found a wait call, increase its argument
            wait_line = new_lines[j]
            # Find the argument inside wait( ... )
            # Pattern: self.wait( NUMBER )
            m = re.search(r'self\.wait\(\s*(\d+\.?\d*)\s*\)', wait_line)
            if m:
                cur_val = float(m.group(1))
                new_val = cur_val + 2.0
                # Replace the argument
                new_wait_line = re.sub(r'self\.wait\(\s*\d+\.?\d*\s*\)', f'self.wait({new_val})', wait_line)
                new_lines[j] = new_wait_line
                print(f"Increased wait from {cur_val} to {new_val} at line {j+1}")
            else:
                # No numeric argument found, just add a wait(2.0) before
                indent = len(line) - len(line.lstrip())
                new_lines.insert(i, ' ' * indent + f'wait(2.0)')
                print(f"Inserted wait(2.0) before ly.clear() at line {i+1}")
                i += 1  # skip the line we just added
        else:
            # No wait call found, insert one before
            indent = len(line) - len(line.lstrip())
            new_lines.insert(i, ' ' * indent + f'wait(2.0)')
            print(f"Inserted wait(2.0) before ly.clear() at line {i+1}")
            i += 1
    i += 1

original = '\n'.join(new_lines)

# Write the fixed script
fixed_path = Path("~/math-channel/scripts/undergraduate/video-25-what-is-a-vector_fixed.py").expanduser()
fixed_path.write_text(original)
print(f"\nFixed script written to {fixed_path}")

# Also, let's create a diff to see what changed
import subprocess
result = subprocess.run(['diff', '-u', str(script_path), str(fixed_path)], capture_output=True, text=True)
if result.stdout:
    print("\n--- Diff (original -> fixed) ---")
    print(result.stdout)
else:
    print("\nNo differences found.")