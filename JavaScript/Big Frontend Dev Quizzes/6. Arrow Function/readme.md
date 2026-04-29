## [6. Arrow Function](https://bigfrontend.dev/quiz/6-Arrow-Function)

### Arrow functions do not have their own this:
This also means that we cannot bind the this context or call a arrow function with some "this" context. The this inside arrow function is from the lexical scope. In simple terms, the "this" will be taken from the surrouding scope where the arrow function was written.

```
// Arrow function
const printNameArrowFunc=()=>this.name;
// Normal function
function printNameFunc(){
 return this.name;
}
const obj={
    name:"Alen"
}
console.log(printNameArrowFunc.bind(obj)())  // undefined
console.log(printNameFunc.bind(obj)()) // "Alen"
```

### Arrow functions do not have arguments object also

```
const sum = () => {
  console.log(arguments); // ReferenceError
};
sum(1, 2);
```

### Arrow functions are not constructible
We cannot use arrow functions as constructors

```
const Person = (name) => {
  this.name=name;
 };
const p = new Person(); //TypeError: Person is not a constructor
```