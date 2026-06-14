# Video 65: Phase Portraits

**Playlist:** Differential Equations (Video 12 of 13)
**Estimated duration:** 12 min
**Script file:** `scripts/undergraduate/video-65-phase-portraits.py`
**Class name:** `Video65_PhasePortraits`
**Status:** PLANNING → SCRIPTING

## Competitive Analysis Insights

### 3Blue1Brown — ODE Series (Chapters on Phase Portraits)
- **Approach:** Geometric intuition first — shows trajectories as flowing water/streams in the phase plane
- **Visual technique:** Color-coded arrows (vector fields) that trace solution curves; slow reveal of trajectories from initial conditions
- **Pacing:** Starts with a concrete 2D system, shows that plotting (x, y) vs t gives two separate graphs, then combines into one picture
- **Key insight to adopt:** Emphasize that the phase portrait is a "topographic map" of the system's behavior — you can read the whole story without solving analytically
- **Their weakness:** Very few worked examples; leans heavy on intuition, light on the classification procedure

### Steve Brunton — Dynamical Systems (various lectures)
- **Approach:** More systematic — covers classification of equilibrium points (saddle, node, spiral, center) with clear eigenvalue criteria
- **Visual technique:** Combines vector field plots with eigenvalue analysis; shows how λ₁, λ₂ signs determine the portrait type
- **Pacing:** Lecture-style, moves fast through classification, spends less time on motivation
- **Key insight to adopt:** The eigenvalue classification table (sign of real part, sign of imaginary part) is the anchor — build everything around it
- **Their weakness:** Whiteboard-heavy, limited animation; can feel dry

### Our Approach (Synthesis)
- **Structure:** Concrete 2D system → phase plane concept → vector field visualization → equilibrium classification → worked example → summary
- **Visual metaphors:** (1) Phase plane as a "landscape" with arrows showing flow, (2) equilibrium points as "mountains/valleys/saddles" where flow converges/diverges, (3) Trajectories as rivers flowing through this landscape
- **Color scheme:** PRIMARY (#5BC0EB) for stable trajectories, RED (#EF476F) for unstable, ACCENT (#FFD166) for equilibrium points, SECONDARY (#7BC950) for separatrix lines

## Scene Breakdown

### Scene 1: Hook — Why Phase Portraits? (45s)
**Narration:** "In the last video we saw how to write coupled ODEs in matrix form. But there's a completely different way to understand these systems — one that doesn't require solving anything at all."
- Content budget: 4 items max
- Title: "Phase Portraits" via play_intro()
- Hook question: "What if you could see the entire behavior of a system — every possible solution — in a single picture?"
- Preview: quick flash of a vector field with trajectories (static, no animation)
- ly.clear()

### Scene 2: From Time Series to Phase Plane (90s)
**Narration:** "Let's start with a simple system. Two tanks with flow between them. We can plot each tank's volume versus time — that gives us two separate graphs. But what if we plot them together?"
- Content budget: 5 items
- Show a 2x2 system: dx/dt = -x + y, dy/dt = x - y (two-tank mixing)
- Show separate x(t) and y(t) plots side-by-side (schematic, not actual function plots)
- Combine: (x, y) plane with a single trajectory traced through it
- Key realization: "Each point on this curve is a snapshot of both tanks at one moment in time"
- Introduce term "phase plane" and "phase portrait"
- ly.clear()

### Scene 3: Vector Fields — The Map (120s)
**Narration:** "A phase portrait is more than just one trajectory. It's the vector field — a map of arrows that shows the direction and speed of the system at every point."
- Content budget: 5 items
- Sub-scene 3a: Define the vector field F(x,y) = (f(x,y), g(x,y))
  - Show MathTex: $\vec{F}(x,y) = \langle f(x,y),\, g(x,y) \rangle$
  - Explain: each point (x,y) gets an arrow showing direction of motion
- Sub-scene 3b: Show example arrows being placed (a few representative arrows, not a full field)
  - At (1,0): arrow pointing toward equilibrium
  - At (0,1): arrow pointing toward equilibrium
  - At (2,2): arrow pointing toward equilibrium
- Sub-scene 3c: Trajectories follow the arrows
  - "A solution curve is a path that always follows the arrows — like a leaf floating on a river"
- ly.clear()

### Scene 4: Equilibrium Points — Where Everything Stops (90s)
**Narration:** "Some points in the phase plane have no arrow at all. These are equilibrium points — where both derivatives are zero, and the system stays at rest."
- Content budget: 5 items
- Define equilibrium: f(x*, y*) = 0 and g(x*, y*) = 0
  - MathTex: $f(x^*, y^*) = 0$ and $g(x^*, y^*) = 0$
- Visual: equilibrium point shown as a prominent dot (ACCENT color)
- Trajectories that reach equilibrium: "If you start at an equilibrium, you stay there forever"
- Trajectories near equilibrium: arrows point toward or away — preview of classification
- ly.clear()

### Scene 5: Section Divider — Classification (10s)
- ly.section_divider(5, "Classifying Equilibria")
- ly.clear()

### Scene 6: The Classification Table (150s)
**Narration:** "The behavior near an equilibrium point depends entirely on the eigenvalues of the Jacobian matrix evaluated at that point."
- Content budget: 5 items
- Sub-scene 6a: The Jacobian matrix
  - MathTex: $J = \begin{pmatrix} \partial f/\partial x & \partial f/\partial y \\ \partial g/\partial x & \partial g/\partial y \end{pmatrix}$
  - Explain: "This matrix captures how the vector field changes near the equilibrium"
- Sub-scene 6b: Eigenvalues determine the type (progressive_reveal a table)
  - Both real, both negative → Stable Node (PRIMARY)
  - Both real, both positive → Unstable Node (RED)
  - Both real, opposite signs → Saddle Point (RED/PRIMARY mix)
  - Complex, negative real part → Stable Spiral (PRIMARY)
  - Complex, positive real part → Unstable Spiral (RED)
  - Complex, zero real part → Center (SECONDARY)
- Sub-scene 6c: Visual sketch for each type (one at a time, remove previous)
  - For each: show equilibrium dot + representative arrows/trajectories
- ly.clear()

### Scene 7: Worked Example — Two-Tank System (120s)
**Narration:** "Let's put this into practice with our two-tank system from earlier."
- Content budget: 5 items
- System: dx/dt = -x + y, dy/dt = x - y
- Step 1: Find equilibria: x* = y*, and -x + y = 0 → all points on x = y (line of equilibria)
  - Actually, let me use a better example: dx/dt = -2x + y, dy/dt = x - 2y
  - Equilibrium: -2x + y = 0 and x - 2y = 0 → x = 0, y = 0
- Step 2: Jacobian: J = [[-2, 1], [1, -2]]
- Step 3: Eigenvalues: λ² + 4λ + 3 = 0 → λ₁ = -1, λ₂ = -3 (both real, both negative)
- Step 4: Classification → Stable Node
- Step 5: Visual sketch (arrows pointing inward)
- ly.clear()

### Scene 8: Nullclines — Reading the Landscape (60s)
**Narration:** "There's a shortcut for sketching phase portraits without computing eigenvalues: nullclines."
- Content budget: 5 items
- Define: x-nullcline (where dx/dt = 0) and y-nullcline (where dy/dt = 0)
- On the x-nullcline, all arrows are vertical (no horizontal component)
- On the y-nullcline, all arrows are horizontal (no vertical component)
- Where they cross → equilibrium points
- Quick example with the worked system
- ly.clear()

### Scene 9: Summary and Outro (45s)
**Narration recap:** "Phase portraits give us a complete picture of a system's behavior without solving any equations."
- Content budget: 5 items
- Key takeaways (progressive_reveal):
  1. Phase plane = (x, y) space where trajectories live
  2. Vector field shows direction at every point
  3. Equilibrium points are where the flow stops
  4. Eigenvalues of Jacobian classify the equilibrium type
  5. Nullclines help sketch without computing eigenvalues
- play_outro() — tease "Numerical Methods (Euler, RK4)"
- ly.clear()

## Technical Notes
- For vector field visualization: use Manim `Arrow` objects placed on a grid (don't use actual `StreamPlot` or continuous fields — too complex for 480p)
- Trajectory sketches: use `ParametricFunction` or `VMobject` with `set_points_smoothly`
- Classification table: use ly.stack_down() with color-coded entries
- Jacobian matrix: use MathTex with `pmatrix`
- Keep visual complexity low — schematic sketches, not photorealistic phase portraits
