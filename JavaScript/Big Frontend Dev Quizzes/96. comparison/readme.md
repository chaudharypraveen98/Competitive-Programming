## [96. comparison](https://bigfrontend.dev/quiz/comparison)

### Approach
1. When using > to compare two operands, if either operand is a number, Javascript will first convert the string to its equivalent number and then numerically compare.
2. Only when both operands are string, they are compared lexicographically. i.e. character by character until they are not equal or there aren't any characters left. The first character of '10' is less than the first character of '9' hence '10' is < '9'