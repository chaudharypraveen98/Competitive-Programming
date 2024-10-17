Link -> [2637. Promise Time Limit](https://leetcode.com/problems/promise-time-limit/description/?envType=study-plan-v2&envId=30-days-of-javascript)

## Approach
1. Create a wrapper function that takes the original function fn and the time limit t as parameters.
2. Within the wrapper function, return an async function that accepts any number of arguments using the spread operator ...args.
3. Inside the async function, create a new Promise to handle the asynchronous execution.
4. Use setTimeout to set a timer with the time limit t. If the timer expires before the promise is resolved, reject the promise with the string "Time Limit Exceeded".
5. Call the original function fn with the provided arguments ...args and await its completion.
6. If the function completes before the time limit, resolve the promise with the result.
7. Return the promise from the async function.
8. Hurray ! Done