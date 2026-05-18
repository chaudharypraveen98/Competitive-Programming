## [70. function](https://bigfrontend.dev/quiz/function)

### Approach
1. Line 1: Hoisting will take place, Function declaration will be hoisted and in the global object foo will be equal to a function.
2. Line 2: foo variable will be hoisted. Now since foo keyword is already present in the global object as a function it will get replaced by foo variable (foo=2).
3. Line 3: It will have no effect due to the below-mentioned rule.
4. Line 4: Since foo is not a function it will throw an error.

### Why did this happen?

Because variable assignment has more importance than function declaration (when the name of variable and function are the same)

**Order of Precedence**: `variable Assigment` > `function declaration` > `variable declaration`