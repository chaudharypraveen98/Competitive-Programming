## [105. typeof](https://bigfrontend.dev/quiz/typeof)

### Approach

The typeof operator returns a string indicating the type of the operand's value.

Here we have defined a variable a of type string. Inside the if condition it looks like we are checking if typeof a is string or not and if its not string we go to the if block otherwise else block gets executed.

```
const a = 'BFE.dev'
if (!typeof a === 'string') { // false === "string" 👉🏻 "false" === "string" 👉🏻 false
  console.log('string')
} else {
  console.log('not a string')
}
// "not a string"

```