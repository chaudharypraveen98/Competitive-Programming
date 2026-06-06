## [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/)

### Approach
- Step 1: Check middle element

```
if(nums[mid] == target)
     return true;
```
If target is found, we're done.

- Step 2: Handle duplicates
```
if(nums[low] == nums[mid] && nums[mid] == nums[high])
{
    low++;
    high--;
    continue;
}
```
When all three are equal, we cannot identify the sorted half.

Example:

[1,1,1,1,1]
or

[1,0,1,1,1]
So we safely discard both ends and continue.

- Step 3: Check if left half is sorted

if(nums[low] <= nums[mid])
This means:

 [4,5,6,7 | 0,1,2]
  ^       ^
 low     mid
The portion from low → mid is sorted.

Now check whether target lies inside this sorted range:

if(nums[low] <= target && target <= nums[mid])
If yes:

high = mid - 1;
Search left.

Otherwise:

low = mid + 1;
Search right.

- Step 4: Otherwise right half is sorted

If left half is not sorted:

else

then right half must be sorted.

Example:

[6,7,0,1,2,4,5]
      ^
     mid
Check if target belongs there:

if(nums[mid] <= target && target <= nums[high])
If yes:

low = mid + 1;
Otherwise:

high = mid - 1;