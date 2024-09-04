Link ->[Permutation with Spaces](https://www.geeksforgeeks.org/problems/permutation-with-spaces3627/1)

## Approach
- Observe the pattern, you will notice you need to create all the patterns/combinations which contains all the characters
- Base condition `start >= len(s)`, we will terminate our recursive function
- we take current character or sum of characters and then take rest left string to next recursive function by incrementing start.
- Hurray! We are done.