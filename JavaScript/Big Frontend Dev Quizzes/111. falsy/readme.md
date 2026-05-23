## [111. falsy](https://bigfrontend.dev/quiz/falsy)

### Approach
1. Using !! before something is effectively doing boolean coercion of the operand.
2. 0, -0, 0n, null, false, NaN, undefined, or the empty string ("") are treated as falsy.
3. All other values, including any object, an empty array ([]) are truthy