# Video 44: Lines and Planes in 3D

## Overview
**Playlist:** Calculus III — Multivariable (Video 4 of 14)
**Topic:** Lines and planes in three-dimensional space — parametric/vector/symmetric equations of lines, and the point-normal form and standard form of planes
**Estimated duration:** 12 minutes

## Competitive Analysis
Skipped — youtubei.js metadata API returned limited data. Proceeding with standard approach. Key insights from the series pattern (Videos 41-43): geometric intuition first, then algebraic formulas, then worked examples. 3B1B's "Essence of Linear Algebra" style emphasizes visual motivation before formalism — we follow the same arc.

## Scene Breakdown

### Scene 1: Hook + Intro (15s)
- **Narration:** "A line in 3D isn't described by y equals mx plus b. We need more information — either a point and a direction, or two points. And a plane? That's defined by a point and a normal vector. Let's see how these equations work."
- **Content budget:** bridge Text + play_intro (2 items)
- **Elements:** bridge Text

### Scene 2: Lines — The Direction Vector (30s)
- **Narration:** "Every line in 3D has a direction vector that tells us which way it points. Given a point on the line and a direction vector d, we can write the line in three equivalent forms: parametric, vector, and symmetric."
- **Content budget:** section divider, title, direction concept Text, parametric equations, note (5 items)
- **Elements:** MathTex for parametric equations x = x0 + at, y = y0 + bt, z = z0 + ct

### Scene 3: Three Forms of a Line (35s)
- **Narration:** "The parametric form writes each coordinate as a function of the parameter t. The vector form combines them: r equals r0 plus t times d. The symmetric form eliminates t: x minus x0 over a equals y minus y0 over b equals z minus z0 over c. Each form is useful in different situations."
- **Content budget:** title, vector form MathTex, symmetric form MathTex, note about when denominators are zero (4 items)
- **Elements:** vector equation, symmetric equation, zero-denominator note

### Scene 4: Worked Example — Line from Two Points (30s)
- **Narration:** "Find the line through the points (1, 2, 3) and (4, 5, 6). The direction vector is the difference: (3, 3, 3). So the parametric form is x equals 1 plus 3t, y equals 2 plus 3t, z equals 3 plus 3t. Notice this is a simple example — the line goes diagonally through space."
- **Content budget:** title, two points, direction vector, parametric result (4 items)
- **Elements:** points MathTex, direction vector, parametric equations

### Scene 5: Planes — Point-Normal Form (30s)
- **Narration:** "A plane in 3D is determined by a point on it and a normal vector perpendicular to it. The equation comes from the dot product: n dot the vector r minus r0 equals zero. If the normal is (a, b, c) and the point is (x0, y0, z0), we get a times x minus x0 plus b times y minus y0 plus c times z minus z0 equals zero."
- **Content budget:** section divider, title, normal vector concept, equation derivation (4 items)
- **Elements:** dot product derivation, point-normal equation

### Scene 6: Standard Form and Distance (35s)
- **Narration:** "Expanding the point-normal form gives the standard equation of a plane: ax plus by plus cz equals d, where d equals ax0 plus by0 plus cz0. To find the distance from a point to a plane, plug it into the formula: absolute value of ax1 plus by1 plus cz1 minus d, divided by the magnitude of the normal vector."
- **Content budget:** title, standard form equation, distance formula, note about the denominator (4 items)
- **Elements:** standard form MathTex, distance formula MathTex

### Scene 7: Worked Example — Plane Through Three Points (30s)
- **Narration:** "Find the plane through (1, 0, 0), (0, 1, 0), and (0, 0, 1). Two direction vectors are v1 equals (-1, 1, 0) and v2 equals (-1, 0, 1). Their cross product gives the normal: n equals (1, 1, 1). The plane equation is x plus y plus z equals 1."
- **Content budget:** title, three points, cross product calculation, plane equation (4 items)
- **Elements:** points, cross product, result

### Scene 8: Summary + Outro (20s)
- **Narration:** "To recap: lines in 3D need a point and direction, with three equivalent equation forms. Planes need a point and a normal vector. The dot product is the key tool for finding plane equations, and the cross product lets us compute normals from points on the plane. Next up, we'll look at vector-valued functions that trace out curves in 3D space."
- **Content budget:** title + 5 takeaways (progressive reveal), then play_outro
- **Elements:** 5 summary Text items

## Key Formulas
1. **Parametric line:** x = x0 + at, y = y0 + bt, z = z0 + ct
2. **Vector line:** r = r0 + td
3. **Symmetric line:** (x-x0)/a = (y-y0)/b = (z-z0)/c
4. **Point-normal plane:** a(x-x0) + b(y-y0) + c(z-z0) = 0
5. **Standard plane:** ax + by + cz = d
6. **Point-plane distance:** |ax₁ + by₁ + cz₁ - d| / √(a² + b² + c²)

## References
- Builds on: Video 41 (Vectors in 3D), Video 42 (Dot Product), Video 43 (Cross Product)
- Precedes: Video 45 (Vector-Valued Functions)
