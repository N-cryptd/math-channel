# Video 87: Trees in Discrete Mathematics
## Discrete Mathematics -- Video 10 of 12

**Predecessor:** Video 86 (Graph Theory Basics)
**Next:** Video 88 (Graph Coloring)

### Competitive Analysis

No dedicated competitive analysis was run for this video due to tool constraints.
Based on known YouTube landscape:
- **3Blue1Brown** has no dedicated trees video but covers tree-related concepts in neural network and error-correcting code videos
- **Reducible** covers trees in algorithm context (sorting, Huffman coding) with clean Manim animations
- **William Fiset** has a dedicated "Trees" video with CS/algorithm focus (~200K views)
- **Abdul Bari** covers trees with whiteboard style, definitions-heavy
- **mycodeschool** has popular binary tree traversal videos

**KEY GAP:** Most competitor videos treat trees purely as CS data structures. Our differentiator: emphasize the MATHEMATICAL properties of trees (acyclic, minimally connected), then bridge to CS applications. Visual proofs of properties, not just definitions.

### Key Differentiators
1. **Bridge from graph theory**: Start by removing cycles from a graph to form a tree (connects to Video 86)
2. **Visual proofs**: Prove |E| = |V| - 1 by building a tree vertex by vertex
3. **Traversal animations**: Pre/in/post-order shown simultaneously on one tree with color-coded visits
4. **MST algorithm animation**: Kruskal's with animated edge sorting and cycle detection
5. **Real-world applications**: File systems, decision trees, phylogenetic trees, network routing

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Tree nodes / vertices | PRIMARY | #5BC0EB |
| Tree edges / branches | SECONDARY | #7BC950 |
| Highlighted / active node | ACCENT | #FFD166 |
| Root node | ACCENT | #FFD166 |
| Visited / processed | ACCENT | #FFD166 |
| Deleted / rejected edge | RED | #EF476F |
| Labels / weights | WHITE | #FFFFFF |
| Cycle highlight | RED | #EF476F |
| Spanning tree edges | SECONDARY | #7BC950 |
| Non-tree edges (dimmed) | DIM | #6B6B8D |

### Structure (14 minutes, 12 scenes)

**Scene 1 -- Hook: From Graphs to Trees (1:00)**
- Start with a connected graph with cycles from Video 86
- Remove one edge at a time, breaking cycles, until no cycles remain
- "We just created a tree! Trees are graphs with no cycles."
- Bridge: "Today we'll explore these special structures that appear everywhere."
- Content budget: Animated graph → cycle removal → tree, 3 text labels

**Scene 2 -- Tree Definition and Properties (1:30)**
- Section divider: "What is a Tree?"
- Definition: A tree is a connected acyclic graph
- Alternative definition: A graph where every pair of vertices has exactly one simple path
- Key properties: |E| = |V| - 1, connected, no cycles
- Visual proof hint: building tree one vertex at a time
- Content budget: Definition text + example tree + property list

**Scene 3 -- Visual Proof: Edges = Vertices - 1 (1:30)**
- Section divider: "Why Trees Have n-1 Edges"
- Start with a single vertex (0 edges, 1 vertex)
- Add vertices one at a time — each new vertex connects with exactly ONE edge
- After adding n-1 more vertices, we have n vertices and n-1 edges
- Show the formula: |E| = |V| - 1
- Note: This is actually an if-and-only-if (equivalent to connected + acyclic)
- Content budget: Step-by-step tree construction + formula + if-and-only-if note

**Scene 4 -- Forests and Rooted Trees (1:30)**
- Section divider: "Rooted Trees and Forests"
- Forest: disconnected collection of trees
- Rooted tree: pick any vertex as the "root"
- Terminology: parent, child, sibling, leaf (external node), internal node
- Height and depth definitions
- Visual: Same tree rooted at different vertices → different parent-child relationships
- Content budget: Tree diagram + labeled terminology + height/depth example

**Scene 5 -- Binary Trees (1:30)**
- Section divider: "Binary Trees"
- Definition: Each node has at most 2 children (left and right)
- Full binary tree: every node has 0 or 2 children
- Complete binary tree: all levels filled except possibly the last, filled left-to-right
- Perfect binary tree: all internal nodes have 2 children, all leaves at same level
- Visual: Examples of each type side by side
- Content budget: 3 small binary tree diagrams + definitions

**Scene 6 -- Tree Traversals: Overview (1:00)**
- Section divider: "Exploring Trees: Traversals"
- Motivation: How do we systematically visit every node?
- Three fundamental orders: Pre-order, In-order, Post-order
- All defined by WHEN we process the current node (before/after children)
- Visual: Three arrows showing visit order on same tree
- Content budget: Labeled tree + three traversal arrows + order names

**Scene 7 -- Pre-order Traversal (1:00)**
- Section divider: "Pre-Order: Root, Left, Right"
- Process root → traverse left subtree → traverse right subtree
- Visual: Animate visiting nodes in pre-order with numbering
- Application: Copying a tree, expression trees (prefix notation)
- Content budget: Animated traversal + sequence output + application text

**Scene 8 -- In-order and Post-order (1:30)**
- In-order: Left subtree → root → right subtree
- Post-order: Left subtree → right subtree → root
- Visual: Same tree, two different traversals animated
- Key insight: In-order gives sorted output for BST
- Post-order: deleting a tree, computing directory sizes
- Content budget: Two traversal animations + sequence outputs + applications

**Scene 9 -- Spanning Trees (1:30)**
- Section divider: "Spanning Trees"
- Definition: A spanning tree of a graph G is a subgraph that includes ALL vertices, is a tree
- Equivalent: minimum set of edges that keeps the graph connected
- Number of spanning trees: a graph can have many spanning trees
- Visual: Start with graph, highlight different spanning trees one at a time
- Bridge: "What if edges have weights and we want the cheapest spanning tree?"
- Content budget: Original graph + 2-3 spanning tree highlights + definition

**Scene 10 -- Minimum Spanning Trees: Kruskal's (2:00)**
- Section divider: "Minimum Spanning Tree: Kruskal's Algorithm"
- Problem: Find spanning tree with minimum total edge weight
- Kruskal's approach: Sort edges by weight, add cheapest edge that doesn't create a cycle
- Visual: Weighted graph → sort edges → add one by one with cycle check
- Animated step-by-step with rejected edges shown in red
- Result: MST with total weight highlighted
- Content budget: Weighted graph + sorted edge list + animated construction

**Scene 11 -- Applications of Trees (1:30)**
- Section divider: "Where Trees Appear"
- File systems: directories and files as a rooted tree
- Decision trees: yes/no decisions lead to classifications
- Phylogenetic trees: evolutionary relationships between species
- Network routing: spanning trees in network design
- Huffman coding: optimal compression using binary trees
- Visual: Quick montage of 4-5 tree application examples
- Content budget: 4-5 application icons/diagrams with brief labels

**Scene 12 -- Summary and Outro (1:00)**
- Recap: Tree definition, properties, binary trees, traversals, spanning trees, MST
- Key formulas: |E| = |V| - 1, traversal orders
- "Trees are the simplest connected structure — minimal edges, no wasted connections."
- Preview: "Next: Graph Coloring — assigning colors under constraints."
- Play outro
- Content budget: Summary points + formula box + transition text

### Production Notes
- Bridge from Video 86 by starting with a graph and removing cycles
- Use consistent green color for tree edges (SECONDARY) to distinguish from generic graph edges
- Keep traversal examples on the SAME tree for comparison
- MST animation should be step-by-step with pauses
- Use progressive disclosure: build trees vertex by vertex
- Every property must have a visual justification, not just stated
- Trees should have ≤7 vertices for clarity
- For Kruskal's, use a small weighted graph (5-6 vertices, 7-8 edges)
