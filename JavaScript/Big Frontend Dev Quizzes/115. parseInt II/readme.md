## [115. parseInt II](https://bigfrontend.dev/quiz/parseInt-II)

### Approach
The parseInt() function parses a string argument and returns an integer of the specified radix. Here, as a radix is not provided and the input string begins with a value other than 0x, the radix is assumed to be 10 (decimal). Before evaluating the number, all leading whitespaces are also trimmed.

The first three statements are straightforward.

However, although 1e2 technically encodes an integer i.e. 100 , here the result will be just 1. The reason for this is, when parseInt encounters a character that is not a numeral in the specified radix (example e is not a valid character), it ignores it and all succeeding characters and returns the integer value parsed up to that point. In this case, e2 part of string is ignored