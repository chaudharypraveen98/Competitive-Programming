Link -> [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## Idea / Proof:
1. The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
2. All other containers are less wide and thus would need a higher water level in order to hold more water.
3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

## Approach
1. Define i , j to zero and len - 1
2. calculate the width x = j-1
3. calculate current holding x*min(i,j)
4. remove min i or j
5. Hurray ! Done
