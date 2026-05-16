## [42. Hoisting V](https://bigfrontend.dev/quiz/hoisting-v)

### Approach
1. **Trick 1: Code contains variable shadowing**
- Execution context is created for each function call. It contains information about scope (availability of variables and functions inside this context).
Scope is defined by a chain of Lexical Environments. 
1.  For nested functions or code blocks it looks like: Local scope -> Outer scope -> ... -> Global scope
2.  When function needs to find a variable, it first look at its local scope and if there is no variable declared, it goes to outer scope and so on until global scope
3.  In a first part of code what is happening is 2 function being declared in different scopes, but with the same name. This is called **variable shadowing** and is considered bad practice. If we use the variable, the one closer to the callee **(closer to the local scope)** will be used.

**2. Trick 2: Code contains block-scoped function declaration**
Traditionally function declarations are hoisted differently from variables. They become available immediately (that is why we can call 'em before declaration). But things get tricky when we define functions inside {...} block. In this case if ... {...} statement.

Without "use strict" they hoisted like var variables and undefined before actually being declared