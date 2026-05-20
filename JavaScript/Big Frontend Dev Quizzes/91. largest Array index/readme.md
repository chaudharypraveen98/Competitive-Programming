## [91. largest Array index](https://bigfrontend.dev/quiz/largest-Array-index)

### Approach
1. The at() method takes an integer value and returns the item at that index, allowing for positive and negative integers. Negative integers count back from the last item in the array. For the last item array[array.length-1], you can also call array.at(-1)
2. JavaScript arrays are zero-based and use 32-bit indexes: the index of the first element is 0, and the highest possible index is 4294967294 (2^32 − 2) which we have assigned as 1
3. Accessing, arr.at(-1) thus returns the last element 1.
4. Also, note that arr[2^32 - 1] = 2 does store 2 at that index however since its more than the max possible length it cannot be accessed by at