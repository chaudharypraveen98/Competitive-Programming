## [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/description/)

## Approach

## Problem
 
Given `nums` and window size `k`, return the median of every contiguous window of size `k` as the window slides across the array.
 
**Standard approach:** two heaps.
- `small` — max-heap, holds the lower half of the current window
- `large` — min-heap, holds the upper half
- Invariant: `len(large) == len(small)` or `len(large) == len(small) + 1`
- Median: top of `large` (odd `k`), or average of both tops (even `k`)
Because elements leave the window over time, some form of **deferred (lazy) deletion** is needed — heaps don't support efficient arbitrary removal.
 
---
 
## Version 1 — Custom class with `(value, index)` tuples + index-based lazy deletion
 
### Bug: wrong comparison for balance check
 
```python
if self.left_size and self.right_size and self.left_max_heap[0][1] > self.right_min_heap[0][1]:
```
 
`[1]` is the **index** stored alongside each value, not the value itself. This compares *which element arrived later in `nums`*, not *which is numerically larger*. Elements could end up on the wrong side of the partition, corrupting the median.
 
**Fix:** compare values, not indices:
```python
if self.left_size and self.right_size and -self.left_max_heap[0][0] > self.right_min_heap[0][0]:
```
 
### Efficiency notes
- Tuples `(value, index)` cost more per heap comparison than plain ints (heapq compares element-by-element, so ties fall through to comparing indices too).
- The index can be dropped entirely: lazy deletion only needs to know *which value* to discard, not *which specific occurrence* — a count map (multiset) is sufficient and simpler.
- Two separate `if` blocks for rebalancing in `add_number` can be collapsed into a single balance step.
---
 
## Version 2 — Two-heap + value-count lazy deletion (first rewrite)
 
Rewrote using `defaultdict(int)` to count pending deletions by value instead of an index set — removes the need to track per-element location.
 
### Bug: `balance()` only called once per window, not per operation
 
```python
for i, num in enumerate(nums):
    add_num(num)
    if i >= k:
        remove_num(nums[i - k])
    if i >= k - 1:
        balance()   # only runs once the window is full
```
 
`balance()` does a **single-step** correction (`if/elif`, moves at most one element). That's only valid if heap sizes can drift by at most 1 between calls. Deferring `balance()` until the window fills lets `small`/`large` drift by many elements first (everything piles into `small` since `large` starts empty), so one corrective step isn't enough — the heaps stay lopsided.
 
**Fix:** call `balance()` after *every* `add_num` and *every* `remove_num`, not just once per window:
 
```python
for i, num in enumerate(nums):
    add_num(num)
    balance()
    if i >= k:
        remove_num(nums[i - k])
        balance()
    if i >= k - 1:
        result.append(...)
```
 
**Verified against `nums=[5,5,8,1,4,7,1,3,8,4], k=8`:**
 
| Window | Sorted | Median |
|---|---|---|
| `[5,5,8,1,4,7,1,3]` | `[1,1,3,4,5,5,7,8]` | 4.5 |
| `[5,8,1,4,7,1,3,8]` | `[1,1,3,4,5,7,8,8]` | 4.5 |
| `[8,1,4,7,1,3,8,4]` | `[1,1,3,4,4,7,8,8]` | 4.0 |
 
Result: `[4.5, 4.5, 4.0]` ✓
 
**Lesson:** in a two-heap lazy-deletion pattern, rebalance after *every single mutation* — batching corrections is an easy way to reintroduce imbalance even when the comparison logic itself is correct.
 
---
 
## Version 3 — Predictive rebalancing (user-provided, index-tagged heaps)
 
A different but valid strategy: instead of tracking heap sizes explicitly, rebalance **at insertion time** by predicting the effect of the *future* removal of the outgoing element.
 
```python
if nums[i] >= large[0][0]:              # new element belongs to `large`
    heapq.heappush(large, (nums[i], i))
    if nums[i - k] <= -small[0][0]:     # outgoing element belongs to `small`
        self.move(large, small)         # pre-compensate now
else:                                    # new element belongs to `small`
    heapq.heappush(small, (-nums[i], i))
    if nums[i - k] >= large[0][0]:      # outgoing element belongs to `large`
        self.move(small, large)         # pre-compensate now
 
# stale elements are physically popped only once they surface at the top
while large and large[0][1] < (i - k + 1):
    heapq.heappop(large)
while small and small[0][1] < (i - k + 1):
    heapq.heappop(small)
```
 
### Why the pre-compensation is needed
 
Removal is lazy — the outgoing element isn't popped until it happens to reach the top of its heap. So the code can't wait for the "real" removal to rebalance; it has to:
 
1. Push the new element (heap grows by 1 now).
2. Check whether the *outgoing* element logically belongs to the *other* heap — if so, that heap will shrink by 1 *later*, once cleanup runs.
3. Move one element between heaps **immediately** to cancel out that future imbalance, so sizes are already correct by the time `get_median` runs — even though the stale entry hasn't been physically removed yet.
### Trace example
 
`nums=[1,3,-1,-3,5,3,6,7], k=3`, at `i=3` (`nums[3] = -3`):
 
- `nums[3] >= large[0][0]` → `-3 >= 1` → **false** → goes to `else` branch (push to `small`)
- Outgoing `nums[0] = 1 >= large[0][0] = 1` → **true** → it belonged to `large` → `move(small, large)`
Sizes stay correct for window `[3, -1, -3]`; `get_median` returns `-1`, matching the true median.
 
### Caveat
 
This is correct, but more fragile than explicit size tracking (Version 2's approach):
- It relies on heap tops always reflecting a valid partition boundary — which only holds because balance is restored on *every* iteration without exception.
- Explicit `small_size` / `large_size` counters (as in Version 2) are easier to reason about, debug, and extend (e.g., if deletions were ever decoupled from strict window order).
---
 
## Summary of takeaways
 
1. **Compare values, not indices**, when tuples carry `(value, index)` — an easy transcription bug.
2. **Rebalance after every mutation**, not in batches — single-step `if/elif` balancing assumes drift of at most 1 between calls.
3. Lazy deletion can be done **by value-count** (simpler, no index tracking needed) or **by index with predictive rebalancing** (works, but requires reasoning about future state at insertion time).
4. All three approaches are O(n log k) time, O(k) space — the differences are in correctness risk and code clarity, not asymptotic complexity.
 