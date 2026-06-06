## [154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/solutions/8244875/solution-by-la_castille-zqoe/)

### Approach
#### Divide-and-Conquer
Since linear search is inevitable, the only thing we can control is limiting the search to the minimum.

We split the array into segments and check each one.
* If nums[left]<nums[right]:
  * the segment is already sorted, so the minimum is nums[left].
* If nums[left]=nums[right]:
  * it is ambiguous (indeterminate), so we still need to search.
* If nums[left]>nums[right]:
  * the array is rotated in this segment, so we split again and continue.


#### Instead of performing a linear scan within an indeterminate segment:

The algorithm recursively divides the region into subsegments until it hits the base case of a single element or a strictly sorted range.
* It then aggregates the results using the minimum function.
* In the best case, it can prune a large segment consisting of all duplicates except for the last element.

In the worst case (all elements equal) every segment is indeterminate:

Therefore, no branches get pruned, forcing the algorithm to split down to 1-element segments, which degrades the time complexity to linear time `O(n)`.