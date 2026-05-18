## [64. reference type](https://bigfrontend.dev/quiz/reference-type)

### Approach
1. In normal javascript functions, this keyword points to who is calling the function (dynamic binding). Thus, when we invoke a function as obj.foo() the this keyword points to obj.
2. Note that, (obj.foo)() is the same as obj.foo() and this again points to obj
3. `()` is a `grouping operator` and is evaluated before execution. Here the logical OR expression || returns the first truthy value i.e. obj.foo which is a plain function foo({console.log(this.msg)}. Later on, when we execute this function, it's just a function without any connection to obj and hence it points to window and window.msg is undefined