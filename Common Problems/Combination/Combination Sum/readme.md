Link -> [Combination Sum](https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1)

## Approach
- Observe the pattern, you need to create a sum and repetition of elements is allowed.
- Write base condition `if not arr or target < 0 or start >= len(arr)` to exit the recursion
- As repetition is allowed but it doesn't mean we take same element multiple times at the same position, to avoid this `if i != 0 and arr[i] == arr[i-1]`
- Just complete the backtrack function.
- Hurray! Done.