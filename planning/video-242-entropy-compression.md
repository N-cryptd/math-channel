# Video 242: Entropy and Data Compression -- Plan

## Metadata
- **Number:** 242
- **Topic:** Entropy and Data Compression
- **Level:** Graduate (Information Theory)
- **Class:** Video242_EntropyCompression
- **Script:** scripts/graduate/video-242-entropy-compression.py
- **Builds on:** Video 241 (What is Information?)
- **Leads to:** Joint Entropy and Mutual Information (243)
- **Estimated duration:** 10-12 minutes

## Purpose
Second video of the Information Theory playlist. Shows how Shannon entropy sets a fundamental lower bound on the average number of bits needed to encode a source. Introduces source coding, Huffman coding, and the source coding theorem.

## Scene Plan (7 scenes)

### Scene 1: Motivation -- Why Compress? (50s)
**Narration:** "Every time you send a photo, stream a video, or store a file, compression is happening. The question is: how far can we compress? Is there a fundamental limit? Shannon's source coding theorem says yes, and that limit is entropy."

- play_intro("Entropy and Data Compression", "Information Theory")
- Title: "The Compression Problem"
- Items: "Files are compressed every day", "How far can we go?", "Entropy is the answer"

### Scene 2: Source Coding (60s)
**Narration:** "Source coding means assigning binary codewords to source symbols. The goal is to minimize the average codeword length. A fixed-length code uses the same number of bits for every symbol. But if some symbols are more likely, we can do better by giving them shorter codewords."

- Title: "Source Coding"
- Items: "Assign binary codes to symbols", "Minimize average length", "Frequent symbols get short codes"

### Scene 3: Fixed vs Variable Length (70s)
**Narration:** "Consider four symbols with probabilities 1/2, 1/4, 1/8, 1/8. A fixed-length code uses 2 bits per symbol. But a variable-length code can assign 1 bit to the most likely symbol, 2 bits to the next, and 3 bits to the rare ones. The average drops from 2 to 1.75 bits."

- Title: "Fixed vs Variable Length Codes"
- Two-column: fixed (2,2,2,2) vs variable (1,2,3,3)
- Formula: L_avg = sum(p_i * l_i)

### Scene 4: Huffman Coding (70s)
**Narration:** "Huffman coding is an optimal prefix-free code. You build it bottom-up: repeatedly merge the two least probable symbols into a new node. The resulting tree gives codeword lengths that minimize the expected length. Huffman is used in JPEG, ZIP, and MP3."

- Title: "Huffman Coding"
- Items: "Optimal prefix-free code", "Merge two least probable symbols", "Used in JPEG, ZIP, MP3"

### Scene 5: The Source Coding Theorem (80s)
**Narration:** "Shannon's source coding theorem is the fundamental result. It states that the average codeword length L can never be less than the entropy H. But we can get arbitrarily close to H from above. In symbols: H(X) is less than or equal to L, which is less than H(X) plus 1. This is why entropy is the limit of compression."

- Title: "Source Coding Theorem"
- Formula: H(X) <= L < H(X) + 1
- Items: "Entropy is the lower bound", "Can approach H arbitrarily closely"

### Scene 6: Example -- English Text (70s)
**Narration:** "The entropy of English text is about 1 to 1.5 bits per letter, far less than the 5 bits needed for fixed-length encoding. This shows English has massive redundancy. Shannon estimated this through clever experiments asking people to guess the next letter. The gap between 5 and 1.5 is the room for compression."

- Title: "Entropy of English"
- Items: "Fixed-length: 5 bits/letter", "Entropy: about 1.0-1.5 bits/letter", "Shannon's guessing experiments"

### Scene 7: Summary (50s)
**Narration:** "Entropy is the fundamental limit of lossless compression. Huffman coding achieves near-optimal performance. English text has far less entropy than its alphabet size suggests. Next, we look at what happens when we have two random variables, not just one."

- Title: "Key Takeaways"
- Items: "H(X) is the compression limit", "Huffman coding is near-optimal", "Redundancy = room for compression"
- play_outro(next="Joint Entropy and Mutual Information", next_playlist="Information Theory")
