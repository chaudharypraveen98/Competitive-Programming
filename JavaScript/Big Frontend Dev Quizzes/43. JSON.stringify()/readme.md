## [43. JSON.stringify()](https://bigfrontend.dev/quiz/json-stringify)

### Appraoch
1. JSON.stringify() method converts a JavaScript object or value to a JSON string following these rules-
   1. Boolean, Number, and String are converted to the corresponding primitive values during stringification
   2. undefined is not a valid JSON value. Such values encountered during conversion are either omitted (in an object) or changed to null ( in an array)
   3. Infinity, NaN, as well as the value null, are all considered null