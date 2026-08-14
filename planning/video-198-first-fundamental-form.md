# Video 198: First Fundamental Form

**Playlist:** Differential Geometry (Video 5 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video198_FirstFundamentalForm
**Script:** scripts/graduate/video-198-first-fundamental-form.py

## Prerequisites
- Video 197: Surfaces in R³ (parametrizations, regularity, tangent plane)
- Video 195: Arc Length & Curvature (arc length formula for curves)
- Linear Algebra: Inner products, metric tensors, quadratic forms

## Learning Objectives
1. Define the first fundamental form as the pullback of the Euclidean metric to the parameter domain
2. Compute the coefficients E, F, G from the parametrization
3. Express arc length on a surface using the first fundamental form
4. Express the angle between curves on a surface using the first fundamental form
5. Compute the area element dA = sqrt(EG - F²) du dv
6. Understand that the first fundamental form is intrinsic (depends only on measurements on the surface)

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — Measuring on a Surface (~45s)
**Visual:** A person walking on a sphere with measuring tape.
- "If you live on the surface of a sphere, you can measure distances, angles, and areas — all without ever leaving the surface. These measurements are intrinsic: they depend only on the surface itself, not on how it sits in space. The first fundamental form is the mathematical tool that encodes all these intrinsic measurements."
**Content:** Motivational hook about intrinsic geometry.
**Elements:** "Distance on surface" label, "Angle between curves" label, "Area of regions" label
**Content budget:** 3 elements max

### Scene 2: Intro + Section Divider (~20s)
- play_intro("First Fundamental Form", "Differential Geometry")
- Section divider: "1 — The Coefficients E, F, G"

### Scene 3: Definition via Pullback (~90s)
**Visual:** Build from dot products of partial derivatives.
- The first fundamental form I_p at a point p measures dot products of tangent vectors.
- For tangent vectors a*sigma_u + b*sigma_v and c*sigma_u + d*sigma_v:
  I_p = E*a*c + F*(a*d + b*c) + G*b*d (quadratic form)
- The coefficients: E = sigma_u . sigma_u, F = sigma_u . sigma_v, G = sigma_v . sigma_v
- Matrix form: I = [[E, F], [F, G]]
- These are functions of (u,v), varying from point to point on the surface.
- "The first fundamental form is a quadratic form on the tangent plane. It takes two tangent vectors and returns their dot product. The three coefficients E, F, and G encode everything we need to measure lengths, angles, and areas on the surface."

### Scene 4: Arc Length on a Surface (~80s)
**Visual:** A curve on a surface with differential arc length formula.
- A curve on the surface: gamma(t) = sigma(u(t), v(t))
- Arc length: L = integral |gamma'(t)| dt = integral sqrt(E*u'² + 2F*u'*v' + G*v'²) dt
- This generalizes the curve arc length formula: the first fundamental form replaces the Euclidean metric.
- "To measure the length of a curve on the surface, we compose the curve with the parametrization and use the chain rule. The speed is the square root of E times u prime squared, plus two F times u prime v prime, plus G times v prime squared."

### Scene 5: Angles on a Surface (~80s)
**Visual:** Two curves intersecting on a surface, showing the angle formula.
- Two curves on S: alpha(t) = sigma(u₁(t), v₁(t)), beta(t) = sigma(u₂(t), v₂(t))
- Their tangent vectors: alpha' = u₁'*sigma_u + v₁'*sigma_v, similarly for beta'
- Cosine of angle: cos(theta) = I(alpha', beta') / (|alpha'| * |beta'|)
- Expanding: cos(theta) = (E*u₁'*u₂' + F*(u₁'*v₂' + v₁'*u₂') + G*v₁'*v₂') / (speeds product)
- "The angle between two curves on a surface is computed using the first fundamental form. It is the ratio of the I-form of the tangent vectors to the product of their speeds."

### Scene 6: Area on a Surface (~70s)
**Visual:** Area element dA on the surface.
- Area of a region R on the surface: A = integral_R |sigma_u x sigma_v| du dv
- But |sigma_u x sigma_v|² = |sigma_u|²|sigma_v|² - (sigma_u . sigma_v)² = EG - F²
- So dA = sqrt(EG - F²) du dv
- "The area element on the surface is the magnitude of the cross product of the partials. Using the Lagrange identity, this equals the square root of E G minus F squared. So the first fundamental form coefficients give us the area element directly."

### Scene 7: Example — Sphere (~90s)
**Visual:** Compute E, F, G for the sphere, then arc length of a great circle.
- Sphere: sigma(theta, phi) = (R sin phi cos theta, R sin phi sin theta, R cos phi)
- E = R² sin² phi, F = 0, G = R²
- I = R² [[sin² phi, 0], [0, 1]]
- Arc length of latitude circle at phi₀: L = integral₀^{2pi} sqrt(E) dtheta = 2pi R sin phi₀
- Area of sphere: A = integral integral sqrt(R⁴ sin² phi) dphi dtheta = 4 pi R²
- F = 0 because spherical coordinates are orthogonal (the grid lines are perpendicular).

### Scene 8: Summary, Intrinsic Geometry, and Outro (~70s)
- Key results:
  1. I = [[E, F], [F, G]] where E = sigma_u·sigma_u, F = sigma_u·sigma_v, G = sigma_v·sigma_v
  2. Arc length: ds² = E du² + 2F du dv + G dv²
  3. Angle: cos(theta) = I(v, w) / (|v|·|w|)
  4. Area: dA = sqrt(EG - F²) du dv
  5. The first fundamental form is intrinsic (Gauss's Theorema Egregium preview)
- Preview: Next video (199) — Second Fundamental Form (extrinsic curvature)
- play_outro

## Competitive Analysis Reference
Per channel-analysis/improvements.md: Green-field topic.
- Dr. Trefor Bazett: First fundamental form whiteboard lecture
- Faculty of Khan: Metric tensor derivation (grad level, formula-heavy)
- 3B1B: References intrinsic/extrinsic but doesn't cover first fundamental form explicitly

Our approach: First animated walkthrough of the first fundamental form in a complete DG playlist. Progressive derivation from dot products → coefficients → applications. Emphasis on geometric intuition over formula memorization.
