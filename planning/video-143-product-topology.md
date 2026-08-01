# Video 143: Product Topology
## Topology Playlist — Video 8 of 12

**Class:** Video143_ProductTopology
**Script:** scripts/graduate/video-143-product-topology.py
**Target Duration:** 12 minutes
**Level:** Graduate (L5)
**Prerequisites:** Video 139 (Introduction to Topology), Video 141 (Compactness)

---

## Competitive Analysis Summary

**Market gap:** No major animation channel has a dedicated Manim-animated video on the product topology. All existing content is lecture-style. This is a foundational topic in topology that deserves visual treatment — particularly the distinction between box topology and product topology, and why the product topology is the "right" one.

**Our opportunity:** First high-production animated treatment. Visual-first approach with:
- Animated visualization of product spaces as "grids" of open rectangles
- Comparison of box topology vs product topology (finite vs infinite products)
- Projection maps visualized as "shadow" maps
- Connection to Tychonoff (already covered in Video 141)
- Examples: R^2 as R x R with product topology, torus as S^1 x S^1

---

## Content Outline

### Scene 1: Hook — "Building New Spaces from Old" (~50s)
Show the idea of taking two spaces and forming their product. Visualize R x R as a grid.

### Scene 2: The Product Space (~60s)
Formal definition of X x Y. The set of all ordered pairs. Visual: grid formed by two number lines.

### Scene 3: Product Topology — Finite Products (~70s)
Base for the product topology: U x V where U is open in X and V is open in Y.
Visual: open rectangles in R^2.

### Scene 4: Projections (~50s)
Projection maps pi_X and pi_Y. These are continuous. Open sets in the product are cylinders.

### Scene 5: Box vs Product Topology (~70s)
For finite products, box = product. For infinite products, box topology has too many open sets.
Visual: infinite product, box allows "too fat" open sets.

### Scene 6: Key Results (~50s)
- Product of compact is compact (Tychonoff, reference Video 141)
- Product of connected is connected
- Product of path-connected is path-connected
- R^n = product of n copies of R

### Scene 7: Summary (~40s)
Recap + play_outro()
