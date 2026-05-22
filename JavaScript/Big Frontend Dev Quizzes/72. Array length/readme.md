## [72. Array length](https://bigfrontend.dev/quiz/array-length)

### Approach
1. The parent's length is an instance property, and it overshadows the child class's length property, which is part of the instance's prototype. Basically, you will not be able to override the parent class's properties.
2. I think this behavior might be because variable overriding might break methods inherited from the Parent if we change its type in the Child class.