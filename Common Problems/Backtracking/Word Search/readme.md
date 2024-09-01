Link -> [Word Search](https://www.geeksforgeeks.org/problems/word-search/1)

## Approach
- Observe the pattern, we have to recursively find the string in four direction - up, down, left, right
- we use the dfs with backtracking
- Memo table is used to maintain if a node is visited for not.
- If we reach the end, and string is matched, we return 1
- Hurray ! Done.