## [81. setTimeout II](https://bigfrontend.dev/quiz/setTimeout-2)

### Approach
Lexical scope or Static scope defines the physical presence of code. Where you write your code, determines how it is being accessed.

let is block scope. Anything between parenthesis {} is block scope in JavaScript.

In the for loop, only i is block scoped. It is within for loop.
num variable is outside for loop. It's scope is NOT specific to each block of for loop.

setTimeout function runs code asynchronously (non-blocking). When it execute the arrow function (callback) after 100 ms, the entire for loop has finished. After 5 iteration (0 to 4), the value of num is now 4.

Each of the 5 callback function inside setTimeout refers to the same value of num. so each of them logs the value of num as 4