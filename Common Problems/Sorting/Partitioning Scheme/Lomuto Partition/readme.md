## Lomuto partitioning
Lomuto partitioning is a classic algorithm used to reorganize an array around a specific element called the pivot (usually the last element).

Its main goal is to rearrange the array so that:
1. Everything smaller than or equal to the pivot moves to the left.
2. Everything greater than the pivot moves to the right.
3. The pivot ends up in its final, correctly sorted position.

It is most famous for being the standard partitioning scheme taught for the QuickSort algorithm.

### How It Works (The Two-Pointer Strategy)
Lomuto uses two pointers, let's call them i and j, moving from left to right:
1. j (The Scanner): Scans every element from the start up to the second-to-last element.
2. i (The Boundary): Keeps track of the tail end of the "smaller than pivot" section. It starts just before the array (index = -1).

Whenever arr[j] is less than or equal to the pivot:
1. Move the boundary i forward by one step.
2. Swap arr[i] and arr[j] to push the smaller element into the safe zone.

Once j finishes scanning, the pivot (still sitting at the very end) is swapped with arr[i + 1]. The pivot is now perfectly placed!