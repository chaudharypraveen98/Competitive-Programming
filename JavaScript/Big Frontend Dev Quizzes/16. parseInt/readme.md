## [16. parseInt](https://bigfrontend.dev/quiz/parseInt)

The "Why": Analyzing the Interaction

To "clear the fog," we must look at the specific signatures of both functions:
- Array.prototype.map(callback): Passes three arguments to the callback for every element: (value, index, array).
- parseInt(string, radix): Accepts two arguments: the string to parse and the radix (mathematical base).

The radix (also known as the base) is a fundamental mathematical concept used by parseInt() to determine how a string should be converted into a number.

The Mathematical Logic

The radix tells the JavaScript engine the base of the numeral system being used, which can range anywhere from 2 to 36.
1. Binary (Base 2): Uses only 0 and 1.
2. Decimal (Base 10): The standard human counting system (0–9).
3. Hexadecimal (Base 16): Uses 0–9 and letters A–F, common in color codes and memory addresses.