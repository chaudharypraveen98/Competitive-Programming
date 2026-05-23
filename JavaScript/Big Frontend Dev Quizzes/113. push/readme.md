## [113. push](https://bigfrontend.dev/quiz/push)

### Approach
Array.push method changes aka mutates the state of original array and returns the new length of array. In functional programming terms it is an impure function. reference

const a = [1,2,3] // original array
const b = a.push(4) // returns the new length of `a` array i.e 4 and assign it to const `b`.  So `b = 4`
const c = b.push(5) // is equivalent to `4.push(5)`. Since numbers are immutable in JavaScript, it is an invalid operation. It logs out 'TypeError'
console.log(c) // Error <---
Array.concat is an pure function i.e it does not change the state of original array. In fact, it returns a new Array with element appended to the end.

so, if we substitute concat with push, we get the expected result:

const a = [1,2,3] // original array
const b = a.concat(4) // adds `4` to the original array, returns a new array and assigns it to const `b`.  So `b = [1,2,3,4]`
const c = b.concat(5) // adds 5 to `b` and returns new array
console.log(c) //[1,2,3,4,5] <---
Side Note: BFE.dev guidelines expects all unexpected errors( TypeError, ReferenceError, SyntaxError) to be submitted as Error.