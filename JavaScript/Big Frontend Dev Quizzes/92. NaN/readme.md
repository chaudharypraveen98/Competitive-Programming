## [92. NaN](https://bigfrontend.dev/quiz/NaN)

### Approach
1. `1` and `2` NaN compares unequal (via both == and ===) to any other value including to another NaN value.
2. `3`: `Object.is()` determines whether two values are the same value and returns true when we compare NaN
3. `3` and `5` indexOf uses Strict Equality Comparison and thus [NaN].indexOf(NaN) === -1 , array.includes uses SameValueZero comparison algorithm , thus making [NaN].includes(NaN) true.
4. `4` , `7` and `8` The Math.max() and Math.min() functions return NaN if any parameter isn't a number and can't be converted into one (of course NaN cannot be converted into a number).
5. The Specification Rule: The Array.prototype.indexOf() method uses the Strict Equality Comparison Algorithm (===) under the hood.