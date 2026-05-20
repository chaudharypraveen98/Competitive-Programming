## [88. try...catch](https://bigfrontend.dev/quiz/try-catch)

### Approach
1. We have just written catch and are not even capturing the error parameter so var a declared inside actually becomes global and overwrites outer a hence printing a1 later
2. We have written catch(b) which means we are using b to hold the exception value which is only available locally inside this catch block. Hence, even after declaring b inside, the global value remains unchanged. Thus, printing b
3. We have written catch(error) and are using error variable to capture the error value , so error is a locally scoped variable but c is not. Hence, similar to 1. var c declared inside actually becomes global and overwrites outer c hence printing c1 later.