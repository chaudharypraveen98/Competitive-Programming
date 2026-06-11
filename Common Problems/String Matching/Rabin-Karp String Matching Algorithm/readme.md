# Rabin-Karp String Matching Algorithm

The Rabin-Karp algorithm is a string-searching algorithm that uses hashing to find an occurrence of a pattern string within a text. Unlike the naive approach which compares characters at each position, Rabin-Karp uses a **rolling hash** to quickly filter out positions that cannot possibly match the pattern, only performing character-by-character checks when hash values match.

## Python Implementation (`main.py`)

Here is the implementation as defined in [main.py](file:///Users/praveen/Documents/Competitive-Programming/Common%20Problems/Rabin-Karp%20String%20Matching%20Algorithm/main.py):

```python
def rabin_karp(text, pattern):
    MOD = 101
    BASE = 256
    m = len(pattern)

    h = pow(BASE, m - 1, MOD)

    def create_hash(s):
        hsh = 0
        for ch in s:
            hsh = (hsh * BASE + ord(ch)) % MOD
        return hsh

    def roll(old_hash, outgoing, incoming):
        return (
            (old_hash - ord(outgoing) * h) * BASE
            + ord(incoming)
        ) % MOD

    pattern_hash = create_hash(pattern)
    window_hash = None

    for start in range(len(text) - m + 1):
        if window_hash is None:
            window_hash = create_hash(text[:m])
        elif start > 0:
            window_hash = roll(
                window_hash,
                text[start - 1],
                text[start + m - 1]
            )

        if (
            window_hash == pattern_hash
            and text[start:start + m] == pattern
        ):
            return start

    return -1


print(rabin_karp("aabcdqaaabftghj", "aaab"))
```

### Key Parameters & Functions

- **`BASE = 256`**: Represents the size of the alphabet. Since we are encoding standard ASCII characters, 256 is used.
- **`MOD = 101`**: A prime number used to modulo hash values to fit them within standard integer limits and prevent overflow, while minimizing the probability of hash collisions.
- **`h = pow(BASE, m - 1, MOD)`**: Precomputed value representing $\text{BASE}^{m-1} \pmod{\text{MOD}}$, which is the weight of the highest-order digit (the most significant character) in the window of size $m$. This is used to subtract the outgoing character's value during a hash roll.
- **`create_hash(s)`**: Helper function that computes the initial polynomial hash for the pattern and the first window of the text.
- **`roll(old_hash, outgoing, incoming)`**: A constant time $O(1)$ function that computes the hash of the next window by removing the hash contribution of the outgoing character and adding the hash contribution of the incoming character.

### Rolling Function

The key insight is that the base should be larger than the range of character values you're encoding.

If you used:

```python
base = 10
```

then:

```python
'a' = 97
'b' = 98

"ab" = 97 * 10 + 98 = 1068
```

and the positional representation becomes less meaningful because your "digits" (97, 98, etc.) are larger than the base itself. It can still work as a hash, but it tends to produce more collisions and loses the clean positional interpretation.

That's why:

- For lowercase letters (0-25), bases like 26 or 31 are common.
- For ASCII (0-255), 256 or 257 are common.

The rolling hash works because multiplying by the base effectively shifts all characters one position to the left, just like multiplying a decimal number by 10 shifts its digits:

```
123 * 10 = 1230

abc_hash * 256
= shifts a,b,c one position left
```

That's the trick that allows Rabin-Karp to update the hash in $O(1)$ time when the window moves.

```
How do you build 123?
| Step  | Computation       |
|-------|-------------------|
| Start | 0                 |
| Add 1 | 0 × 10 + 1 = 1    |
| Add 2 | 1 × 10 + 2 = 12   |
| Add 3 | 12 × 10 + 3 = 123 |
```

### Workflow

```
Compute Pattern Hash
        ↓
Compute First Window Hash
        ↓
Compare Hashes
        ↓
If Equal → Verify Characters (to handle collisions)
        ↓
Slide Window
        ↓
Update Rolling Hash
        ↓
Repeat
```

### Time Complexity

| Case                    | Complexity | Description |
| ----------------------- | ---------- | ----------- |
| Best/Average            | $O(n + m)$   | When there are few or no hash collisions, we slide the window in $O(1)$ per step. |
| Worst (many collisions) | $O(n \cdot m)$   | When hash values collide frequently, causing redundant full character comparisons at every shift. |
