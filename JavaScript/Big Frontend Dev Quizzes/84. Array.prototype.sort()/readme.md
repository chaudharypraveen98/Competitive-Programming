## [84. Array.prototype.sort()](https://bigfrontend.dev/quiz/Array-prototype-sort)

### Approach
Array.sort() method sorts the elements of an array in place and returns the sorted array

Note that the array is sorted in place, and no copy is made.

This explains why both a and b get sorted. a is sorted in place while this sorted array is then assigned to b.

As to why numbers don't appear in order, remember that sort expects a compare function that defines the sort order. If omitted, the array elements are converted to strings, then sorted according to each character's Unicode code point value.

When compared in strings, "111" < "2", "1111" < "999", etc.