## Josephus problem


Problem : -> [https://www.geeksforgeeks.org/problems/josephus-problem](https://www.geeksforgeeks.org/problems/josephus-problem)

### Approach (IBH - recursion)
1. Define the base condition `len(arr)==1`
2. Use the modulo function to get the index to be deleted `currIndex = prevIndex + k -1`. If `currIndex>=len(arr)`, use the modulo function to get the `currIndex = currIndex%len(arr)`
3. Done Hurray