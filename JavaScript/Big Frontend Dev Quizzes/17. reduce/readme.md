## [17. reduce](https://bigfrontend.dev/quiz/reduce)

### Approach
1. reduce() method executes a user-supplied callback function on each element of the array, in order, passing in the return value from the calculation on the preceding element. The final result is a single value returned at the end.
2. This method has the following syntax — reduce(callbackFn, initialValue) where initialValue is an optional initial value used. If this parameter is skipped, it's assumed to be the first value of the array.
3. The way the reducer function works is that the first parameter a is the return value of the result of each iteration while the second parameter b is the current element while iterating.
4. Since we are not returning anything from the callback functions here, the function returns undefined implicitly.
5. In the first example, since the initial value is not supplied it defaults to the first item 1. reduce function first compares 1 and 2 and as undefined is returned inside next time it compares undefined and 3
6. In the second example, the initial value is 0. reduce function first compares 0 and 1 and as undefined is returned inside next time it compares undefined and 2 and similarly undefined and 3