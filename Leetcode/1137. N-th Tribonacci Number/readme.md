Link -> [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/description/)

## Approach
1. You can use recursion or iterative approach
2. simply initialize the array with [0, 1, 1] or memo {0: 0, 1: 1, 2: 1}
3. just do arr[i-1]+arr[i-2] + arr[i-3]
4. Hurray ! Done 