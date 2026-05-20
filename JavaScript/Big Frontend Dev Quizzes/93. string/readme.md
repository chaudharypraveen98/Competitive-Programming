## [93. string](https://bigfrontend.dev/quiz/string)

### Approach
1. Starting from ECMAScript 5, a string can be treated as an array-like object, where individual characters correspond to a numerical index.
2. However, when using bracket notation for character access, attempting to delete or assign a value to these properties will not succeed. The properties involved are neither writable nor configurable.
3. Strings are completely immutable.