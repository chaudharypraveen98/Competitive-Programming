## Naive partitioning

Naive partitioning is a simple way to rearrange an array around a chosen pivot element. In this approach, the pivot is usually taken as the last element of the subarray, and the array is rebuilt so that:

1. All elements less than or equal to the pivot come first.
2. All elements greater than the pivot come after them.
3. The pivot ends up in its final partition position.

This method is often taught as a beginner-friendly version of partitioning because it is easy to understand, even though it is not the most efficient one for QuickSort.

### How it works

1. Pick the pivot as the last element of the current subarray.
2. Create a temporary list.
3. Collect all elements less than or equal to the pivot into the temporary list.
4. Collect all elements greater than the pivot into the same temporary list.
5. Copy the temporary list back into the original array.
6. Return the index where the pivot was placed.

### Why it is called "naive"

This approach is simple, but it uses extra space and scans the array multiple times. Because of that, it is not ideal for performance-critical implementations compared to in-place methods like Lomuto or Hoare partitioning.

### Time complexity

- Time: O(n)
- Space: O(n)

### Example

If the array is:

```python
[4, 6, 8, 1, 3, 7, 5, 2]
```

and the pivot is `2`, the partitioned result will place the pivot at its correct index and arrange the remaining elements around it.

### Note

This method is useful for understanding the concept of partitioning, but in real implementations, more efficient in-place partition schemes are preferred.