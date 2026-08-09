# [127. Word Ladder](https://leetcode.com/problems/word-ladder/description/)

## Description
- Find the shortest transformation length from `beginWord` to `endWord` using valid one-letter word changes.

## Key idea
- View each word as a graph node with edges to all dictionary words that differ by exactly one letter.

## Approach
### Solution 1: Standard BFS over word list
1. Track current layer of words with a queue of paths.
2. For each word, compare against dictionary words and collect neighbors with one differing letter.
3. Increment depth each layer and return when `endWord` is found.

### Solution 2: BFS with direct neighbor generation
1. Convert `wordList` to a set for O(1) membership checks.
2. For each word dequeued, generate all one-letter mutations and enqueue valid unseen words.
3. Remove seen words from the set immediately to avoid revisiting.

### Solution 3: Bidirectional BFS
1. Maintain search frontiers from `beginWord` and `endWord`.
2. Always expand the smaller frontier to reduce branching.
3. When a generated neighbor is found in the opposite frontier, return the combined level count.

## Complexity
- Time: O(N * L * 26) in the optimized BFS / bidirectional BFS case, where N is dictionary size and L is word length.
- Space: O(N * L) for queue/frontier and visited structures.

## Notes
- Use Solution 1 for a direct and simple implementation.
- Use Solution 2 when neighbor generation is cheaper than repeated pairwise word comparisons.
- Use Solution 3 when the dictionary is large and search depth is high.
