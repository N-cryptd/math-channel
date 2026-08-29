# Video 256: Chinese Remainder Theorem

## Playlist: Number Theory (Videos 251-265)
## Duration Target: 10-15 minutes
## Prerequisites: Video 255 (Linear Congruences)

---

## Scene Plan

### Scene 1: Hook -- Ancient Problem (45s)
- Chinese mathematician Sun Tzu, 3rd century AD
- "There are things of unknown number. When counted in threes, remainder 2. When counted in fives, remainder 3. When counted in sevens, remainder 2."

### Scene 2: Statement of the Theorem (75s)
- Section divider: "1. The Theorem"
- If n_1, ..., n_k are pairwise coprime
- Then the system x = a_i (mod n_i) has a unique solution mod N = n_1 * ... * n_k

### Scene 3: Constructive Proof / Algorithm (90s)
- Section divider: "2. Constructing the Solution"
- Let N = n_1 * ... * n_k
- Let N_i = N / n_i
- Find m_i = N_i^(-1) (mod n_i)
- Solution: x = sum(a_i * m_i * N_i) (mod N)
- Work through the Sun Tzu example

### Scene 4: Applications (60s)
- Section divider: "3. Applications"
- Reconstructing large integers from remainders
- Used in RSA decryption
- Secret sharing schemes

### Scene 5: Summary & Outro (45s)

---
## Technical Notes
- Script file: scripts/graduate/video-256-chinese-remainder-theorem.py
- Class name: Video256_ChineseRemainderTheorem
