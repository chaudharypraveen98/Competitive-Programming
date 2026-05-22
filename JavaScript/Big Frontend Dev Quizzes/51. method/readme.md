## [51. method](https://bigfrontend.dev/quiz/method)

### Approach
1. In obj1 we have defined an object method foo. However, in case of obj2 we have defined a property foo which is a function. There's a subtle difference.
2. This code throws Uncaught SyntaxError: 'super' keyword unexpected here error because super is valid only inside methods and not normal property/function.
3. `obj1` is normal instance of `Object` and it doesn't have `prototype`, only constructor function can have `prototype` property. Instance can only has `__proto__` property which point to object pointed by `prototype` property of its constructor funciton. Here. we are making `__proto__` property of `obj1` to a different object.