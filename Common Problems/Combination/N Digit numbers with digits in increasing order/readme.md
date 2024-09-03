Link -> [N Digit numbers with digits in increasing order](https://www.geeksforgeeks.org/problems/n-digit-numbers-with-digits-in-increasing-order5903/1)

## Approach
- Observe the pattern, you will create only the patterns in which numbers are keep increasing
- Possible digits can be `[1, 2, 3, 4, 5, 6, 7, 8, 9]`, include 0 if `n = 1`
- Use the combination method to create all the combinations of particular method with condition `len(path) >= n`
- Hurray! Done.