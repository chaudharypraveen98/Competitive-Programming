## [889. Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/)

### Approach

- Preorder is `root, left, right`. Postorder is `left, right, root`.
- The root is `pre[0]`, which is also `post[-1]`.
- The hard part is finding where the left subtree ends.
- `pre[1]` is the root of the left subtree.
- In postorder, a subtree's root comes last in its block, so the position of `pre[1]` in `post` marks the end of the left subtree.
- Left size is `mid - post_l + 1`, where `mid` is the index of `pre[1]` in `post`.
- Use a hashmap (value to postorder index) for O(1) lookups.
- Left call: the next `left_size` elements of `pre`, and `post[post_l..mid]`.
- Right call: the rest of `pre`, and `post[mid+1..post_h-1]`.
- The `-1` in `post_h - 1` drops the current root, which is the last element of the postorder block.
- Base cases: an empty range returns `None`, and a single node returns the leaf immediately.
- Bugs to avoid:
  - Look up `idx[preorder[pre_l+1]]`, not `idx[pre_l+1]`.
  - Measure left size from `post_l`, not `pre_l`.
  - Don't skip the single-node base case, or `pre_l + 1` goes out of bounds.
- Index-mixing bugs hide at the top call, where both starts are 0, so test on a deeper call.
- The answer isn't unique because a single-child node is ambiguous. We treat that child as the left one.
- Time is O(n). Space is O(n) for the map plus O(h) for the recursion stack.
- Split-point pattern:
  - Pre + In: find `pre[0]` in inorder.
  - Post + In: find `post[-1]` in inorder.
  - Pre + Post: find `pre[1]` in postorder.