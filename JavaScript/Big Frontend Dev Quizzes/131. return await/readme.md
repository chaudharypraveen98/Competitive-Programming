## [131. return await](https://bigfrontend.dev/quiz/return-await)

### Approach

Here, we have a an async function that await Promise.reject(1). The await keyword causes the function to immediately wait for the promise to settle (reject in this case). Since the promise is rejected with the value 1, the catch block is executed, logging 1.

b is an async function that returns Promise.reject(2) without await. Because the promise rejection is not awaited, the rejection is not caught by the catch block inside b. The rejection will propagate to wherever b is awaited (Inside start function in this case)

Thus when we execute start(), a is awaited and it logs 1 because of the rejection handling. When b is awaited, it results in an unhandled promise rejection i.e a warning or error, depending on the environment (but here it won't be part of the logs)