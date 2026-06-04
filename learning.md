# 🧠 Central Revision & Study Guide

Welcome to your central learning and revision dashboard. This document organizes your core patterns, heuristics, and top-tier questions for both **Data Structures & Algorithms (Competitive Programming)** and **Core JavaScript / Web Development**.

---

## 🗺️ Navigation Index
* [💻 Data Structures & Algorithms Patterns](#-data-structures--algorithms-patterns)
* [🏆 Curated DSA Questions & Practice](#-curated-dsa-questions--practice)
* [⚡ JavaScript & Frontend Core Concepts](#-javascript--frontend-core-concepts)

---

## 💻 Data Structures & Algorithms Patterns

Use these key mental models and heuristics when tackling algorithmic problems under time constraints:

### 1. 🔍 Search & Optimization
- **Binary Search**: Don't just think of binary search for sorted lists. Use it when looking for an optimized value where the feasibility function is monotonic (e.g. *Binary Search on Answer* / *Minimizing Maxima*).
- **Sorting Anchors**: When a problem feels complex, try sorting. Many interval, scheduling, and comparison problems become trivial once sorted.

### 2. 🔀 Two-Pointer Heuristics
- **Opposite Direction**: Useful for sorted arrays (e.g., Two Sum, container with most water).
- **Same Direction (Sliding Window)**: Used when searching for consecutive sequences or subarrays meeting constraint thresholds.
- **Fast & Slow**: Used for cycle detection (Floyd's) and finding midpoints in linked lists.

### 3. 🔄 Recursion & Combinatorics
- **Backtracking**: Use for *all permutations*, *combinations*, or *subsets*. Keep a global state, recurse, and then backtrack to undo state changes.
- **Pattern Identification**: If a problem has repeating mathematical patterns, break it down recursively.

### 4. 🧮 Advanced Heuristics
- **Duplicate Prevention**: `nums[i] == nums[i-1]` after sorting is the gold standard pattern to prevent processing duplicate sub-cases.
- **Range Queries**: Use Fenwick Trees (Binary Indexed Trees) or Segment Trees for logarithmic point updates and range sum queries.

---

## 🏆 Curated DSA Questions & Practice

A curated set of highly educational algorithm questions categorized by technique:

### 🎒 Dynamic Programming & Greedy
1. [Optimal Strategy For A Game](./GeeksForGeeks/Optimal%20Strategy%20For%20A%20Game/) — *Minimax DP approach for perfect information games.*
2. [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/) — *Greedy validation using high/low balance tracking.*

### 🗺️ Graphs & BFS/DFS
3. [Replace O's with X's](./GeeksForGeeks/Replace%20O's%20with%20X's/) — *Flood fill / boundary-connected DFS traversal.*

### 🛠️ Array Manipulation & Two Pointers
4. [Shuffle integers](./GeeksForGeeks/Shuffle%20integers/) — *In-place index math and shuffling patterns.*
5. [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/) — *Prefix/suffix accumulated sum array pattern.*
6. [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/description/) — *Character frequency counting.*
7. [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/) — *Classic stack matching pattern.*

### 📑 Backtracking & Palindromes
8. [Find all possible palindromic partitions of a String](./Common%20Problems//Combination/Find%20all%20possible%20palindromic%20partitions%20of%20a%20String/) — *DFS backtracking combined with palindrome validation.*

### 🌲 Advanced Data Structures
9. [1409. Queries on a Permutation With Key](https://leetcode.com/problems/queries-on-a-permutation-with-key/solutions/575019/python-fenwick-tree-o-n-log-n/) — *Fenwick Tree implementation for linear index queries.*

---

## ⚡ JavaScript & Frontend Core Concepts

For a deep-dive, high-density cheatsheet including Spec-Accurate details, refer to the local [learnings.md](./JavaScript/Big%20Frontend%20Dev%20Quizzes/learnings.md) file.

### 🌟 4 Core JS Pillars:
1. **Event Loop & Asynchronous Mechanics**
   - *Microtasks* (Promises, queueMicrotask) are always executed to completion before the next *Macrotask* (`setTimeout`, `setInterval`) is processed.
   - Promise executor functions run **synchronously** immediately inside the constructor.
   - Ref: [1. Promise order](./JavaScript/Big%20Frontend%20Dev%20Quizzes/1.%20Promise%20order/readme.md)

2. **State & Scoping**
   - `var` is function-scoped. `let`/`const` are block-scoped and create separate lexical bindings in loop iterations.
   - Arrow functions bind `this` lexically at creation time and cannot be bound dynamically.
   - Ref: [5. scope](./JavaScript/Big%20Frontend%20Dev%20Quizzes/5.%20scope/readme.md), [6. Arrow Function](./JavaScript/Big%20Frontend%20Dev%20Quizzes/6.%20Arrow%20Function/readme.md)

3. **Loose Equality (`==`) & Coercion Rules**
   - Booleans are coerced to Numbers first (`false -> 0`, `true -> 1`).
   - Objects/Arrays use `ToPrimitive` conversion (`valueOf` -> `toString`) returning primitives like empty strings `""`.
   - Strings are parsed into Numbers.
   - Ref: [8. Implicit Coercion I](./JavaScript/Big%20Frontend%20Dev%20Quizzes/8.%20Implicit%20Coercion%20I/readme.md), [10. Equal](./JavaScript/Big%20Frontend%20Dev%20Quizzes/10.%20Equal/readme.md)

4. **Primitive Nullish Context**
   - `null` and `undefined` only loosely equal (`==`) each other.
   - In math, `null` coerces to `0`, but `undefined` coerces to `NaN`.
   - In arrays, `JSON.stringify` converts `undefined` to `null` to preserve indexing.
   - Ref: [9. null and undefined](./JavaScript/Big%20Frontend%20Dev%20Quizzes/9.%20null%20and%20undefined/readme.md)