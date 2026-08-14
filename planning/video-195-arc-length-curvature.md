# Video 195: Arc Length and Curvature

**Playlist:** Differential Geometry (Video 2 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video195_ArcLengthCurvature
**Script:** scripts/graduate/video-195-arc-length-curvature.py

## Prerequisites
- Video 194: Curves in R^n (parametrized curves, tangent vectors, regularity, reparametrization)
- Calculus III: integration, arc length in R^2 and R^3
- Linear Algebra: norms, dot products, cross products in R^3

## Learning Objectives
1. Derive the arc length formula from the integral of speed
2. Define arc-length parametrization and understand why it is canonical
3. Reparametrize the helix by arc length explicitly
4. Define curvature as the magnitude of the second derivative in arc-length parametrization
5. Compute curvature for a circle (showing it equals 1/radius)
6. Compute curvature for a helix and interpret geometrically
7. Connect curvature to the intuitive notion of "how much a curve bends"

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — The Road Question (~40s)
**Visual:** Two roads drawn on screen — one straight, one winding. Question overlay.
- "Imagine two roads connecting the same two towns. One is straight, the other winds through the hills. Both connect A to B, but the winding road is longer. How do we measure the length of a curve?"
- Transition to intro: "Today we answer this question rigorously and go further — we develop curvature, the measure of how much a curve bends."
**Content:** Motivational hook connecting arc length to real-world measurement.
**Elements:** "Road A: straight" (line), "Road B: winding" (sinusoidal curve), "Which is longer?" label
**Content budget:** 3 elements max

### Scene 2: Intro + Section Divider (~20s)
**Visual:** Channel intro, then section divider.
- play_intro("Arc Length & Curvature", "Differential Geometry")
- Section divider: "1 — Arc Length"
**Elements:** Intro animation, section divider
**Content budget:** Animated sequence

### Scene 3: Arc Length Formula (~90s)
**Visual:** Progressive formula derivation.
- Start from the definition: "Chop the curve into small pieces, each piece is approximately straight, sum the lengths, take the limit."
- The formula: s = integral from a to b of |gamma'(t)| dt
- This is the integral of speed — speed measures how fast we move along the curve, and integrating speed over time gives total distance traveled.
- Geometric meaning: the length depends only on the image of the curve, not the parametrization.
- Key insight: reparametrization changes speed but the integral of speed over the parameter stays the same (by the substitution rule).
**Content:** "To find the length of a curve, we use the same idea from calculus. Chop the curve into tiny segments. Each segment is approximately straight, with length equal to the speed of traversal times the time interval. Summing all these lengths and taking the limit gives us the arc length formula: s equals the integral from a to b of the magnitude of gamma prime of t dt. The integrand is the speed, and integrating speed over time gives total distance traveled. An important property: the arc length depends only on the image of the curve, not on how we traverse it. This follows directly from the substitution rule for integration."
**Elements:** Definition box, integral formula, speed formula, "invariant under reparametrization" note
**Content budget:** Progressive reveal, max 5

### Scene 4: Arc-Length Parametrization (~90s)
**Visual:** The unit circle traversed at constant speed vs variable speed.
- Define s(t) = integral from a to t of |gamma'(u)| du as the arc length function.
- If gamma'(t) is never zero (regular curve), s(t) is strictly increasing and has an inverse.
- Define the arc-length parametrization: let alpha(s) = gamma(t(s)), where t(s) is the inverse of s(t).
- Key property: |alpha'(s)| = 1 for all s. The parameter s directly measures distance traveled.
- "This is the canonical parametrization — the parameter equals the distance along the curve."
**Content:** "Given a regular curve gamma, define s of t as the integral from a to t of the magnitude of gamma prime dt. This function measures how far we have traveled along the curve from the starting point. Since gamma is regular, gamma prime is never zero, so s is strictly increasing and therefore has an inverse. We define the arc-length parametrization alpha of s as gamma composed with the inverse of s. The magic of this reparametrization is that the speed is always exactly one: the magnitude of alpha prime of s equals one for all s. This means the parameter s directly measures distance traveled along the curve. It is the natural, canonical choice of parametrization."
**Elements:** s(t) integral formula, alpha(s) = gamma(t(s)), |alpha'(s)| = 1, "s = distance traveled" note
**Content budget:** Progressive reveal, max 5

### Scene 5: Section Divider + Curvature Definition (~80s)
**Visual:** Section divider, then the curvature definition with geometric intuition.
- Section divider: "2 — Curvature"
- Intuition: "How much does a curve bend at a point?"
- For a straight line: curvature = 0 everywhere. No bending.
- For a circle: curvature is constant — the same everywhere. And a tighter circle bends more.
- Formal definition: kappa(s) = |alpha''(s)| where alpha is arc-length parametrized.
- "The second derivative of the arc-length parametrization measures how fast the unit tangent vector changes direction. Since the tangent vector always has length 1, the second derivative is perpendicular to the curve — it points toward the center of bending."
**Content:** "Now we measure how much a curve bends. A straight line has zero curvature everywhere. A circle has constant curvature, and a tighter circle has higher curvature. Formally, the curvature kappa of a curve at a point is defined as the magnitude of the second derivative of the arc-length parametrization. Geometrically, this measures how fast the unit tangent vector rotates. Since the tangent vector always has unit length, the second derivative is perpendicular to the curve, pointing toward the center of the osculating circle."
**Elements:** Section divider, kappa(s) = |alpha''(s)|, tangent turning intuition, straight line vs circle contrast
**Content budget:** Progressive reveal, max 5

### Scene 6: Curvature of a Circle (~80s)
**Visual:** Circle with osculating circle / radius标注.
- Unit circle: gamma(t) = (cos t, sin t), already arc-length parametrized.
- Second derivative: gamma''(t) = (-cos t, -sin t) = -gamma(t).
- Curvature: kappa = |gamma''(t)| = 1 for all t.
- For a circle of radius R: gamma(t) = R(cos t, sin t).
- Speed: |gamma'(t)| = R, so we need to rescale to get arc-length param.
- After reparametrization: kappa = 1/R.
- Key result: "The curvature of a circle equals the reciprocal of its radius. A larger circle is less curved. This matches our geometric intuition perfectly."
**Content:** "Let us compute the curvature of a circle. Starting with the unit circle gamma of t equals cosine t, sine t. This is already arc-length parametrized since the speed is one. The second derivative is negative cosine t, negative sine t, which is just negative gamma. Its magnitude is one for all t, so the curvature of the unit circle is exactly one. For a circle of radius R, the standard parametrization has speed R. After reparametrizing by arc length, the curvature becomes one over R. The curvature of a circle is the reciprocal of its radius. A larger circle bends less. This perfectly matches our geometric intuition."
**Elements:** Unit circle computation, kappa = 1 result, general R circle, kappa = 1/R result
**Content budget:** Progressive reveal, max 5

### Scene 7: Curvature of a Helix (~80s)
**Visual:** Helix (2D projection) with curvature labels.
- Standard helix: gamma(t) = (cos t, sin t, t).
- Speed: |gamma'(t)| = sqrt(2), so s(t) = t*sqrt(2), t = s/sqrt(2).
- Arc-length parametrization: alpha(s) = (cos(s/sqrt(2)), sin(s/sqrt(2)), s/sqrt(2)).
- Second derivative computation gives |alpha''(s)| = 1/2.
- Curvature of the helix: kappa = 1/2.
- Interpretation: "The helix has constant curvature, the same at every point. This is less than the unit circle (kappa=1) because the helix also moves upward — it does not bend as much horizontally since some of the turning goes into the third dimension."
- Visual: contrast helix curvature with circle curvature.
**Content:** "Now the helix, gamma of t equals cosine t, sine t, t. Its speed is root 2 everywhere. The arc-length parametrization is alpha of s with s divided by root 2 in place of t. Computing the second derivative, we find that the curvature is exactly one half. The helix has constant curvature, the same at every point, just like a circle. But it is less than the unit circle because the helix also advances upward — not all of the turning goes into bending the curve in the plane. This is a beautiful example where geometry and computation reinforce each other."
**Elements:** Helix formula, speed computation, kappa = 1/2 result, interpretation comparison with circle
**Content budget:** Progressive reveal, max 5

### Scene 8: Summary and Outro (~60s)
**Visual:** Recap of key results, then outro.
- Key results:
  1. Arc length: s = integral of |gamma'(t)| dt
  2. Arc-length parametrization: |alpha'(s)| = 1
  3. Curvature: kappa = |alpha''(s)| — how fast the tangent turns
  4. Circle: kappa = 1/R (larger circle, smaller curvature)
  5. Helix: kappa = 1/2 (constant, less than unit circle)
- Preview of next video: Frenet-Serret Frame — the natural coordinate system for curves.
**Content:** "Today we learned two fundamental quantities associated with curves. The arc length measures how long a curve is, computed as the integral of speed. The arc-length parametrization is the canonical choice where the parameter directly measures distance. Curvature measures how much a curve bends, defined as the magnitude of the second derivative in arc-length parametrization. For a circle, curvature equals one over the radius. For a helix, curvature is constant at one half. Next time, we build the Frenet-Serret frame — the natural moving coordinate system attached to a curve at every point."
**Elements:** 5 key results (numbered), next video preview, outro animation
**Content budget:** Progressive reveal, max 5

## Competitive Analysis Reference
Per channel-analysis/improvements.md: No direct Manim-animated differential geometry competitor exists. This is green-field. Our approach: systematic, animated, building-block style unique to this channel. Building directly on Video 194 (Curves in R^n) — this is the natural continuation.
