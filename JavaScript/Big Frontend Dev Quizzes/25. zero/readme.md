## [25. zero](https://bigfrontend.dev/quiz/zero)

### Approach
1. 0 / 0 --> NaN: Indeterminate form; zero divided by zero is always NaN.
2. Object.is(0, Math.round(-0.5)) --> false: Because 0 is not -0.

### The Three Core ConceptsSigned 
1. `Zero (0 and -0)`: JavaScript differentiates between positive and negative zero. While they are strictly equal (===), they behave differently when used as divisors.Special Values 
2. `(Infinity and NaN)`: Dividing by zero in JavaScript does not always throw an error; it typically results in Infinity or NaN (Not a Number).
3. `Object.is() vs. ===`: The Object.is() method is more precise. It can distinguish between $0$ and $-0$, and it correctly identifies that NaN is equal to itself.
4. `BigInt Division by Zero`: Attempting 1n / 0n will not return Infinity or NaN; it will throw a RangeError