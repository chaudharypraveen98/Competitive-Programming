## [83. Plus Plus](https://bigfrontend.dev/quiz/Plus-Plus)


### Approach
The unary plus operator (+) precedes its operand and attempts to convert it into a number if it isn't already. If it's not possible it returns NaN

In mathematical operators, + works on both numbers and strings (used in string concatenation). Hence, if any of the operands is not a number, using + converts all operand/s to string and concatenates.

The unary operator has higher precedence over the addition operator.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence

```
console.log(1 + 1) // 2
console.log(1 + + 1) // 1 + (+1) = 1 + 1 = 2
console.log(1 + + 1 + 1) // 1 + (+1) + 1 = 1 + 1 + 1 = 3
console.log(1 + + 1 + + 1) // 1 + (+1) + (+1) =  1 + 1 + 1 = 3
console.log(1 + + + 1) // 1 + (+(+1)) = 1 + (+1) = 1 + 1 = 2
console.log(1 + + '1' + + '1') // 1 + (+'1') + (+'1') = 1 + 1 + 1 = 3
console.log('1' + + '1' + + '1') // "1" + (+'1') + (+'1') = "1" + 1 + 1 = "1" + "1" + "1" = "111"
console.log('a' + + 'b') // "a" + (+'b') = a + "NaN" = "aNaN"
console.log('a' + + 'b' + 'c') // "a" + (+'b') +'c' = a + "NaN"  + "c" = "aNaNc"
console.log('a' + + 'b' + + 'c') // "a" + (+'b') + (+'c') = a + "NaN"  + "NaN" = "aNaNNaN"
```