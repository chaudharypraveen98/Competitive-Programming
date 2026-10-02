## [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

### Approach
- **Inorder is always your map/ruler**: No matter what combination you use, inorder is always used to slice boundaries (left and right, mid - 1, mid + 1) to figure out what belongs to the left or right.
- **Pre- means First**: Preorder puts the root first, so you start at index 0 and go forward. You build the Left subtree first because left comes first in normal reading order.
- **Post- means Last**: Postorder puts the root last, so you start at the end and go backward. Because you're working backward, you hit the Right subtree's root first, so you build the right side first!