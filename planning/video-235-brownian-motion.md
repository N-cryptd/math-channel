# Video 235: Brownian Motion
Stochastic Processes playlist, video 7/12. Est. duration: 15 min.

## Topic
Brownian motion (Wiener process): definition via increments, properties
(normal increments, continuous paths, nowhere differentiable),
Brownian motion as a limit of random walks, and basic properties.

## Prerequisites
- Video 229: Random Walks
- Video 233: Poisson Processes (continuous-time intuition)

## Scenes

### Scene 1: Hook (45s)
- Robert Brown's 1827 observation: pollen grains jittering in water
- Einstein's 1905 explanation: molecular bombardment
- Brownian motion is the continuous limit of random walks

### Scene 2: Formal Definition (120s)
- Section divider: "Definition"
- W(0) = 0
- Independent increments
- W(t) - W(s) ~ Normal(0, t-s)
- Continuous sample paths

### Scene 3: Key Properties (120s)
- Section divider: "Properties"
- E[W(t)] = 0 for all t
- Var[W(t)] = t (variance grows linearly!)
- Cov[W(s), W(t)] = min(s,t)
- Self-similar: W(ct) = sqrt(c) W(t) in distribution
- Nowhere differentiable: the path has no derivative anywhere

### Scene 4: Random Walk Limit (90s)
- Section divider: "From Random Walks to Brownian Motion"
- Scale a random walk: step size 1/sqrt(n), time step 1/n
- Donsker's theorem: the limit converges to Brownian motion
- Visual intuition: zooming into a random walk

### Scene 5: Brownian Motion and the Heat Equation (60s)
- Section divider: "Connection to Physics"
- The probability density satisfies the heat equation
- u_t = (1/2) u_xx
- Bridge between probability and PDEs

### Scene 6: Summary (60s)
- W(0)=0, independent normal increments, continuous paths
- E[W(t)]=0, Var[W(t)]=t, Cov=min(s,t)
- Limit of scaled random walks
- Preview: Martingales
- Outro

## Key Formulas
- W(t) - W(s) ~ N(0, t-s)
- E[W(t)] = 0
- Var[W(t)] = t
- Cov[W(s), W(t)] = min(s,t)
- Self-similarity: W(ct) ~ sqrt(c) W(t)
- Heat eq: u_t = (1/2) u_xx