## [18. Promise executor II](https://bigfrontend.dev/quiz/Promise-executor-II)

### Approach
We know that for object comparisons to be true, the object reference should be same. Here, all the variables `p1,p2,p3,p4,p5` store the Promise object, and their comparisons should return false as references are different.

However, the case of `p1 == p3` is true because of how `Promise.resolve()` works.

`Promise.resolve()` returns a Promise object that is resolved with a given value. If the value is a promise, that promise is returned; otherwise, the returned promise will be fulfilled with the value.

Since we are passing `p1` as an argument to `p3`, the same promise object gets returned and hence the reference is also the same.

`p2`, `p4` and `p5` are fulfilled promises