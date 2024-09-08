Link -> [Generate Parentheses](https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1)

## Approach
- Observe the pattern, we have to generate the valid parentheses
- The number of right ")" parentheses doesn't exceed the number of left "("parentheses
- We make sure that pattern start with "(" and end with ")" by using condition left == n and right == n-1, n-1 because we add ")" at last and initialize the left = 1 and pattern with "("
- Using backtracking using recursive function.
- Hurray ! Done. 