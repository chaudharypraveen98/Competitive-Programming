## [101. Equal IV](https://bigfrontend.dev/quiz/Equal-IV)

### Approach
1. In the first comparison as both operands are string the comparison is straightforward and returns false
2. In the second comparison, we are comparing string to a number, here the string is first coerced into a number and then comparison happens i.e "0" is coerced to 0. Thus, returning true