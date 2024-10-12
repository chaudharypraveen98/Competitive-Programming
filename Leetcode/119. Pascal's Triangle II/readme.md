Link -> [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)

## Approach
1. Write a base condition when cur==1 and cur>n
2. First and Last item is always 1
3. Else other elements are res[-1][i-1]+res[-1][i]
4. return n+1 row
5. Hurray ! Done