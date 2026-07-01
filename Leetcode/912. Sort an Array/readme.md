## [912. Sort an Array](https://leetcode.com/problems/sort-an-array/description/)

### Approach
1. Merge Sort
   - ⏰ Time complexity: O(n * log n), in any case we divide array in half up to arrays of size 1 and then perform sorting an smaller parts so even in the worst case time complexity is still will be O(n * log n)
   - 🧺 Space complexity: O(n), since we're creating new n arrays of size 1 and also there some recursion stack space
2. Counting Sort
   1. Initialize a counting array with size 2 * 5 * 10^4 + 1 (to accommodate both positive and negative numbers) and fill it with zeros.
   2. Iterate through each element num in the input nums array:
   3. Increment the corresponding index in the counting array by adding 5 * 10^4 to num to handle negative values.
   4. Initialize write_ind to 0 to track the position in the original nums array for writing sorted values.
   5. Iterate through the counting array with index number_ind and frequency freq:
   6. While freq is not zero, write the value (number_ind - 5 * 10^4) back to the nums array, update write_ind, and decrement freq.
   7. Return the sorted nums array.