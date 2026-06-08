# Video 52: Green's Theorem
## Calculus III — Multivariable Playlist -- Video 12 of 14

### Topic
Green's Theorem: relating line integrals around a closed curve to double integrals
over the region it encloses. Circulation form, flux form, proof idea, worked examples,
applications.

### Prerequisites
- Video 51: Line Integrals
- Video 49: Double Integrals
- Curl (from Video 47: Gradient)

### Duration Target
12–15 minutes

### Scene Plan

**Scene 1: Hook — A Bridge Between Two Worlds (0:00–1:30)**
- Narration: "Green's Theorem reveals a deep connection: the circulation of a vector
field around a closed boundary equals the total curl inside the region."
- Visuals: closed curve C, interior region D, question

**Scene 2: The Circulation Form (1:30–4:00)**
- Statement: ∮_C F·dr = ∫∫_D (∂Q/∂x - ∂P/∂y) dA
- Where F = (P, Q), C is positively oriented boundary of D
- "Positive orientation" = counterclockwise
- Key intuition: curl inside → net circulation on boundary

**Scene 3: The Flux Form (4:00–5:30)**
- ∮_C F·n ds = ∫∫_D (∂P/∂x + ∂Q/∂y) dA
- Divergence form: flux across boundary = total divergence inside
- Brief mention of divergence theorem preview

**Scene 4: Proof Idea (5:30–7:30)**
- Divide D into small rectangles
- On each rectangle: circulation = (curl at center) × area
- Interior edges cancel (each shared by two rectangles)
- Only boundary edges survive
- Sum → double integral of curl = line integral on boundary

**Scene 5: Worked Example (7:30–10:00)**
- F(x,y) = (y², x²), C = boundary of [0,1]×[0,1]
- Direct line integral vs Green's Theorem
- Both give result 0 (curl = 2x - 2y, integral over square = 0)

**Scene 6: Applications (10:00–11:30)**
- Area from line integral: A = (1/2)∮_C x dy - y dx
- Computing area without explicit double integration
- Planimeter concept

**Scene 7: Summary (11:30–13:00)**
- Green's Theorem connects line integrals and double integrals
- Two forms: circulation (curl) and flux (divergence)
- Applications: simplify line integrals, compute area
- Outro
