## [132. banana](https://bigfrontend.dev/quiz/banana)

### Approach
+ is an operator that has different meaning depending on the context it is used. The addition (+) operator produces the sum of numeric operands or string concatenation. The unary plus (+) operator precedes its operand and evaluates to its operand but attempts to convert it into a number, if it isn't already.

In this example, we actually have a space between two + operators. This resolves to having one being treated as concatenation and other being treated as unary operator. We know that converting a non-numerical string to a number returns NaN thus +'b' becomes NaN

Concatenating everything becomes baNaNa and converting it to lowercase results in banana 🍌