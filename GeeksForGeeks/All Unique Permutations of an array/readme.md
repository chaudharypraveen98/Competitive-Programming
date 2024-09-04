Link -> [All Unique Permutations of an array](https://www.geeksforgeeks.org/problems/all-unique-permutations-of-an-array/1)

## Approach
- By Observing the pattern , we are sure that we can select one item from the list and continue this recursive function
- To remove duplicates, we use this condition `i > 0 and arr[i] == arr[i - 1]` and skip these values as array is sorted.
- Hurray ! Done