## [65. Function name](http://bigfrontend.dev/quiz/Function-name)

### Approach
1. Here, because the name bar is used within a function expression, it doesn't get declared in the outer scope. With named function expressions, the name of the function expression is enclosed within its own scope.
2. That's why foo() return "BFE", while bar() throws a ReferenceError