## [106. Promise.all() II](https://bigfrontend.dev/quiz/Promise-all-II)

### Approach
1. Promise.all() takes an iterable of promises as input and returns a single Promise. This returned promise fulfills when all of the input's promises fulfill, with an array of the fulfillment values. It rejects when any of the input's promises rejects, with this first rejection reason.
2. So when promiseAll(which is just a wrapper function) is invoked, out of the four promises, promise4 rejects with value 4 . Which means the result is no longer available, and an error is thrown which gets captured in the catch and logs 4 to the console.