# Video 25: What is a Vector? (Geometric)

## Playlist
Linear Algebra — Video 1 of 16

## Target Duration
12 minutes

## Competitive Analysis Reference
Based on 3B1B "Vectors | Chapter 1" (11.7M views):
- Geometric-first approach (arrows before numbers)
- Color-coded basis vectors (PRIMARY = x-hat, SECONDARY = y-hat)
- Animate vectors growing from origin
- Grid backgrounds for visual clarity
- End with algebraic perspective as teaser

Unlike 3B1B's minimalist approach, we include formal notation alongside intuition.

## Scene Breakdown

### Scene 1: Hook + Intro (45s)
- Play ChannelIntro("What is a Vector?", "Linear Algebra")
- Opening question: "What exactly IS a vector?"
- Show three contexts where vectors appear: physics (force/velocity), computer graphics (position), data science (features)
- Key point: a vector is fundamentally a quantity with both magnitude AND direction

### Scene 2: The Geometric View — Arrows in Space (2 min)
- Start with a single point on a number line
- "A vector on a number line is just a displacement"
- Animate: a dot at the origin, then an arrow growing to a point
- Label: "this arrow represents the number 3"
- Transition: "But in 2D, things get interesting"
- Show a 2D plane with grid, arrow from origin to point (2, 3)
- This is a vector — it has a direction and a length

### Scene 3: Components — Describing a Vector with Numbers (2 min)
- Same 2D vector on screen
- Drop perpendicular lines to x-axis and y-axis
- "We can describe this arrow using its components"
- Show x-component (horizontal) and y-component (vertical)
- Notation: v = (2, 3) or v⃗ = [2, 3]^T
- Color-code: x-component in PRIMARY, y-component in SECONDARY
- Key formula: v⃗ = x·î + y·ĵ

### Scene 4: Vector Magnitude (Length) (1.5 min)
- "How long is this arrow?"
- Visual: measure the arrow with a ruler animation
- Formula: |v⃗| = √(x² + y²) — Pythagorean theorem connection
- Quick example: |(3, 4)| = 5
- Show 3-4-5 triangle forming under the vector
- "The magnitude is just the hypotenuse!"

### Scene 5: Vector Addition — Tip to Tail (2 min)
- "How do we add two vectors?"
- Show two vectors from origin: a⃗ = (2, 1) and b⃗ = (1, 3)
- Animate: move b⃗ so its tail sits at the tip of a⃗
- Result: arrow from origin to the new tip
- "The sum a⃗ + b⃗ connects the origin to the final tip"
- Show parallelogram rule briefly as alternative view
- Component-wise: (2,1) + (1,3) = (3, 4)
- Real-world analogy: "Walk 2 right, 1 up, then 1 right, 3 up"

### Scene 6: Scalar Multiplication — Stretching and Flipping (1.5 min)
- "What happens if we multiply a vector by a number?"
- Show v⃗ = (2, 1)
- Multiply by 2: arrow stretches to (4, 2) — same direction, twice as long
- Multiply by 0.5: arrow shrinks to (1, 0.5)
- Multiply by -1: arrow flips to (-2, -1) — opposite direction
- Key visual: all scaled vectors lie on the same line through the origin
- "Scalar multiplication changes magnitude and possibly direction, but never changes the 'line' the vector lives on"

### Scene 7: Summary + Teaser (1.5 min)
- Key takeaways:
  1. A vector has magnitude and direction
  2. We describe vectors using components: v⃗ = (x, y)
  3. Addition: tip-to-tail, component-wise
  4. Scalar multiplication: stretches/flips
  5. |v⃗| = √(x² + y²)
- Teaser: "But what if we combine scalars and vectors freely? What set of points can we reach? That's the span — and it's the topic of our next video."
- Play ChannelOutro("Linear Combinations and Span", "Linear Algebra")

## Visual Design Notes
- Grid background throughout (NumberPlane with dimmed grid lines)
- Basis vector colors: î in PRIMARY (#58C4DD), ĵ in SECONDARY (#83C167)
- General vectors in ACCENT (#FFFF00) or WHITE
- Scalars in RED (#FF6B6B)
- Vectors animated from origin (Create with tip growing outward)
- Component projections shown as dashed lines
- Consistent arrow tips on all vector arrows

## LaTeX Reference (single backslash in raw strings)
- r"\vec{v}" — vector notation
- r"\hat{\imath}", r"\hat{\jmath}" — basis vectors
- r"\sqrt{x^2 + y^2}" — magnitude
- r"\vec{a} + \vec{b}" — addition
- r"2\vec{v}" — scalar multiplication
