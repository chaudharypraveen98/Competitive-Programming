# 126. Word Ladder II

## Description
- Find all shortest transformation sequences from `beginWord` to `endWord`, changing one letter at a time and using only words in the given dictionary.

## Key idea
- Use bidirectional BFS to build the shortest-layer graph of valid transformations, then backtrack from `endWord` to `beginWord` using parent links to generate all shortest paths.

## Approach
### Solution 1: Bidirectional BFS + backtracking
1. Use two frontiers starting from `beginWord` and `endWord`, always expanding the smaller frontier to keep search breadth minimal.
2. Track parent relationships for each new word discovered in the current layer, while stopping when the two search fronts meet at the same word.
3. Reconstruct all shortest paths by recursively following parent links from `endWord` back to `beginWord`.

### Solution 2: Standard BFS + backward path reconstruction
1. Run a single BFS from `beginWord` to build a distance map and parent adjacency list for words reachable on shortest paths.
2. Once `endWord` is reached, perform DFS/backtracking from `endWord` to `beginWord` using stored parent links.
3. Collect each valid path and reverse it to return results from `beginWord` to `endWord`.

## Complexity
- Time: O(N * L * 26) for BFS where N is number of words and L is word length, plus the cost of reconstructing all shortest paths.
- Space: O(N * L) for word storage, parent tracking, and BFS frontiers.

## Notes
- If `endWord` is not in the word list, return an empty list immediately.
- Bidirectional BFS is usually faster on large dictionaries because it reduces the number of visited words compared to standard BFS.
