## [79. Equal III](https://bigfrontend.dev/quiz/equal-iii)

### Approach

```
console.log(2.0 == "2" == new Boolean(true) == "1") // true
// 2 == 2 == true == "1"
// true == true == "1"
// true == "1"
// 1 == 1
// true
```

As per Operator Precedence, equality operator == attempts to convert and compare operands that are of different types and comparisons happen from Left to Right.

Here, it'll convert the string and boolean values to number and then compare

```
Number(2.0) // 2
Number("2") // 2
Number(true) // 1
```