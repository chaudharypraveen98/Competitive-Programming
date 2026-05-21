## [55. sparse array](https://bigfrontend.dev/quiz/sparse-array)

### Approach
1. Array.forEach() is not invoked for index properties that have been deleted or are uninitialized
2. Similarly, In Array.map() callback is invoked only for indexes of the array which have assigned values (including undefined). It is not called for missing elements of the array. But output arrays does contain the holes.
3. The for...of statement creates a loop iterating over iterable objects like an Array. For a sparse array, the holes are treated as undefined
4. The Spread Operator (...) follows a similar behavior and expands an array such that holes are undefined

