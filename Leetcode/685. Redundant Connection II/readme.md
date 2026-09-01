## [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/description/)

### Approach
In a rooted tree, the root node has no incoming edges and all other nodes have exactly one incoming edge. Adding one more edge could lead to one of two scenarios:

One node ends up with two parents. In this case, the added edge is easy to identify as it is the second incoming edge to this node. We then have to determine which edge to remove to maintain the tree structure. Typically, since we need to keep the edge that occurs later in the 2D array, we'd remove the earlier edge unless doing so would create a cycle.

There is a cycle in the graph. In this case, all nodes still have exactly one parent but there is a cycle. Since all edges on this cycle are equal in terms of maintaining the tree structure (removing any of them would result in a valid tree), we remove the one that occurs last in the input array as per the problem's instructions.

The complexity of this problem is primarily in identifying which of these two scenarios has occurred and then identifying which edge to remove. This can usually be achieved in linear time by scanning through the list of edges and maintaining a record of the parent of each node.
