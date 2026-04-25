## [19. find corresponding node in two identical DOM tree](https://bigfrontend.dev/problem/find-corresponding-node-in-two-identical-DOM-tree)

### Approach
1. use `recursion` to do.
2. `children vs childNodes` : You used node.children. This is usually correct for HTMLElement challenges (which only count elements), but if the problem allowed Text nodes or Comments, node.children would skip them, while node.childNodes would include them. Always check if the input tree could contain non-element nodes.