Link -> [Unique partitions](https://www.geeksforgeeks.org/problems/unique-partitions1041/1)


## Approach
1. Use the [combination](../../Common%20Problems/Combination/Combination/readme.md) method with [backtracking](../../Common%20Problems/Backtracking/README.md)
2. Just observe the pattern making target/goal to zero
3. Neglect the repetitive pattern using `path and path[-1] < i` clause.
4. Hurray! we are done