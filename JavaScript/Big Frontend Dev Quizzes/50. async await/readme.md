## [50. async await](https://bigfrontend.dev/quiz/async-await)

### Approach
So all code execution can be explained in these steps-

1. 4 gets printed as its synchronous statement
2. 5 is a setTimeout get pushed to the Macrotask queue
3. async1 gets called and 1 gets printed, then async2 is invoked and 3 gets printed. 2 gets queued to Microtask queue
4. 6 gets printed as it's synchronous inside executer function of the promise while 7 gets queued to Microtask queue
5. 8 gets printed being synchronous
6. Now since, the call stack is empty. Microtask queue is checked first and 2 and 7 gets printed
7. Lastly, queued setTimeout get executed i.e. 5 will get printed

Note that, this order may vary in browsers because of underlying implementations. For example, the same code in Safari prints 4,1,3,6,8,7,2,5