/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  k = nums.length - k;
  function quickSelect(left, right) {
    const pivot = nums[right];
    let p = left;
    for (let i = left; i < right; i++) {
      if (nums[i] <= pivot) {
        [nums[i], nums[p]] = [nums[p], nums[i]];
        p += 1;
      }
    }
    [nums[p], nums[right]] = [nums[right], nums[p]];
    if (p < k) {
      return quickSelect(p + 1, right);
    } else if (p > k) {
      return quickSelect(left, p - 1);
    } else {
      return nums[p];
    }
  }
  return quickSelect(0, nums.length - 1);
};

console.log(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4));

// var findKthLargest = function (nums, k) {
//   // Create a min-heap using a priority queue
//   let minHeap = new MinPriorityQueue();

//   // Add the first k elements to the heap
//   for (let i = 0; i < k; i++) {
//     //minHeap.enqueue(nums[i]): Adds the element nums[i] to the min-heap.
//     minHeap.enqueue(nums[i]);
//   }

//   // Iterate through the remaining elements
//   for (let i = k; i < nums.length; i++) {
//     //minHeap.front().element: Retrieves the smallest element in the min-heap without removing it.
//     if (minHeap.front().element < nums[i]) {
//       // minHeap.dequeue(): Removes the smallest element from the min-heap.
//       minHeap.dequeue();
//       // Add the current element
//       minHeap.enqueue(nums[i]);
//     }
//   }

//   // The root of the heap is the kth largest element
//   return minHeap.front().element;
// };
