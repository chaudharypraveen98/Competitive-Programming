Link -> [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/)

## Approach
1. We will be using bottom up with recursion approach for this problem
2. writing base condition `cur >= len(cost)`
3. check if current path has been explored in memo table
4. calculate both possibility by `cur+1` and `cur+2 `
5. store the min of above with current val
6. Hurray ! Done