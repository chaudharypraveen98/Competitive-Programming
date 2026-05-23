## [112. Symbol](https://bigfrontend.dev/quiz/Symbol)

### Approach
1. The in operator tests if a string or symbol property is present in an object or its prototype chain. In this example, in returns true for both keys.
2. The Object.keys() method returns an array of a given object's own enumerable string-keyed property names. This excludes symbols (presumably for backward compatibility since pre-es6 code might not be handling symbol keys). That's why, Object.keys(a) will only consider the key BFE, and length of the returned array will be 1