## [44. Function call](https://bigfrontend.dev/quiz/Function-call)

### Approach
1. In this example, when we call the outer function, it prints 1 and then returns an object with another function a. By calling it like a().a() we invoke the a method of this returned object too. That's why it prints 2.
2. On the last line, when we write return a(), its actually a function invocation of outer function a. Hence, it prints 1 again