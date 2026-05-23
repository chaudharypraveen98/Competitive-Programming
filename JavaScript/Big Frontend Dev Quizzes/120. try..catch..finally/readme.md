## [120. try..catch..finally](https://bigfrontend.dev/quiz/try-catch-finally)

### Approach
1. When a return statement is used in a function body, the execution of the function is stopped. But, If a return statement is executed within a try block, its finally block, if present, is first executed, before the value is actually returned.
2. In this example, when we invoke func() thy try block gets executed which logs 1 and returns. However, there is also a finally block present which gets executed before returning. Hence, 3 is also logged to the console.