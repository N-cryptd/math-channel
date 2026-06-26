# Video 86: Graph Theory Basics
## Discrete Mathematics -- Video 9 of 12

**Predecessor:** Video 85 (Pigeonhole Principle)  
**Next:** Video 87 (Trees)

### Competitive Analysis

Analyzed 3 competitor videos (2026-06-25):

- **Reducible**: "Graph Theory Basics" (~450K views, Mar 2023). Clean node/edge animations but lacks depth in proofs. 7/10 structure, 6/10 pacing, 8/10 visuals, 7/10 narration, 6/10 hooks.
- **William Fiset**: "Graph Theory Tutorial Series" (~180K views, Jan 2022). CS/algorithm-focused with pseudocode. 8/10 structure, 7/10 pacing, 6/10 visuals, 7/10 narration, 5/10 hooks.
- **Abdul Bari**: "Graph Theory Introduction" (~320K views, Oct 2020). Whiteboard-style with minimal animation. 6/10 structure, 5/10 pacing, 5/10 visuals, 6/10 narration, 4/10 hooks.

**KEY GAP:** No competitor uses Manim's full potential for dynamic graph transformations or visual proofs of theorems like the Handshaking Lemma. All start with dry definitions without motivational hooks.

### Key Differentiators
1. **Motivational hook**: Open with the Seven Bridges of Königsberg problem (Euler's original motivation)
2. **Dynamic animations**: Show graphs being built/altered in real-time (adding vertices/edges)
3. **Visual proof of Handshaking Lemma**: Animate each edge contributing 2 to the degree sum
4. **Algorithm visualization**: Step-by-step BFS/DFS with queue/stack evolution
5. **Real-world connections**: Social networks, road maps, molecular structures
6. **Interactive engagement**: Prompts like "Can you spot the cycle?" to maintain attention

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Vertices / nodes | PRIMARY | #5BC0EB |
| Edges / connections | SECONDARY | #7BC950 |
| Highlighted / active | ACCENT | #FFD166 |
| Visited (in algorithms) | ACCENT | #FFD166 |
| Path / cycle | ACCENT | #FFD166 |
| Weighted edges | RED | #EF476F |
| Labels / weights | WHITE | #FFFFFF |
| Background grid | DIM | #6B6B8D |

### Structure (15 minutes, 8 scenes)

**Scene 1 -- Hook: The Seven Bridges of Königsberg (2:00)**
- "In 1736, the people of Königsberg posed a simple question: Can you walk through the city, crossing each of its seven bridges exactly once?"
- Visual: Animated map of Königsberg with Pregel River, four land masses, seven bridges
- Euler's insight: Abstract to nodes (land masses) and edges (bridges) - birth of graph theory
- Bridge: This abstraction lets us solve seemingly impossible problems with simple rules
- Content budget: Map + river + land masses + bridges + question text

**Scene 2 -- Basic Definitions (2:00)**
- Section divider: "What is a Graph?"
- Formal definition: Graph G = (V, E) where V = vertices, E = edges
- Visual: Empty space → dots appear (vertices) → lines connect them (edges)
- Simple example: Social network (people = vertices, friendships = edges)
- Key terms: vertex, edge, adjacent, degree, loop, multiple edges
- Visual: Highlight degree of vertices with incoming/outgoing edge counters
- Content budget: Definition text + 2-3 example graphs + degree labels

**Scene 3 -- Graph Types and Properties (2:00)**
- Section divider: "Types of Graphs"
- Undirected vs directed (arrows on edges)
- Weighted vs unweighted (numbers on edges)
- Simple vs multigraph vs pseudograph (loops/multiple edges)
- Connected vs disconnected (can you reach everywhere?)
- Visual: Transform same vertex set to show different edge types
- Examples: Road networks (undirected), Twitter follows (directed), flight distances (weighted)
- Content budget: 4-5 small graphs showing different types + labels

**Scene 4 -- Representing Graphs (2:00)**
- Section divider: "How We Store Graphs"
- Edge list: [(A,B), (B,C), (C,A)] - simple but inefficient lookup
- Adjacency matrix: NxN grid, 1 if connected, 0 otherwise - good for dense graphs
- Adjacency list: Each vertex stores list of neighbors - good for sparse graphs
- Visual: Same graph shown with all three representations side-by-side
- Trade-offs: Space vs time for different operations (add edge, check edge, neighbors)
- Content budget: Three side-by-side representations + complexity annotations

**Scene 5 -- The Handshaking Lemma (2:00)**
- Section divider: "A First Theorem: The Handshaking Lemma"
- Statement: Sum of all vertex degrees = 2 × |E| (twice the number of edges)
- Intuition: Each edge contributes 1 to the degree of TWO vertices
- Visual proof: Animate each edge lighting up, adding +1 to each endpoint's degree counter
- Example: Apply to a small graph, compute both sides to verify
- Corollary: Number of odd-degree vertices is always even (important for Euler paths)
- Visual: Highlight odd-degree vertices, show they come in pairs
- Content budget: Theorem text + animated proof + example verification + corollary

**Scene 6 -- Graph Traversal: BFS and DFS (3:00)**
- Section divider: "Exploring Graphs: Breadth-First Search"
- Problem: Find shortest path or visit all nodes efficiently
- BFS intuition: Explore in "layers" - friends, then friends-of-friends, etc.
- Visual: Queue animation + highlighting of discovered nodes level-by-level
- Pseudocode: Initialize queue, mark start, while queue not empty...
- Transition to DFS: "What if we went deep before going wide?"
- Visual: Stack animation + depth-first exploration with backtracking
- Contrast: BFS finds shortest path (unweighted), DFS explores deeply first
- Content budget: Algorithm pseudocode + animated traversal + queue/stack visualization

**Scene 7 -- Applications and Connections (2:00)**
- Section divider: "Where Graphs Appear Everywhere"
- Social networks: Influence detection, community finding
- Transportation: Shortest paths (GPS), network flow (airlines)
- Biology: Protein interactions, food webs, neural networks
- Computer science: Dependency trees, garbage collection, routing algorithms
- Puzzle connection: Sudoku as graph coloring, mazes as spanning trees
- Visual: Quick montage of 4-5 real-world graphs with brief explanations
- Bridge: "Next time we'll see how trees (special graphs) simplify many problems"
- Content budget: 4-5 application icons/examples with labels

**Scene 8 -- Summary and Preview (1:00)**
- Recap: Vertices, edges, degree, representations, Handshaking Lemma, BFS/DFS
- "We've seen how graphs model relationships, and how to explore them efficiently, and appear everywhere."
- Preview: "Next: Trees - connected graphs without cycles. Why they're special and everywhere."
- Visual: Graph → remove cycles → tree transformation animation
- Call-to-action: "Like if you enjoyed seeing math come alive, subscribe for more visual proofs!"
- Content brief: Summary points + transition animation + subscribe reminder

### Production Notes
- Start with Königsberg problem IMMEDIATELY - no dry definitions first
- Every definition must be accompanied by a visual example being built
- Use progressive disclosure: show simple examples before complex ones
- Animate ALL proofs - never just state a theorem without visual justification
- Keep vertex/edge counts small (≤6 vertices) for clarity unless showing scale
- Use consistent object permanence: vertices don't jump around unexpectedly
- For algorithms, show data structures (queue/stack) evolving alongside the graph
- End with clear bridge to next video (trees as acyclic connected graphs)