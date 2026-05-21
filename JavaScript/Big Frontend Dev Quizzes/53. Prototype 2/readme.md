## [53. Prototype 2](https://bigfrontend.dev/quiz/prototype2)

### Approach
1. Functions like F have prototypes. Object instances, like f, don't.
2. The instance object, in your case f, has an internal reference to the prototype object. This reference is used internally to resolve properties and methods in the prototype chain. However it is not accessible directly, and thus we can't access prototype property of f.