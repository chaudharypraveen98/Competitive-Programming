# String Matching Revision Notes

## Quick Decision Tree

```text
Need substring existence?
│
├── Python → use `pattern in text`
│
└── Interview / Implement yourself
    │
    ├── Need guaranteed O(n + m)?
    │   └── KMP
    │
    └── Need hash-based matching?
        └── Rabin-Karp
```

---

# Complexity Summary

| Algorithm               | Time                      | Space | Finds Index  | Collision Risk |
| ----------------------- | ------------------------- | ----- | ------------ | -------------- |
| Built-in (`in`, `find`) | O(n + m)                  | O(1)  | Yes (`find`) | No             |
| KMP                     | O(n + m)                  | O(m)  | Yes          | No             |
| Rabin-Karp              | Avg O(n + m), Worst O(nm) | O(1)  | Yes          | Yes            |

Where:

* `n` = text length
* `m` = pattern length

---

# Built-in Search

## Existence Check

```python
pattern in text
```

Example:

```python
"abc" in "xxabcxx"
```

Returns:

```python
True
```

---

## First Index

```python
text.find(pattern)
```

Example:

```python
"xxabcxx".find("abc")
```

Returns:

```python
2
```

---

## Why Built-in is Usually Fastest

Python executes substring search in optimized C code.

Advantages:

* No Python loops
* No Python function calls
* No hash computations
* No collision handling
* Optimized memory access

### Rule

For production Python code:

```python
text.find(pattern)
```

is usually preferred over manually implementing KMP or Rabin-Karp.

---

# KMP (Knuth-Morris-Pratt)

## Core Idea

Avoid re-checking characters after a mismatch.

Precompute:

```text
LPS = Longest Prefix which is also Suffix
```

---

## When to Use

Use KMP when:

* Interview asks for string matching algorithm
* Need guaranteed O(n + m)
* Need first occurrence index
* Need all occurrences
* Building your own search utility

---

## Strengths

### Guaranteed Linear Time

```text
O(n + m)
```

No collisions.

No worst-case degradation.

---

### Finds First Match Naturally

Example:

```python
haystack = "sadbutsad"
needle = "sad"
```

Returns:

```python
0
```

---

### Finds All Matches Efficiently

Example:

```text
Text    : AAAAAAA
Pattern : AAA
```

Matches:

```text
0
1
2
3
4
```

---

# KMP Pattern Recognition

## Repeated Substring Pattern

Example:

```python
ababab
```

Build LPS:

```text
[0, 0, 1, 2, 3, 4]
```

Formula:

```python
repeat_len = n - lps[-1]
```

Condition:

```python
lps[-1] > 0 and n % repeat_len == 0
```

---

## Useful Hint

Whenever a problem mentions:

```text
prefix
suffix
longest border
repeated pattern
periodic string
```

Think:

```text
KMP / LPS
```

---

# Rabin-Karp

## Core Idea

Compare hashes instead of strings.

Instead of:

```text
substring == pattern
```

Compare:

```text
hash(substring) == hash(pattern)
```

Then verify actual strings only if hashes match.

---

## Rolling Hash

Move window:

```text
abcdef
```

from:

```text
abc
```

to:

```text
bcd
```

without recomputing the entire hash.

---

## When to Use

Use Rabin-Karp when:

* Multiple pattern searches
* Duplicate substring problems
* Longest duplicate substring
* String hashing problems
* Interview explicitly mentions rolling hash

---

## Strengths

### Multiple Pattern Matching

Can hash many patterns.

Useful when:

```text
1 text
1000 patterns
```

---

### Duplicate Substring Detection

Common in advanced problems.

Examples:

* Longest Duplicate Substring
* Distinct Echo Substrings
* Repeated DNA Sequences

---

## Weaknesses

### Hash Collisions

Different strings may produce:

```text
same hash
```

Therefore verification is required.

Worst case:

```text
O(nm)
```

---

### Python Overhead

Handwritten Rabin-Karp often loses to:

```python
pattern in text
```

because Python loops are slower than optimized C implementations.

---

# Interview Strategy

## If Using Python

### Need Existence

```python
pattern in text
```

### Need Index

```python
text.find(pattern)
```

---

## If Interview Asks Algorithm

### Need Exact Matching

```text
KMP
```

Reason:

```text
Guaranteed O(n + m)
No collisions
```

---

### Need Rolling Hash

```text
Rabin-Karp
```

Reason:

```text
Efficient hash-based matching
Useful for duplicate substring problems
```

---

# Memory Tricks

## KMP

Think:

```text
Prefix
Suffix
LPS
Repeated Pattern
```

---

## Rabin-Karp

Think:

```text
Hash
Rolling Window
Duplicate Substring
```

---

## Built-in Search

Think:

```text
Production Python
Fastest Practical Choice
```

---

# Final Rule

For Python:

```python
pattern in text
text.find(pattern)
```

For Interviews:

```text
KMP -> Exact matching, guaranteed linear time

Rabin-Karp -> Rolling hash, duplicate substring problems
```
