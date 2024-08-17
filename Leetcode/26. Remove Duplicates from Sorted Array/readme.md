Link ->[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Approach
- Observe the pattern and read the question twice. we have return the length of unique items from the starting and we must move the unique items to start.
- We can use the [two pointer approach](../../Common%20Problems/Two%20Pointer%20Approach/readme.md)
- Initialize the `i = 0` and `j = 1`
- If `if nums[i] == nums[j]` increment `j`
- Else increment `i` , swap item at `i` and `j` and increment `j`.
- Hurray Done