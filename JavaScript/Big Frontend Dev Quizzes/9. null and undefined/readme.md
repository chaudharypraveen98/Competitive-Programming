## [9. null and undefined](https://bigfrontend.dev/quiz/null-and-undefined)

### Approach
1. `undefined` in array is converted to `null` in `JSON.stringify` .
2. `In Math Operators`: null is coerced to 0, but undefined is coerced to NaN.
   1. Addition : `null + 1 -> 0 + 1 = 1` , `undefined + 1 -> NaN + 1`
   2. Multiplication & Division: `null * 10 -> 0 * 10 = 0` , `undefined * 10 -> NaN * 10 = NaN`
   3. Comparison (Greater/Less Than): `null >= 0 -> true` (Coerced to 0 >= 0).`undefined >= 0 -> false` (Coerced to NaN >= 0, and NaN is never greater than, less than, or equal to anything).
3. Null and Undefined : The behavior of null and undefined changes depending on the operator:
   1. `Equality (==)`: Only equal to each other.