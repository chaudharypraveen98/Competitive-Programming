Link -> [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/)


Reference [Leetcode ans](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/solutions/1075895/easy-python-beats-100-time-and-space)
## Approach
1. Initialize the array with zero value of len(boxes)
2. Create cost of element left and rights in respect to current element using two array left_arr and right_arr
3. If left-1 == "1" increase the leftCount and simply add the leftCount to leftCost and eventually to res array
4. Similarly do the right array
5. Hurray ! Done