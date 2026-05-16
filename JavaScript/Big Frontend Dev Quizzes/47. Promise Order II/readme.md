## [47. Promise Order II](https://bigfrontend.dev/quiz/promise-order-II)

### Approach & Key points to remember are -
1. All synchronous code gets executed first
2. The Promise object represents the eventual completion (or failure) of an asynchronous operation and its resulting value. Basically, it's a nonblocking block of code that executes when the call stack is empty
3. The executor is called synchronously by the Promise constructor before even the Promise constructor returns the created object
4. Promises create Microtask which has priority over the Macrotask created by setTimeout.
5. So all code execution can be explained in these steps-
   1. 1 gets printed
   2. 3 and 2 get pushed to the Macrotask queue (remember 3 gets pushed before 2 because of less delay)
   3. 4 and 6 get printed next and the promise is queued to the Microtask queue
   4. 13 also gets printed being a synchronous code
   5. Now since, the call stack is empty. Microtask queue is checked first and promise gets executed. Since it is rejected, it goes into catch block and 8 gets printed
   6. Because of promise chaining as long as no error happens, all subsequent then get executed i.e. 9, 11, undefined and then finally gets invoked so 12 gets printed
   7. Lastly, queued setTimeouts get executed i.e. 3 and 2 will get printed