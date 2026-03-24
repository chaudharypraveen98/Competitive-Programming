Link -> [79. Word Search](https://leetcode.com/problems/word-search/description/)

## Approach
1. Just use backtracking and pruning


Performance BreakdownSpace Complexity: 
$O(M \times N)$ for the visited_board and $O(L)$ for the recursion stack (where $L$ is word length).Time Complexity: $O(M \times N \times 4^L)$ in the absolute worst case, but your pruning makes the average case significantly faster.