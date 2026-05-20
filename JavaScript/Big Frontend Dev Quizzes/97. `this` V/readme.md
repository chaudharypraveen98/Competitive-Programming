## [97. `this` V](https://bigfrontend.dev/quiz/this-V)

### Approach
1. Here, this inside the log function will point to obj as it's a normal function. Thus, this.list.forEach loops over the array ['1','2','3'].
2. However, inside the forEach callback function, since it's not the obj invoking callback, this will not point to obj. Rather, it will refer to window hence this.prefix will be undefined

