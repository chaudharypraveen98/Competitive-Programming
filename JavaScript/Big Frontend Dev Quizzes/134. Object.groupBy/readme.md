## [134. Object.groupBy](https://bigfrontend.dev/quiz/object-groupby)

### Approach
items is an array that contains two objects. Using toString on it simple logs all the array elements. Note that, for javascript objects, by default the string value is [object Object]. This gets printed twice as there are two objects inside items

groups contains the result of Object.groupBy static method that will group the elements of items according to the key id. This method returns a null-prototype object with properties for all groups.

An object with a null prototype doesn't inherit any object methods from Object.prototype which includes toString method . Thus, calling groups.toString throws the following error — TypeError: groups.toString is not a function