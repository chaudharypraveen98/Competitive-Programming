## [49. `this` IV](https://bigfrontend.dev/quiz/this-4)


### Approach
1. The `call()` method calls a function with a given this value and arguments provided individually.
2. When we don't specify this, it'll refer to the globalThis aka window in the browser's context.
3. `a.foot.call()` makes this point to the window.bar and hence 1 is returned (it also increments bar because of post-increment)
4. `a.foo1()` this time its a normal function call so this will refer to a and returns 10 (again increments it too)
5. `a.foo2.call` is similar to the first case, no argument is passed hence this is the window and it prints 2 (again incremented after returning)
6. In `a.foo2()`, inside the function body foo is executed independently losing context of a. Hence, it again prints global bar i.e. 3