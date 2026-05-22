## [77. parseInt 2](http://bigfrontend.dev/quiz/parseInt-2)

### Approach
1. Before converting a string to a number parseInt first converts a number to a string. If the number >= 1e+21 or number <= 1e-7 , it's represented in its scientific notation.
2. `1. & 2.` are straightforward, the integer part is 0
3. `3.` Since the number is equal to 1e-7, 0.0000001 gets converted to its scientific notation 1e-7. Now, as soon as parseInt encounters a character that is not a numeral in the specified radix, it ignores it and all succeeding characters and returns the integer value parsed up to that point
4. `4.` If the input string begins with "0x" or "0X" (a zero, followed by lowercase or uppercase X), radix is assumed to be 16 and the rest of the string is parsed as a hexadecimal number. 0x12 in HEX is 18 in decimal
5. `5.` Similar to 3. it ignores e2 and returns 1

```
// 0.0000001.toString() becomes 1e-7
parseInt(0.0000001) // becomes
parseInt(1e-7) // so e-7 gets ignored and it returns only 1
```