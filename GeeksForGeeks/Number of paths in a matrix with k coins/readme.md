Link -> [Number of paths in a matrix with k coins](https://www.geeksforgeeks.org/problems/number-of-paths-in-a-matrix-with-k-coins2728/1)

## Approach
-  Observe the things, we need to move from top left to bottom right and sum of elements along paths must be k.
-  At any point in 2x2 matrix, we have two choices either to move `bottom` or `right` and they are represented by two recursive function
-  we store **result of these two values with target in memo** table for next values which tries to make path with same target with using the same element , it can be directly filled from the memo table.
-  while reaching the bottom, our **sum becomes greater than the target** / **negative**, we simply return 0 without continuing the rest path.
-  Make sure to add base condition, if row and columns goes out of range.
-  Hurray! Done