## [54. setTimeout(0ms)](https://bigfrontend.dev/quiz/setTimeout-0ms)

### Approach
1. setTimeout() method sets a timer that executes a function or specified piece of code once the timer expires. When this happens the handler gets pushed to a queue where they are executed one by one (if the call stack is empty)
2. Here, 2ms is long enough for other timeouts to be pushed to the queue before it. However, 1ms is not enough and is pushed earlier than even the following 0ms.