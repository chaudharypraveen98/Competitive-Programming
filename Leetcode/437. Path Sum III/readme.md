## [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

### Approach
1. Run DFS from each node and track the path sum for the current branch.
2. Maintain a prefix-sum map for the current root-to-node path.

### Core Mathematical Insight
This is the heart of the algorithm, borrowed from the classic Subarray Sum Equals K problem.

As you traverse down the tree, you maintain a running total called `currPathSum` (the sum from the root to your current node). Imagine there is an earlier node on your current path whose running sum from the root was `oldPathSum`.

The sum of the nodes between that earlier node and your current node is simply:

$$
\text{Current Section Sum} = \text{currPathSum} - \text{oldPathSum}
$$

We want this section sum to equal the target:

$$
\text{currPathSum} - \text{oldPathSum} = \text{target}
$$

Rearranging gives:

$$
\text{oldPathSum} = \text{currPathSum} - \text{target}
$$

So, at any node, you only need to check whether you have previously seen a prefix sum equal to `currPathSum - target` on the current path. Each time that value appears in the map, it represents a valid path ending at the current node, and you add that frequency to the answer.
