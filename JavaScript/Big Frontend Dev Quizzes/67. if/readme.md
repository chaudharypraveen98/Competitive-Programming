## [67. if](https://bigfrontend.dev/quiz/if)

### Approach
1. Function declarations are not block scoped. This means a function declared in a block will leak outside it. If and when Javascript actually executes the block and creates the function for you.
2. In the first if, JS will actually create the function foo that is available outside the block too. When we are declaring the function inside the if block, with a false condition, JS won’t execute the if block hence won’t create the function bar.
3. So, you get an error while calling the function bar.