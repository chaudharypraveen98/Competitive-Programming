## [75. meaningless calculation](https://bigfrontend.dev/quiz/meaningless-calculation)

### Approach
The unary plus operator (+) precedes its operand attempts to convert it into a number, if it isn't already.

The bitwise NOT operator (~) inverts the bits of its operand.

So basically,

```
+[] // 0 since Number([]) = 0
!0 // true since 0 is falsy
~true // -2
~-2 // 1
// another way to think will be is that ~~ cancel out each other and Number(true) is 1
// If we use all this,
(~~!+[]) // 1
```

In the case of unary operators, evaluation happens from Right to Left. Of course, the Grouping operator () is evaluated first. But the overall evaluation will happen from Left to Right. See Operator Precedence

Let's break this down,

```
const num = +((~~!+[])+(~~!+[])+[]+(~~!+[]))
// We know that (~~!+[]) = 1
// num = +(1 + 1 + [] + 1)
// num = +(2 + [] + 1)
// since not all operands are number JS performs string concatenation, String([]) = ""
// num = +('2' + '' + '1') = +("21") = 21
console.log(num) // 21
```