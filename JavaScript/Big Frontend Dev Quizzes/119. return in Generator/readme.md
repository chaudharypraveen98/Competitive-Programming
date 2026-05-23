## [119. return in Generator](https://bigfrontend.dev/quiz/return-in-generator)

### Approach
1. A return statement in a generator, when executed, will make the generator finish (i.e. the done property of the object returned by it will be set to true).
2. In this case, when we invoke the generator function gen and spread it we see all the values yielded by it. The try block yields 1 and 2 and then return will finish the execution of generator.
3. However, the thing to remember is the finally block is also executed irrespective of whether gen has finished and 5 is yielded. The next return completes the execution. This behavior is consistent with normal functions i.e. if you have try..finally then statements in finally block are still executed despite returning fromtry block