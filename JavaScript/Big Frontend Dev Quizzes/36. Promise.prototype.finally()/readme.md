## [36. Promise.prototype.finally()](https://bigfrontend.dev/quiz/Promise-prototype-finally)

### Approach
1. Here, Promise resolves with the value `1` and control goes to the first finally block. A finally callback will not receive any argument hence it logs undefined and it returns a rejected promise.
2. Next control goes to the first catch block and `"error"` parameter is passed to it. It throws another error `"error2"` and control goes to the chained finally. Again, no argument is passed to finally so it logs undefined
3. This finally returns a resolved promise that logs `2`. `.then` is skipped because there was rejected promise before finally 
4. Lastly, the previously thrown error2 is catched and logs `error2`