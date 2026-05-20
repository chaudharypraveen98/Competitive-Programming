## [94. emoji](https://bigfrontend.dev/quiz/emoji)

### Approach
1. [es6-strings-and-unicode-in-depth#unicode](https://ponyfoo.com/articles/es6-strings-and-unicode-in-depth#unicode)
2. JavaScript strings are represented using UTF-16 code units. Each code unit can be used to represent a code point in the [U+0000, U+FFFF] range – also known as the “basic multilingual plane” (BMP).
3. For code points beyond U+FFFF, you’d represent them as a surrogate pair. That is to say, two contiguous code units. For instance, the emoji '👍' code point is represented with the '\uD83D\uDC4D' contiguous code units.
4. String.length property returns the number of code units in the string. While this is usually the same as character length, using characters that are outside the BMP([U+0000, U+FFFF] range) can return a different length