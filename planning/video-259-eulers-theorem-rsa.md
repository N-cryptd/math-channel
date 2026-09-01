# Video 259: Euler's Theorem and RSA

## Playlist: Number Theory (Graduate)
## Duration target: 10-13 minutes
## Prerequisites: Video 257 (Fermat's Little Theorem), Video 258 (Euler's Totient)

## Competitive Analysis

### Key Competitors
1. **Art of the Problem** — "Public Key Cryptography: RSA Encryption" (990K views, 2012)
   - Animated explainer covering Euler's theorem + phi + factoring + complexity
   - Strength: Ties the math directly to the crypto application
   - Weakness: Dated animation style, no formal proof
   - Rating: Structure 8, Pacing 7, Visual 7, Narration 7, Engagement 8

2. **Eddie Woo** — "The RSA Encryption Algorithm" (1.27M views, 2014)
   - Whiteboard lecture, step-by-step numerical example
   - Strength: Very clear worked example, classroom energy
   - Weakness: No visual animation, no proof of Euler's theorem
   - Rating: Structure 6, Pacing 8, Visual 3, Narration 9, Engagement 7

3. **Mu Prime Math** — "Euler's Totient Theorem and Fermat's Little Theorem" (91K views, 2020)
   - Complete proof of Euler's theorem, connects to FLT
   - Strength: Rigorous proof, good intuition
   - Weakness: No RSA application, static visuals
   - Rating: Structure 7, Pacing 6, Visual 4, Narration 7, Engagement 5

### Our Differentiation
- Unlike Art of the Problem (no formal proof) and Mu Prime Math (no RSA), we do BOTH: rigorous proof + crypto application
- Unlike Eddie Woo (whiteboard only), we use animated Manim visuals
- Our proof uses the permutation argument (same as Fermat's, extended to the coprime residue set), which is more visual than the group-theory proof
- Worked RSA example with small primes (p=61, q=53) — clear enough to follow but not trivially small

## Scene Plan (9 scenes)

### Scene 1: Hook — The Encryption Paradox (18s)
**Content budget:** title + 3 items
- Play intro
- Title: "The Encryption Paradox"
- Text: "How can you share a secret with someone you've never met?"
- Text: "The answer uses a theorem we proved last time"
- Text: "Euler's theorem: a^phi(n) = 1 (mod n)

### Scene 2: Euler's Theorem — Statement (15s)
**Content budget:** title + formula box + 2 items
- Section divider: "The Theorem"
- Title: "Euler's Theorem"
- Formula box: gcd(a, n) = 1 => a^phi(n) ≡ 1 (mod n)
- Text: "When n = p (prime): phi(p) = p-1, recovers Fermat's Little Theorem"
- Text: "Example: 3^4 = 81 = 1 (mod 10). phi(10) = 4. Confirmed!"

### Scene 3: Proof — The Permutation Argument (22s)
**Content budget:** title + 4 items (two sub-groups)
- Section divider: "Proof"
- Title: "Proof: Permutation of Coprime Residues"
- Sub-group 1:
 - Text: "Let U = {x : 1 ≤ x ≤ n, gcd(x,n) = 1}"
 - Text: "|U| = phi(n). For a in U, the map f(x) = ax (mod n) is a bijection on U"
- Clear, then sub-group 2:
 - MathTex: product of all x in U ≡ product of all a*x in U (mod n)
 - MathTex: X ≡ a^phi(n) * X (mod n), cancel X (since gcd(X, n) = 1)
 - MathTex: a^phi(n) ≡ 1 (mod n) QED

### Scene 4: From Theorem to Encryption (20s)
**Content budget:** title + 3 items
- Section divider: "The Key Insight"
- Title: "From Theorem to Encryption"
- Text: "Euler's theorem says: a^phi(n) = 1 (mod n)"
- Text: "So: a^(k*phi(n)+1) = a (mod n) for any k"
- Text: "If we split the exponent: a^e raised to d = a (mod n), where e*d = 1 (mod phi(n))"

### Scene 5: RSA — Key Generation (22s)
**Content budget:** title + 4 items
- Section divider: "RSA Algorithm"
- Title: "Key Generation"
- Items progressive reveal:
 - Text: "1. Choose two large primes p and q"
 - Text: "2. Compute n = p*q and phi(n) = (p-1)(q-1)"
 - Text: "3. Choose e with gcd(e, phi(n)) = 1 (public exponent)"
 - Text: "4. Compute d = e^(-1) (mod phi(n)) (private key)"

### Scene 6: RSA — Encryption and Decryption (18s)
**Content budget:** title + 4 items
- Title: "Encryption and Decryption"
- Items progressive reveal:
 - Text: "Public key: (n, e).  Private key: d"
 - Text: "Encrypt: c = m^e (mod n)"
 - Text: "Decrypt: m = c^d (mod n) = m^(ed) (mod n) = m (mod n)"
 - Text: "This works because ed = 1 (mod phi(n))!"

### Scene 7: Worked Example (26s)
**Content budget:** title + 5 items (split into 2 sub-groups)\n- Section divider: "Worked Example"
- Title: "Example: p = 61, q = 53"
- Sub-group 1 (key generation):
 - Text: "n = 61*53 = 3233, phi(n) = 60*52 = 3120"
 - Text: "Choose e = 17. Then d = 2753 (since 17*2753 = 1 (mod 3120))"
- Clear, then sub-group 2 (encrypt/decrypt):
 - Text: "Message m = 42. Encrypt: 42^17 (mod 3233) = 2557"
 - Text: "Decrypt: 2557^2753 (mod 3233) = 42. It works!"

### Scene 8: Why Is RSA Secure? (18s)
**Content budget:** title + 4 items
- Section divider: "Security"
- Title: "Why Is RSA Secure?"
- Items progressive reveal:
 - Text: "Public key reveals n and e, but NOT phi(n) or d"
 - Text: "To find d, you need phi(n), which needs p and q"
 - Text: "Finding p and q from n = p*q is the FACTORING problem"
 - Text: "For a 2048-bit n, factoring is computationally infeasible"

### Scene 9: Summary and Outro (18s)
**Content budget:** title + 4 items
- Section divider: "Summary"
- Title: "Key Takeaways"
- Items progressive reveal:
 - Text: "1. Euler's theorem: a^phi(n) = 1 (mod n), generalizes Fermat"
 - Text: "2. Proof: permutation of coprime residues"
 - Text: "3. RSA uses e*d = 1 (mod phi(n)) to enable public-key encryption"
 - Text: "4. Security rests on the difficulty of factoring large numbers"
- Play outro
