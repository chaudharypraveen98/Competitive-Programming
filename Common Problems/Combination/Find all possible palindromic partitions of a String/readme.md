Link -> [Find all possible palindromic partitions of a String](https://www.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1)

## Approach
- Observe the pattern, you notice we have find all the palindromic partitions. We try to create each combinations which satisfy the condition
- Create a util function  which will check if substring is a palindromic string. 
- Start partitioning from index 1, 2, 3 ...n 
- Once we have created partition , check if left substring is palindromic string for not. 
- If palindromic, the we find the pattern created by taking the left side all together.
- Else continue the flow, just taking that single element into consideration
- Hurray ! Done.

Still confused : [L17. Palindrome Partitioning](https://www.youtube.com/watch?v=WBgsABoClE0&t=662s) 