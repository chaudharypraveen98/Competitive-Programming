## [129. Function II](https://bigfrontend.dev/quiz/function-ii)

### Approach
Let's go through each case one by one-

1. Function.prototype inherits from Object.prototype.
2. Both Function and Object constructors inherit from Object.prototype
3. Object.constructor is Function, and Function.prototype is not the same as Object.prototype
4. Function is a constructor created by Function, so Function.constructor is Function
5. Object.constructor is Function, not Object
6. Both Array and Function inherit from Function.prototype
7. The Array constructor is created by Function, so Array.constructor is Function
8. Object.__proto__ is Function.prototype, not Function
9. Function inherits from Function.prototype
10. Object is an instance of Object
11. Function is an instance of Function
12. Map is a constructor function, not an instance of Map.
