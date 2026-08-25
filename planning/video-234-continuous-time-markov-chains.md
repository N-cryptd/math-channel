# Video 234: Continuous-Time Markov Chains
Stochastic Processes playlist, video 6/12. Est. duration: 15 min.

## Topic
Continuous-time Markov chains (CTMCs): transition rates (Q-matrix/generator),
Kolmogorov forward/backward equations, embedded jump chain,
connection to Poisson processes, and long-run behavior.

## Prerequisites
- Video 230: Markov Chains (discrete-time)
- Video 232: Stationary Distributions
- Video 233: Poisson Processes (exponential holding times)

## Scenes

### Scene 1: Hook (45s)
- Discrete-time chains move in steps. Real systems evolve continuously.
- Chemical reactions, queueing, epidemics happen at any moment
- Key insight: CTMCs combine discrete state space with continuous time

### Scene 2: From Discrete to Continuous (90s)
- Section divider: "Making Time Continuous"
- In discrete time: P is the one-step transition matrix
- In continuous time: transitions happen at random times
- Holding times are Exponential (memoryless!)
- Rate parameter q_ij for transition from i to j

### Scene 3: The Generator Matrix (120s)
- Section divider: "The Q-Matrix"
- Q(i,j) = q_ij for i != j (transition rates)
- Q(i,i) = -sum_{j!=i} q_ij (diagonal = negative total rate)
- Row sums = 0
- P(t) = exp(Q*t)
- The matrix exponential

### Scene 4: Kolmogorov Equations (90s)
- Section divider: "How Probabilities Evolve"
- Forward equation: P'(t) = P(t) Q
- Backward equation: P'(t) = Q P(t)
- For finite chains, both give same solution
- Connection to systems of ODEs

### Scene 5: Embedded Jump Chain (90s)
- Section divider: "The Jump Chain"
- Ignore time, just look at the sequence of states
- This is a discrete-time Markov chain
- Jump probabilities: P_ij = q_ij / q_i for i != j
- q_i = sum_{j!=i} q_ij (total rate out of state i)
- Holding time in state i: Exponential(q_i)

### Scene 6: Stationary Distributions (60s)
- Section divider: "Long-Run Behavior"
- pi Q = 0 (analogous to pi P = pi)
- sum pi_j = 1
- Same classification ideas from Video 231 apply

### Scene 7: Summary (60s)
- CTMC: discrete states, continuous time
- Generator Q: rates + diagonal constraints
- P(t) = exp(Qt), Kolmogorov equations
- Embedded chain for jump sequence
- Preview: Brownian Motion
- Outro

## Key Formulas
- Q(i,j) = q_ij for i != j
- Q(i,i) = -sum_{j!=i} q_ij
- P(t) = exp(Q*t)
- Forward: P'(t) = P(t)Q
- Backward: P'(t) = Q P(t)
- Jump: P_ij = q_ij / q_i
- Holding: T_i ~ Exp(q_i)
- Stationary: pi Q = 0