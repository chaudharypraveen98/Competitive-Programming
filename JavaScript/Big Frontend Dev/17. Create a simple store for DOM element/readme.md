## [17. Create a simple store for DOM element](https://bigfrontend.dev/problem/create-a-simple-store-for-DOM-node)

### Approach
1. `JSON.stringify` does not work for node, so solution one should be avoided
2. use `Symbol`, and store data in node itself