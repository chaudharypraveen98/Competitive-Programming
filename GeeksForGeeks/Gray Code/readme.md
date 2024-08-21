Link -> [Gray Code](https://www.geeksforgeeks.org/problems/gray-code-1611215248/1)

Youtube ->[Binary to Gray Code Conversion & Vice-versa](https://www.youtube.com/watch?v=R7uuIACpdGQ)

## Approach
- To generate Gray code sequences for N-bit patterns, we can use a backtracking approach.
-  The idea is to generate the (N-1)-bit Gray code sequence and then append '0' to the front of each number to create the N-bit sequence. 
-  After that, we reverse the (N-1)-bit Gray code sequence and append '1' to the front of each number. 
-  Combining these two sequences will give us the complete N-bit Gray code sequence.
-  Hurray! Done