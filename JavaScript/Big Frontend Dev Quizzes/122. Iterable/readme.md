## [122. Iterable](https://bigfrontend.dev/quiz/iterable)

### Approach
The entries() method returns a new array iterator object that contains the key/value pairs for each index in the array. When we run the for...of loop over this iterable, it will repeatedly call the iterator's next() method to produce the sequence of values i.e, in this case, the array elements 1,2,3 and 4 (since we have destructured the array elements as item in the for...of loop itself).

In the first for...of, it console logs 1 and then encounters a break statement causing the control to go outside the loop, but the iterator is not yet completely iterated. So in the second for...of it simply resumes from where we last stopped and prints the next array element i.e. 2 because the iterable is the same.