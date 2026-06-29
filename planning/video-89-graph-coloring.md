# Video 89: Graph Coloring
## Video 12 of 12 in Discrete Mathematics Playlist

### Competitive Analysis Summary
- Numberphile (2M views): narrative-driven history of the Four Color Theorem, engaging storytelling but light on formal definitions
- Quanta Magazine (259K views): best storytelling with Kempe/Heawood/Appel-Haken narrative, clean animated visuals
- Wrath of Math (134K views): definition-heavy lecture style, covers chromatic number systematically but no animation
- Kimberly Brehm (20K views): slide-based with scheduling application, practical but visually minimal
- Our angle: Animated Manim demonstrations of coloring algorithms — the gap no competitor fills

### Structure (target: 10-12 minutes)

#### Scene 1: Hook — How Many Colors? (45s)
- Physical map puzzle: can you color this map with 3 colors? Show conflicts arise.
- Motivate: scheduling conflicts, frequency assignment, compiler register allocation
- Content budget: simple map diagram + color conflict animation

#### Scene 2: Proper Vertex Coloring (60s)
- Definition: assign colors to vertices so adjacent vertices differ
- Formal definition with MathTex: c: V → {1, 2, ..., k}
- Show a simple example graph with proper 3-coloring
- Content budget: definition text + one small graph with colored vertices

#### Scene 3: Chromatic Number (75s)
- Definition: chi(G) = minimum number of colors needed
- Examples: chi(K_n) = n, chi(C_even) = 2, chi(C_odd) = 3, chi(tree) = 2
- Animate coloring K3 with 3 colors, then show you can't do it with 2
- Content budget: formula + 2-3 small example graphs

#### Scene 4: Bipartite Graphs and 2-Colorability (60s)
- A graph is bipartite iff it is 2-colorable
- Show BFS-level assignment as a constructive 2-coloring proof
- Odd cycle detection: if BFS finds an edge between same-level vertices, not bipartite
- Content budget: BFS tree diagram with level coloring

#### Scene 5: Greedy Coloring Algorithm (90s)
- Algorithm: iterate vertices in some order, assign the smallest available color
- Animate step-by-step on a sample graph with 6-7 vertices
- Show that vertex ordering affects the result (worst case vs best case)
- Upper bound: greedy uses at most max_degree + 1 colors
- Content budget: algorithm text + animated graph coloring sequence

#### Scene 6: The Four Color Theorem (75s)
- Statement: any planar graph can be colored with at most 4 colors
- Equivalent: any map can be colored with 4 colors so no adjacent regions share a color
- Brief historical note: Kempe's flawed proof (1879), Heawood's counterexample (1890), Appel-Haken computer proof (1976)
- Show a map → planar graph dual conversion visually
- Content budget: theorem statement + brief history + one map-to-graph example

#### Scene 7: Applications (45s)
- Exam scheduling: vertices = exams, edges = shared students, colors = time slots
- Register allocation: variables = vertices, interference = edges, colors = registers
- Frequency assignment in cellular networks
- Content budget: application list with one visual example

#### Scene 8: Summary and Outro (30s)
- Key takeaways: proper coloring, chromatic number, greedy algorithm, Four Color Theorem, applications
- Preview next topic (series finale: Discrete Math recap or special topic)
