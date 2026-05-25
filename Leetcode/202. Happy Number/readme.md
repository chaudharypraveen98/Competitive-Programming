## [202. Happy Number](https://leetcode.com/problems/happy-number/submissions/2012899556/)

### Approach

1. if N == 1: return True [Happy Number]
2. if N repeats itself (that means there's a cycle not ending in 1): return False [Not Happy Number]
3. keep a record of N (in a seen set)
4. update N to sum of square of digits
5. Hurray!!