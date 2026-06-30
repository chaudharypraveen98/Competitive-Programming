## Merge Sort

Merge Sort is a stable divide-and-conquer sorting algorithm. It works by recursively splitting the array into halves, sorting each half, and then merging the sorted halves back together.

### Why Merge Sort?

Merge Sort guarantees O(n log n) time complexity for all cases, making it reliable for large datasets and predictable performance.

### Core Idea

1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves into a single sorted array.

### Advantages of Merge Sort

- Stable sorting algorithm.
- Predictable O(n log n) runtime in best, average, and worst cases.
- Well-suited for linked lists and external sorting.

### Time Complexity

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n log n)

### Space Complexity

- O(n) due to the temporary arrays used during merging.

### Summary

Merge Sort is an efficient and stable sorting algorithm that performs consistently across all inputs. It is often used when stable sorting is required or when working with large datasets where worst-case performance matters.
