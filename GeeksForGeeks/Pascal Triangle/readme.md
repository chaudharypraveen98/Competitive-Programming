Link -> [Pascal Triangle](https://www.geeksforgeeks.org/problems/pascal-triangle0652/1)

## Approach
- Write base condition `row_no >= n`
- Observe the pattern and you will find that `prev_row[i-1]+prev_row[i]` is the current element and base `i==0` or `i==row_no` is `1`.
- Hurray! We are done with our recursive function