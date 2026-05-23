## [127. JSON.stringify() II](https://bigfrontend.dev/quiz/json-stringify-ii)

### Approach
1. JSON.stringify is used to convert a JavaScript value to a JSON string.
2. `undefined` is not a valid JSON value and values that do not have a JSON representation do not produce a String. Instead they produce the undefined value. If undefined is encountered during conversion when found in an array it is changed to null.

