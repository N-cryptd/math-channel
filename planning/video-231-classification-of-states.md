# Video 231: Classification of States
Stochastic Processes playlist, video 3/12. Est. duration: 12 min.

## Topic
Classification of states in Markov chains: recurrent vs transient, periodic vs aperiodic, absorbing states, and communicating classes.

## Prerequisites
- Video 229: Random Walks (simple walk definition)
- Video 230: Markov Chains (transition matrices, Chapman-Kolmogorov)

## Scenes

### Scene 1: Hook (45s)
- "Not all states in a Markov chain behave the same way. Some you visit infinitely often, some you leave forever."
- Motivating question: in a random walk, do you always return to the origin?
- Tease the classification framework

### Scene 2: Communicating States (90s)
- Section divider: "Communicating States"
- Definition: state i communicates with state j (i → j) if P^n(i,j) > 0 for some n
- Communication is an equivalence relation (reflexive, symmetric, transitive)
- Communicating classes partition the state space
- Visual: state diagram with arrows showing which states communicate

### Scene 3: Recurrent vs Transient (120s)
- Section divider: "Recurrent and Transient States"
- Definition: starting from i, probability of ever returning to i
- Recurrent: f_ii = 1 (guaranteed return)
- Transient: f_ii < 1 (may never return)
- Key fact: in a finite chain, not all states can be transient
- Visual: compare a state that always gets revisited vs one you escape

### Scene 4: Positive vs Null Recurrent (90s)
- Section divider: "Positive and Null Recurrent"
- Definition: expected return time m_i = E[T_i | X_0 = i]
- Positive recurrent: m_i < ∞ (return quickly on average)
- Null recurrent: m_i = ∞ (return is guaranteed but takes forever on average)
- Example: 1D symmetric random walk is null recurrent (Polya from video 229)

### Scene 5: Periodicity (90s)
- Section divider: "Periodicity"
- Definition: period d(i) = gcd{n : P^n(i,i) > 0}
- Periodic: d(i) > 1 (returns only at multiples of d)
- Aperiodic: d(i) = 1 (no cyclic pattern)
- Visual: 2-state cycle (d=2) vs fully connected (d=1)
- Self-loop implies aperiodic

### Scene 6: Irreducible Chains (60s)
- All states communicate with each other
- In an irreducible chain, all states share the same classification
- All recurrent or all transient, same period
- Reduces the analysis to checking one state

### Scene 7: Absorbing States & Examples (90s)
- Definition: absorbing state i has P(i,i) = 1
- Once entered, never left
- Examples: gambler's ruin (0 and N are absorbing)
- Absorbing Markov chains and their applications

### Scene 8: Summary (60s)
- Classification tree: Recurrent (positive/null) vs Transient, Periodic vs Aperiodic
- Irreducibility = same class for all states
- Preview of next video: stationary distributions
- Outro

## Content Budget
- 8 scenes, ~12 min total
- Each scene: max 5 visible elements
- Narration: ~12 words per 5 seconds

## Key Formulas
- Communication: P^n(i,j) > 0 for some n ≥ 1
- Return probability: f_ii = P(ever return to i | X_0 = i)
- Expected return time: m_i = Σ n · f_ii^(n)
- Period: d(i) = gcd{n ≥ 1 : P^n(i,i) > 0}
- Absorbing: P(i,i) = 1