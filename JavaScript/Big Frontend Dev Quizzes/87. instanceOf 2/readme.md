## [87. instanceOf 2](https://bigfrontend.dev/quiz/instanceOf-2)

### Approach
The instanceof operator tests to see if the prototype property of a constructor appears anywhere in the prototype chain of an object. The return value is a boolean value.

```
console.log(Function instanceof Object) // true
// Object.getPrototypeOf(Function) is not equal to Object.prototype
// it goes further in chain
// Object.getPrototypeOf(Object.getPrototypeOf((Function)) is equal to Object.prototype
console.log(Object instanceof Function) // true
// Object.getPrototypeOf(Object) is equal to Function.prototype
```

### Important
[https://stackoverflow.com/questions/23622695/why-in-javascript-both-object-instanceof-function-and-function-instanceof-obj](https://stackoverflow.com/questions/23622695/why-in-javascript-both-object-instanceof-function-and-function-instanceof-obj)
