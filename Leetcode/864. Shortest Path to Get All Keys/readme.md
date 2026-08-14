# [864. Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/description/)

`Use bfs with keys tracking`

## 1. Core Problem & State Representation
* **Pattern**: Shortest Path in an unweighted grid $\rightarrow$ **Standard BFS**.
* **The Pitfall**: A cell $(r, c)$ can be visited multiple times depending on the keys collected.
  * Greedy search (running fresh BFS per key) fails because the nearest key might lead to a suboptimal global path.
* **The Solution**: Expand the BFS state from $(r, c)$ to include key ownership.
  $$\text{State} = (row, col, \text{keys\_held})$$
  $$\text{Visited Set} = \{(r, c, \text{keys\_held})\}$$

---

## 2. Bitmask Technique (Optimal & Idiomatic)
Because the number of keys is small ($K \le 6$), a bitmask tracks the subset of keys in $O(1)$ space and time.

### Quick Bitwise Cheatsheet
| Operation | Goal | Code |
| :--- | :--- | :--- |
| **All $K$ Keys Target** | Set first $K$ bits to `1` | `target = (1 << total_keys) - 1` |
| **Pick up key `val`** | Turn bit `k` ON (`\|`) | `mask \| (1 << (ord(val) - ord('a')))` |
| **Check key for door** | Check if bit `k` is `1` (`&`) | `(mask >> (ord(door.lower()) - ord('a'))) & 1` |

---

## 3. Alternative: Sorted Representation
* Instead of a bitmask, keys can be represented as:
  * A sorted string: `"".join(sorted(keys + new_key))`
  * An immutable collection: `frozenset(keys)` or `tuple(sorted(keys))`
* **Why sorting is necessary**: Appending keys naively treats `"ab"` and `"ba"` as distinct states, causing redundant or invalid traversals.
* **Trade-off**: Sorting strings/tuples adds minor overhead ($O(K \log K)$ per state transition), whereas bitmasking is strictly $O(1)$ bit manipulation.

---

## 4. BFS Invariants & Edge Checklist
1. **Initial State**: Queue starts at `(start_r, start_c, 0, 0)` $\rightarrow$ `(r, c, cost, keys_mask)`.
2. **Initial Visited**: Initialize `visited` with `{(start_r, start_c, 0)}` to include the initial key state `0`.
3. **Early Exit**: When `acquired_keys == target`, return `cost` immediately (guaranteed shortest path by BFS level-order property).
4. **Door Blocking**: If the cell is a lock (`A-F`) and the matching bit is `0`, prune the branch (`continue`).