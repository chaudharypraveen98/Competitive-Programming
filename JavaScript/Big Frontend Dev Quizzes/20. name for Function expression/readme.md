## [20. name for Function expression](https://bigfrontend.dev/quiz/name-for-Function-expression)

### Approach
1. a is a Function Declaration and has data type function
2. b and c are Function Expression and have data type function
3. d is a Named Function Expression This name d is then local only to the function body (scope) hence outside the function body typeof d returns undefined
4. The special case is inside the named function d. The function name is un-reassignable inside the function. You can easily see the difference if you run this in "use strict" mode where it gives an error Uncaught TypeError: Assignment to constant variable. Thus, d will still point to the named function d despite being reassigned to "e"