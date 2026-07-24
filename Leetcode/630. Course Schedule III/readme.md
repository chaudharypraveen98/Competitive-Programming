## [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/)

### Approach
1. sort by end date and use max heap


### Pattern to understand
[[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]

sort on basis of second index (max completion limit):
[[2,3],[6,8],[6,11],[3,12],[3,13],[3,14],[7,16],[6,16],[10,16],[10,19]]

push 2 total = 2,     2 <=  3
push 6 total = 8,     8 <=  8
push 6 total = 14,    14 <= 11 -> FAILS -> pop largest element so far -> pop 6, total = 8
push 3 total = 11,    11 <= 12
push 3 total = 15,    15 <= 13 -> FAILS -> pop largest element so far -> pop 6, total = 9
push 3 total = 12,    12 <= 14
push 7 total = 19,    19 <= 16 -> FAILS -> pop largest element so far -> pop 7, total = 12
push 6 total = 18,    18 <= 16 -> FAILS -> pop largest element so far -> pop 6, total = 12
push 10 total = 22,   22 <= 16 -> FAILS -> pop largest element so far -> pop 10, total = 12
push 10 total = 22,   22 <= 19 -> FAILS -> pop largest element so far -> pop 10, total = 12

total elements that  stills remain in queue = 4 = result