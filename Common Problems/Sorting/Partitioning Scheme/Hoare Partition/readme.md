## Hoare Partition

Hoare Partition is the original partitioning algorithm used in Quicksort, proposed by Tony Hoare. It is usually faster than Lomuto partition because it performs fewer swaps.

### Intuition

Instead of putting the pivot into its final position during partitioning, Hoare partition:
1. keeps two pointers
2. left pointer searches for an element greater than or equal to the pivot
3. right pointer searches for an element less than or equal to the pivot
4. swaps them if they are on the wrong sides

The pointers continue until they cross.

Unlike Lomuto:
- Pivot does not necessarily end up in its sorted position
- The function returns a partition index, not the pivot index.