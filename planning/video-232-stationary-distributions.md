# Video 232: Stationary Distributions
Stochastic Processes playlist, video 4/12. Est. duration: 12 min.

## Topic
Stationary distributions of Markov chains: definition, existence and uniqueness theorems,
computing stationary distributions, and the connection to long-run behavior.

## Prerequisites
- Video 230: Markov Chains (transition matrices)
- Video 231: Classification of States (recurrent, irreducible, aperiodic)

## Scenes

### Scene 1: Hook (45s)
- "If you run a Markov chain long enough, does it settle down?"
- Weather example: does the long-run fraction of sunny days converge?
- Preview the stationary distribution concept

### Scene 2: Definition (90s)
- Section divider: "What is a Stationary Distribution?"
- Definition: pi is stationary if pi P = pi
- Interpretation: if the chain starts with distribution pi, it stays there
- pi_j = lim (1/n) sum of indicator that X_k = j

### Scene 3: Computing Stationary Distributions (120s)
- Section divider: "Finding the Stationary Distribution"
- System of linear equations: pi P = pi with constraint sum(pi) = 1
- Replace one equation with normalization
- Weather example worked out numerically
- Visual: show the matrix equation and solution

### Scene 4: Existence and Uniqueness (90s)
- Section divider: "When Does It Exist?"
- Theorem: finite irreducible Markov chain has a unique stationary distribution
- Positive recurrent: unique stationary distribution exists
- Connection to classification from Video 231
- If chain is also aperiodic, chain converges to stationary distribution

### Scene 5: Detailed Balance (90s)
- Section divider: "Detailed Balance"
- Definition: pi_i P(i,j) = pi_j P(j,i)
- Sufficient condition for stationarity
- Reversibility: chain looks the same forward and backward
- Examples: random walk on a graph

### Scene 6: Convergence Theorem (90s)
- Section divider: "Convergence to Stationarity"
- Theorem: for irreducible, aperiodic, positive recurrent chain
- lim P^n(i,j) = pi_j regardless of starting state
- Mixing time: how long until close to stationary
- Ergodic theorem connection

### Scene 7: Summary (60s)
- Stationary distribution: pi P = pi, sum = 1
- Exists and is unique for finite irreducible chains
- Convergence requires aperiodicity
- Detailed balance as a sufficient condition
- Preview: Poisson processes
- Outro

## Content Budget
- 7 scenes, ~12 min total
- Each scene: max 5 visible elements

## Key Formulas
- Stationary: pi P = pi, sum_j pi_j = 1
- Detailed balance: pi_i P(i,j) = pi_j P(j,i)
- Convergence: lim_{n->inf} P^n(i,j) = pi_j
- Ergodic: (1/n) sum_{k=1}^{n} 1_{X_k=j} -> pi_j a.s.