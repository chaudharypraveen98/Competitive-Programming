## [34. precedence](https://bigfrontend.dev/quiz/precedence)


### Approach
1. Whenever three unary operators are placed one after another it actually becomes a post-increment/decrement operator followed by another operator See Reason
2. But, if there are spaces between the operators, it actually means multiple unary operators one after another

Basically,
```
a +++ a // is same as (a++ + a)
a + + + a // is same as (a +  +(+a)) = a + a
```
Also, remember If used postfix, with operator after operand (for example, x++), the increment operator increments and returns the value before incrementing.