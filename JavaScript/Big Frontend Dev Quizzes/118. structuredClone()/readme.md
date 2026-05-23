## [118. structuredClone()](https://bigfrontend.dev/quiz/structuredclone)

### Approach
Here, we created a custom error object stored in error. Updating error.name only updates the name property, it doesn't mean the prototype is also updated. If we recall how instanceOf works, we'll understand why error is instanceOf Error and not SyntaxError

The instanceof operator tests to see if the prototype property of a constructor appears anywhere in the prototype chain of an object.

In the case of clonededError we are making use of the structuredClone() method that creates a deep clone of a given value using the structured clone algorithm. The reason why clonedError is an instance of SyntaxError, is because SyntaxError is a serializable object and is cloned by structuredClone().

In simple words, when we use structuredClone to clone error, it'll actually set the prototype of clonededError to SyntaxError using the error.name property. This results in clonededError instanceof SyntaxError evaluate to true