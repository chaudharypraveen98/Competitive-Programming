## [21. Array I](https://bigfrontend.dev/quiz/Array-I)

### Approach
1. In JavaScript, arrays aren't primitives but are instead Array objects
2. The length property of an Array sets or returns the number of elements in that array. You can set the length property to truncate an array at any time. The thing to remember is that the length property does not necessarily indicate the number of defined values in the array
3. In Array.map() callback is invoked only for indexes of the array which have assigned values (including undefined). It is not called for missing elements of the array
4. Similarly, Array.forEach() is not invoked for index properties that have been deleted or are uninitialized
5. Arrays being very similar to Objects allow Object.keys to be called on it returning the indexes as an array. However, for sparse arrays, only the defined indexes are returned
6. Deleting array element using delete just unassigns the value (making it empty) at that index