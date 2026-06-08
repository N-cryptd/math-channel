# Video 26: Linear Combinations and Span
## Linear Algebra Playlist — Video 2 of 16
## Estimated Duration: 12-15 minutes

### Learning Objectives
1. Define linear combination of vectors (algebraically and geometrically)
2. Understand and visualize the span of a set of vectors
3. Distinguish between span as a line, a plane, or just {0}
4. Understand linear dependence vs independence through the lens of span
5. See 3D examples: two vectors spanning a plane, three vectors spanning all of R³

### Competitive Analysis References
- **3B1B Chapter 2**: Slider/dial metaphor for coefficients, animate span filling in, show dependence through failed span
- **Khan Academy**: Concrete numerical examples alongside geometry
- **Dr. Trefor Bazett**: Three-case taxonomy (point, line, plane), "you already know these operations" bridge

### Scene Plan

#### Scene 1: Hook + Intro (1:30)
- play_intro("Linear Combinations and Span", "Linear Algebra")
- Bridge from Video 25: "We learned to add vectors and scale them. What if we do both?"
- Motivating question: "What set of points can you reach using only these two operations?"
- Set up the scenario: two vectors, all possible scalars

#### Scene 2: What is a Linear Combination? (2:30)
- Formal definition with notation: c₁v₁ + c₂v₂ + ... + cₙvₙ
- Geometric interpretation on a NumberPlane:
  - Start with vector a (color PRIMARY), vector b (color SECONDARY)
  - Show a specific linear combination: 2a + 1b — animate sliding/scaling
  - Show another: (-1)a + 3b — different result
  - Emphasize: c₁ and c₂ can be ANY real numbers (including negative, zero)
- Show the algebraic notation side-by-side with the geometric picture
- The "slider" idea: imagine dials for c₁ and c₂, the tip of the resulting vector traces out the span

#### Scene 3: Visualizing the Span — Two Independent Vectors (3:00)
- Define span: "The set of ALL possible linear combinations"
- Key emphasis on the word "ALL"
- Animation: sweep c₁ and c₂ through many values, show the resulting vectors filling the plane
- Use UPDATERS or a series of Arrow placements to show many sample combinations
- Visual payoff: the entire 2D plane fills with color, showing span(a,b) = R²
- When vectors are not parallel, their span is the entire plane

#### Scene 4: When Span is Just a Line (2:00)
- Contrast: what if both vectors point in the same direction?
- Show two parallel vectors (e.g., a = (1,2), b = (2,4))
- Animate linear combinations — they all land on the same line through origin
- Introduce the concept: "linearly dependent" vectors
- Key insight: if one vector is a scalar multiple of the other, the span collapses to a line
- Visual: line through origin highlighted, everything off the line is "unreachable"

#### Scene 5: Special Cases — Zero Vector and Single Vector (2:00)
- What is span({0})? Just the origin — nothing moves
- What is span({v}) for a single nonzero vector? A line through the origin
- Connect back to Video 25: "scalar multiples of one vector stay on the same line"
- Three-case taxonomy:
  1. span({0}) = {0} — a single point
  2. span({v}) = line through origin
  3. span({v₁, v₂}) = plane (if independent) or line (if dependent)

#### Scene 6: 3D Preview (1:30)
- Quick 3D scene with three vectors
- Two vectors span a plane (flat sheet in 3D)
- Three independent vectors span all of R³
- Tease: "this pattern continues — the number of independent vectors determines the dimension of the span"
- Tease next video: "How do we describe these operations systematically? With matrices."

#### Scene 7: Summary + Outro (1:30)
- Key takeaways bullet list
- Teaser for Video 27: Matrices as Transformations
- play_outro("Matrices as Transformations", "Linear Algebra")

### Key Formulas / Notation
- Linear combination: c₁v₁ + c₂v₂ where c₁, c₂ ∈ ℝ
- Span: span({v₁, v₂, ...}) = {c₁v₁ + c₂v₂ + ... | cᵢ ∈ ℝ}
- Linear dependence: v₂ = kv₁ for some scalar k

### Visual Elements
- NumberPlane with grid (consistent with Video 25)
- Colored arrows: PRIMARY (#58C4DD) for first vector, SECONDARY (#83C167) for second
- ACCENT (#FFFF00) for the resulting linear combination vector
- Highlight rectangles for formulas
- Fade-in sweep animation for showing the span filling the plane
- Dashed line to show "boundary" of span in degenerate cases

### Color Coding (consistent with Video 25)
- PRIMARY (#58C4DD): first basis vector, x-components, vector a
- SECONDARY (#83C167): second basis vector, y-components, vector b  
- ACCENT (#FFFF00): result vectors, important formulas, key terms
- RED (#FF6B6B): degenerate cases, linearly dependent warnings
- DIM (#888888): grid lines, axis labels, secondary information
