# Video 88: Planarity and Euler's Formula
## Video 11 of 12 in Discrete Mathematics Playlist

### Competitive Analysis Summary
- Most graph theory channels cover planarity briefly within a broader video
- 3B1B doesn't have a dedicated planarity video — this is a gap we fill
- Key competitor approach: show K5 and K3,3 as counterexamples, prove Euler's formula visually
- Our angle: rigorous but visual — actually show planar embeddings and face counting

### Structure (target: 10-12 minutes)

#### Scene 1: Hook — Can You Draw Without Crossing? (45s)
- Classic puzzle: can you draw a utility graph (K3,3) without edge crossings?
- Real-world motivation: circuit board layout, map coloring
- Content budget: puzzle diagram + question

#### Scene 2: Planar Graphs Definition (60s)
- A graph is planar if it can be drawn in the plane with no edge crossings
- Planar embedding vs isomorphic redrawings
- Examples: K4 is planar (show redraw), K5 is NOT
- Content budget: two graphs side by side

#### Scene 3: Euler's Formula (90s)
- For connected planar graphs: V - E + F = 2
- Where V=vertices, E=edges, F=faces (regions including outer face)
- Visual proof using tree growing argument
- Content budget: formula + example graph with face counting

#### Scene 4: Applications of Euler's Formula (60s)
- Consequences: E ≤ 3V - 6 for simple planar graphs
- K5 has 10 edges but needs ≤ 3(5)-6 = 9 — contradiction!
- K3,3 has 9 edges but needs ≤ 2(6)-4 = 8 for bipartite — contradiction!
- Content budget: inequality derivations

#### Scene 5: Kuratowski's Theorem (75s)
- A graph is planar iff it contains no subdivision of K5 or K3,3
- Subdivision explanation
- Visual examples of subdivisions
- Content budget: K5 and K3,3 diagrams

#### Scene 6: Applications and Summary (45s)
- Map coloring (four color theorem preview)
- Circuit design, graph drawing algorithms
- Preview of final video (Graph Coloring)
