# Video 233: Poisson Processes
Stochastic Processes playlist, video 5/12. Est. duration: 12 min.

## Topic
Poisson processes: counting processes, Poisson distribution, exponential inter-arrivals, memoryless property, superposition and thinning.

## Prerequisites
- Video 67: Probability Spaces
- Video 72-73: Common Distributions
- Video 230: Markov Chains

## Scenes

### Scene 1: Hook (45s)
- "How many customers arrive at a store in an hour? How many earthquakes in a year?"
- These are counting processes — events happening randomly in time
- Poisson process: the most important continuous-time counting model

### Scene 2: Definition (90s)
- Section divider: "Definition"
- N(t) = number of events in [0, t]
- Four axioms: N(0)=0, independent increments, stationary increments, rare events
- N(t) follows Poisson distribution with parameter lambda*t

### Scene 3: Poisson Distribution Connection (90s)
- Section divider: "The Poisson Distribution"
- P(N(t) = k) = e^(-lambda*t) * (lambda*t)^k / k!
- Mean = lambda*t, Variance = lambda*t
- lambda = rate parameter (events per unit time)
- Visual: Poisson PMF for different lambda*t values

### Scene 4: Exponential Inter-arrivals (90s)
- Section divider: "Waiting Times"
- Time between events is Exponential(lambda)
- Memoryless property: P(T > s+t | T > s) = P(T > t)
- Connection to continuous-time Markov chains

### Scene 5: Superposition and Thinning (90s)
- Section divider: "Building New Processes"
- Superposition: sum of independent Poisson processes is Poisson
- Rate adds: lambda_1 + lambda_2 + ...
- Thinning: each event kept with probability p gives Poisson(p*lambda)
- Applications in queueing and network theory

### Scene 6: Non-homogeneous Poisson (60s)
- Section divider: "Varying Rates"
- Rate can depend on time: lambda(t)
- Expected count = integral of lambda(t) from 0 to t
- Applications: rush hour traffic, seasonal events

### Scene 7: Summary (60s)
- Poisson process = continuous-time counting with independent increments
- N(t) ~ Poisson(lambda*t)
- Inter-arrivals ~ Exponential(lambda), memoryless
- Superposition adds rates, thinning scales rates
- Preview: continuous-time Markov chains
- Outro

## Key Formulas
- P(N(t) = k) = e^(-lambda*t) * (lambda*t)^k / k!
- E[N(t)] = Var(N(t)) = lambda*t
- P(T > t) = e^(-lambda*t)
- Memoryless: P(T > s+t | T > s) = P(T > t)
- Superposition: rate = sum of rates
- Thinning: rate = p * lambda