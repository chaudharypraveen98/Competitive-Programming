Link -> [2725. Interval Cancellation](https://leetcode.com/problems/interval-cancellation/?envType=study-plan-v2&envId=30-days-of-javascript)

## Approach
1. Create a time with setInterval
2. setInterval doesn't call initially that's why we need to call once manually
3. and return a function to clear the interval
4. Hurray ! Done