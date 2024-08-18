Link -> [Replace O's with X's](https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1)


## Approach
- Observe the pattern carefully, You will notice that the elements connected with boundary elements must not be converted, as boundary elements dissatisfy the argument that top, bottom, left and right must be 'X'
- Traverse the border elements and is element is 'O', use dfs and find all the connected nodes.
- Once we know which elements will not be converted, we convert the rest.
- Hurray! Done.

## Youtube
[G-14. Surrounded Regions | Replace O's with X's](https://www.youtube.com/watch?v=BtdgAys4yMk)