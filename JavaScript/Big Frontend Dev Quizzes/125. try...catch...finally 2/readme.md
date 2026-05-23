## [125. try...catch...finally 2](https://bigfrontend.dev/quiz/try-catch-finally-2)

### Approach
1. In a try...catch...finally scenario, the finally block is always executed irrespective of an error is thrown or not within the try block. Also, Control flow statements like return in the finally block overwrite any completion values of the try block or catch block.
2. In this example, for "BFE.dev" JSON.parse will throw error and control goes to the catch block and "errored" is returned. However, since finally block always executes and we return str from it, the final returned value is "BFE.dev" that gets logged
3. Similarly, for "123", the try block tries to return, but finally block's return value is returned instead.