## [3. Promise then callbacks](https://bigfrontend.dev/quiz/3-promise-then-callbacks)

### Approach
1. If `callback` passed to then is not a `function` then `previous value is returned`.
2. Promise.prototype.then() strictly expects a function as its argument. If a non-function (number, string, or even a Promise object) is provided, it is treated as null. This triggers "fallthrough," where the chain ignores that step and passes the last successfully resolved value to the next handler.
3. .then(console.log) : `console.log` is a callback