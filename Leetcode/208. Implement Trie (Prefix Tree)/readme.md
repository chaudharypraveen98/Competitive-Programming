## [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)


### Let's like a trie but instead of only two child, it can have multiple children.

| Use Case        | Core Functionality                                 | Why Use a Trie?                                                       |
|-----------------|----------------------------------------------------|-----------------------------------------------------------------------|
| Auto-complete   | Predicting the rest of a word based on a prefix.   | All words with the same prefix are stored in the same subtree.        |
| Spell Checker   | Verifying if a word exists and suggesting fixes.   | Fast lookups and easy traversal to find "nearby" valid words.         |
| IP Routing      | Finding the "Longest Prefix Match" for packets.    | Efficiently handles variable-length bit strings in routing tables.    |
| Bioinformatics  | Searching for gene sequences (A, C, G, T).         | Manages massive strings by sharing common sub-sequences.              |
| T9 Texting      | Mapping keypress sequences to dictionary words.    | Quickly narrows down valid word paths from numeric input.             |
| Browser History | Suggesting URLs as you type in the address bar.    | Optimized for prefix-based searching across thousands of strings.     |
| Word Games      | Validating words in games like Scrabble or Boggle. | Can quickly determine if a string is a valid word or a prefix of one. |

### Summary: Trie vs. Hash Table

| Feature         | Hash Table             | Trie                            |
|-----------------|------------------------|---------------------------------|
| Search Speed    | O(1) (average)         | O(L) where L is word length     |
| Partial Matches | Not supported          | Excellent (Prefix search)       |
| Memory          | Can be sparse/wasteful | Saves space for shared prefixes |
| Ordering        | Unordered              | Lexicographically ordered       |
