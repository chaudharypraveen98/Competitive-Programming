## [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/)

### Approach 1 - Naive Approach
We iterate over all possible substring lengths (from 1 to len(s)//2). For each length, we check if the string can be constructed by repeating that substring.

#### Key Data Structures:
Substring: To hold the possible substring that could be repeated to form the string s.

#### Enhanced Breakdown:
- Initialization:
  - Start from the first character.
- Processing Each Substring:
  - For each possible length of substring, check if repeating that substring forms the original string.
- Wrap-up:
  - Return True if any such substring is found, otherwise False.

#### Example:
Given the string "abcabc":
- First check with substring "a" - Does not form the original string.
- Next, check with substring "ab" - Does not form the original string.
- Finally, check with substring "abc" - Forms the original string. Hence, return True.


### Approach 2 - KMP Approach
Problem:

```python
return s in (s + s)[1:-1]
```

### Why?

If:

```text
s = "abab"
```

then:

```text
s + s

abababab
```

Remove first and last character:

```text
bababa
```

Contains:

```text
abab
```

### Intuition

```text
Repeated string
    ↓
Has a rotation equal to itself
    ↓
All rotations appear in s+s
    ↓
Remove trivial copies at ends
    ↓
Check if s still exists
```

### Example

```text
abab
```

Rotation by 2:

```text
abab
```

Same string.

Therefore:

```python
s in (s + s)[1:-1]
```

returns True.
