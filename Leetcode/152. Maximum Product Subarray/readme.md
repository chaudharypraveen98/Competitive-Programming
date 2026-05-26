## [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/)

### 1. Dynamic Programming (Min/Max Tracking)
* **The Core Paradox:** Multiplying by a negative number flips a tiny minimum into a massive maximum and vice-versa[cite: 1731, 1858]. 
* **The Strategy:** Micro-manage state by tracking both running maximum and minimum products up to index $i$[cite: 1786, 1859].
* **The Decision Tree:** At each index, calculate choices for `max_product` and `min_product`[cite: 1834, 1860]:
    1. Start a fresh subarray containing only the current element ($nums[i]$)[cite: 1735, 1860].
    2. Multiply the current element by previous positive progress (`max_product`)[cite: 1736, 1861].
    3. Multiply the current element by a previous negative streak (`min_product`)[cite: 1737, 1862].
* **The Negative Swap:** If $nums[i] < 0$, atomically swap `max_product` and `min_product` *before* recalculating bounds to correctly capture the sign inversion[cite: 1720, 1741, 1863].

### 2. Boundary Scanning (Modified Kadane's)
* **The Core Paradox:** The absolute magnitude of an integer subarray product always grows or stays constant unless it hits a "Reset Wall"[cite: 1801, 1864]. Therefore, the optimal window *must* touch either the prefix or suffix boundary[cite: 1746, 1865].
* **The Strategy:** Macro-manage state by scanning simultaneously from both ends using a **Prefix Scan** (forward) and a **Suffix Scan** (backward)[cite: 1821, 1866].
* **Breaking the Reset Walls:**
    * **Zeros:** Wipes out the sequence[cite: 1806, 1867]. If encountered, immediately reset the cumulative multiplier back to `1` to start a fresh sequence[cite: 1752, 1868].
    * **Odd Negatives:** Makes the full array product negative[cite: 1813, 1869]. To find the maximum positive window, exactly *one* boundary negative must be dropped[cite: 1748, 1870].
* **The Failsafe:** One of the bidirectional scanning paths is mathematically guaranteed to sweep past the single problematic negative number, capturing the optimal isolated window without explicitly searching for it[cite: 1825, 1871].

---

### 📊 Operational Trade-off Matrix

| Metric | Approach 1: Dynamic Programming | Approach 2: Boundary Scanning |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ — Single pass [cite: 1758, 1873] | $O(N)$ — Single pass [cite: 1758, 1874] |
| **Space Complexity**| $O(1)$ — 3 tracking variables [cite: 1759, 1875] | $O(1)$ — 3 tracking variables [cite: 1759, 1875] |
| **Management Style**| **Micro-management:** Explicitly syncs states [cite: 1827, 1876] | **Macro-management:** Relies on array bounds [cite: 1828, 1876] |
| **Interview Edge** | Demonstrates state-machine mastery [cite: 1761, 1877] | Demonstrates mathematical visualization [cite: 1761, 1877] |
| **Edge Case Gotcha**| Must handle signed zero (`-0`) in JS[cite: 1754, 1878]. | Avoid zero-reset bugs; reset to `1` *before* next step[cite: 1752, 1878]. |