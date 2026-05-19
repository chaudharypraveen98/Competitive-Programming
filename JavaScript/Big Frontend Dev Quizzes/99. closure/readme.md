## [99. closure](https://bigfrontend.dev/quiz/closure-1)

### Approach
1. Here, a closure is created when function a is defined such that the returned function within, maintains a reference to the function variable dev = BFE even after the function's execution is completed.
2. In this code snippet, we have an outer variable also, dev declared using let which is later reassigned to bigfrontend. However, when we execute the returned function with a()(), we are logging the closure value "BFE" irrespective of the outer dev value bigfrontend