Link ->[Find the string in grid](https://www.geeksforgeeks.org/problems/find-the-string-in-grid0111/1)

## Approach
- We need to find the string in all 8 directions
- Focus on making the input smaller (main goal of recursion function) by starting wordIndex from 0
- Write all the base condition which result in `False` condition
- Increase or Decrease `row` or `column` or `both` depending on the all the directions.
- Once you found any `True` at a position return `True` and don't wait for others to complete.
- Hurray! you are done.