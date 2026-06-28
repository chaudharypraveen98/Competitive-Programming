## Quick Sort

Quick Sort is a fast and widely used sorting algorithm based on the divide-and-conquer approach. It works by selecting a pivot element, partitioning the array around it, and then recursively sorting the left and right parts.

### Why Quick Sort?

Quick Sort is efficient for large datasets because it usually runs in O(n log n) time on average. It is an in-place sorting algorithm, which means it does not require much extra memory compared to other methods.

### Core Idea

1. Choose a pivot element.
2. Reorganize the array so that elements smaller than the pivot go to the left and larger ones go to the right.
3. Recursively sort the two subarrays.

### Different Partitioning Approaches

This folder contains three common implementations of Quick Sort using different partitioning strategies.

#### 1. Quick Sort via Naive Partitioning

This is the simplest version. It picks the pivot and creates a temporary list to collect smaller and larger elements separately. Then it copies the values back into the original array and returns the pivot index.

- Easy to understand.
- Uses extra space.
- Good for learning the basic idea of partitioning.

#### 2. Quick Sort via Lomuto Partitioning

Lomuto partitioning is a classic and easy-to-follow method. It uses a single pivot (usually the last element) and a pointer that tracks the boundary of the smaller elements.

- Simple to implement.
- Works well as an introductory partitioning scheme.
- Commonly taught in Quick Sort explanations.

#### 3. Quick Sort via Hoare Partitioning

Hoare partitioning uses two pointers moving from both ends of the array. It is a more efficient in-place partitioning technique and is often considered a more standard implementation in advanced practice.

- More efficient in-place partitioning.
- Slightly more complex than Lomuto.
- Often preferred for practical implementations.

### Time Complexity

- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n^2) (when the pivot is always the smallest or largest element)

### Space Complexity

- Average: O(log n) due to recursion stack
- Worst: O(n)

### Summary

Quick Sort is one of the fastest sorting algorithms in practice. The main difference between the three approaches here is the partitioning method:

- Naive partitioning focuses on clarity.
- Lomuto partitioning is simple and beginner-friendly.
- Hoare partitioning is more efficient and commonly used in real implementations.
