## [130. async](https://bigfrontend.dev/quiz/async)

### Approach
1. promise -> Contains the resolved promise object (resolved value is undefined)
2. f -> This function returns the promise.
3. a -> This async function calls f() and returns the promise it resolves to. Since f() returns promise, a() essentially returns promise.
4. b -> This async function calls f() and uses await to wait for the promise to resolve. However, it returns the resolved value of the promise (not the promise itself).
5. c -> This function calls f() and returns the resolved promise.
6. async functions always return a new promise.
7. Therefore all three functions a(),b() and c() return different values and all comparisons log false