# Video 166: Bounded Linear Operators

**Playlist:** Functional Analysis (Videos 162-173)
**File:** scripts/graduate/video-166-bounded-linear-operators.py
**Class:** Video166_BoundedLinearOperators
**Prerequisites:** Video 163 (Banach Spaces), Video 165 (Hilbert Spaces)

## Scene Plan (8 scenes, ~12 min)

### Scene 1: Hook -- "The Gentle Transformers" (30s)
- Play intro
- Title: "The Gentle Transformers"
- Progressive reveal: What if you want a linear map that doesn't break things?
  - Linear maps can stretch, rotate, project...
  - Some maps send bounded sets to bounded sets, some don't
  - Bounded = well-behaved. This is the class of operators we study.

### Scene 2: Definition of Bounded Linear Operator (60s)
- Section divider
- Definition: T: X -> Y is bounded if there exists M such that ||Tx|| <= M||x|| for all x
- Intuition: T maps the unit ball to a bounded set
- Visual: unit ball -> stretched ball image (conceptually)
- Key formula: ||T|| = sup{||Tx|| : ||x|| <= 1}

### Scene 3: The Operator Norm (60s)
- Definition of operator norm as supremum
- Geometric meaning: "maximum stretching factor"
- Properties: positivity, homogeneity, triangle inequality
- This makes ||.||_op a NORM on operators

### Scene 4: Bounded = Continuous (60s)
- Theorem: T is bounded iff T is continuous
- Proof sketch: bounded -> Lipschitz -> continuous
- And continuous at 0 -> bounded (uniform boundedness)
- Visual intuition: the epsilon-delta picture
- This is why "bounded" is the right notion in infinite dimensions

### Scene 5: Key Examples (90s)
- Example 1: Identity operator I, ||I|| = 1
- Example 2: Multiplication operator on C[0,1], (Tf)(x) = x*f(x), ||T|| = 1
- Example 3: Differentiation operator on C[0,1] -- NOT BOUNDED!
  - Take f_n(x) = sin(nx), ||f_n|| = 1 but ||f'_n|| = n
  - This is a KEY insight competitors miss: differentiation is unbounded
- Contrast bounded vs. unbounded visually

### Scene 6: The Space B(X,Y) (60s)
- Set of all bounded linear operators from X to Y
- B(X,Y) is itself a Banach space (when Y is complete)
- Composition: if T in B(X,Y) and S in B(Y,Z), then ST in B(X,Z)
- ||ST|| <= ||S|| ||T|| (submultiplicativity)
- Key result that ties everything together

### Scene 7: Adjoint Operators on Hilbert Spaces (60s)
- Connect to Video 165 (Riesz Representation Theorem)
- Definition: T* is the unique operator with <Tx,y> = <x,T*y>
- Key properties: ||T*|| = ||T||, (T*)* = T, (ST)* = T*S*
- The adjoint as "mirror image" of the operator

### Scene 8: Spectral Radius and Summary (45s)
- Spectral radius: r(T) = sup{|lambda| : lambda in spectrum(T)}
- Spectral radius formula: r(T) = lim ||T^n||^{1/n}
- Teaser: this connects to eigenvalues, spectral theorem (future videos)
- Summary of key takeaways
- Play outro: "Compact Operators"

## Competitive Analysis Insights Incorporated
- Unlike MIT OCW (84 min lecture), we use 8 focused scenes with progressive disclosure
- Unlike TBSOM (fragmented across multiple videos), we unify the topic in one video
- Animated geometric intuition for "bounded" (unit ball -> bounded set) -- NO competitor does this
- Visual differentiation: bounded vs. unbounded operator comparison (differentiation example)
- Connect adjoint to Riesz theorem from Video 165 (following MIT OCW's bridge but animated)
