### Approach
1. First find the element with the help of **binary search**
2. Once get the index of the item, we can easily find the first occurence with the logic **nums[i] == nums[i-1]** and similarly last **nums[i] == nums[i+1]**