# Counting Sort

## Idea
Counting Sort is a **non-comparison based** sorting algorithm. Instead of comparing elements, it counts how many times each value occurs, then uses that count to place elements directly into their sorted position.

It works best when the range of input values (`k`) is not significantly larger than the number of elements (`n`).

---

## When to Use
- Input consists of **non-negative integers** (or values easily mapped to integers).
- The range of values `k` is small relative to `n`.
- You need a **stable** sort.
- Examples: sorting scores (0–100), sorting characters, sorting ages, radix sort's subroutine.

---

## Algorithm Steps
1. Find the maximum value `max` in the input array (to know the range).
2. Create a `count` array of size `max + 1`, initialized to 0.
3. Traverse the input array and increment `count[value]` for each element.
4. Transform `count` array into a **prefix sum** array — `count[i]` now holds the position (index) where the last occurrence of value `i` should go in the output.
5. Build the `output` array by traversing the input array **from right to left** (this keeps the sort stable), placing each element at `output[count[value] - 1]`, then decrementing `count[value]`.
6. Copy `output` back into the original array (if needed).

---

## Pseudocode
```
function countingSort(arr):
    max = max(arr)
    count = array of size (max + 1), filled with 0

    // Step 1: Count occurrences
    for num in arr:
        count[num] += 1

    // Step 2: Prefix sums (cumulative count)
    for i from 1 to max:
        count[i] += count[i - 1]

    // Step 3: Build output array (traverse right to left for stability)
    output = array of size len(arr)
    for i from len(arr) - 1 down to 0:
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1

    return output
```

---

## Python Implementation
```python
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Prefix sums
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output (stable: iterate input in reverse)
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num

    return output


# Example
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))  # [1, 2, 2, 3, 3, 4, 8]
```

---

## Handling Negative Numbers
If the array has negative numbers, shift all values by `abs(min(arr))` before counting, then shift back when producing the output.

```python
def counting_sort(arr):
    if not arr:
        return arr
        
    # 1. Find both min and max to handle negative numbers
    min_val = min(arr)
    max_val = max(arr)
    
    # 2. Determine the exact range size needed
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # 3. Shift each number by subtracting min_val to safely map to index
    for num in arr:
        count_arr[num - min_val] += 1
    
    # 4. Prefix sum accumulation
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # 5. Fill output array from the back (using shifted indices)
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    return output_arr

print(counting_sort([5,1,1,2,0,0]))
```

---

## Complexity Analysis
| Aspect            | Complexity   |
|-------------------|--------------|
| Time (Best)       | O(n + k)     |
| Time (Average)    | O(n + k)     |
| Time (Worst)      | O(n + k)     |
| Space             | O(n + k)     |
| Stable?           | Yes          |
| In-place?         | No           |

- `n` = number of elements
- `k` = range of input values (max - min + 1)

**Key takeaway:** If `k` is very large compared to `n` (e.g., sorting a few numbers but with huge value range), counting sort becomes inefficient — use comparison-based sorts (like quicksort/mergesort) instead.

---

## Why It's Stable
Stability comes from:
1. Building the prefix-sum `count` array (positions correspond to the *last* index for each value).
2. Iterating the **original array from the end to the start** when placing elements into `output`.

This ensures elements with equal values retain their original relative order — important when counting sort is used as a subroutine in **Radix Sort**.

---

## Comparison with Other Sorts
| Algorithm       | Time         | Space   | Stable | Comparison-based |
|-----------------|--------------|---------|--------|-------------------|
| Counting Sort   | O(n + k)     | O(n+k)  | Yes    | No                |
| Quick Sort      | O(n log n)   | O(log n)| No     | Yes               |
| Merge Sort      | O(n log n)   | O(n)    | Yes    | Yes               |
| Radix Sort      | O(d(n + k))  | O(n+k)  | Yes    | No                |

---

## Quick Recap
- Count → Prefix Sum → Place (right to left) → Done.
- Great when value range is small.
- Building block for **Radix Sort**.
- Not comparison-based, so it can beat the O(n log n) lower bound of comparison sorts.