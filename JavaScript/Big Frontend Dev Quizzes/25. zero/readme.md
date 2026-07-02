# 📝 [25. zero](https://bigfrontend.dev/quiz/zero)

## 📌 Problem Overview

This quiz tests deep understanding of JavaScript's special numeric values: positive zero (`0`), negative zero (`-0`), `Infinity`, and `NaN`. It explores how division by zero behaves, how `Object.is()` differs from `===`, and how BigInt handles edge cases.

```javascript
console.log(1 / 0)
console.log(-1 / 0)
console.log(0 / 0)
console.log(0 === -0)
console.log(Object.is(0, -0))
console.log(Object.is(0, Math.round(-0.5)))
console.log(Object.is(0, Math.round(0.5)))
console.log(0 * Infinity)
console.log(Infinity / Infinity)
console.log(Object.is(0, Math.sign(0)))
console.log(Object.is(0, Math.sign(-0)))
console.log(1 / -0)
console.log(1 / 0)
console.log(1n / 0n)
```

---

## 🚀 Correct Answer

> [!TIP]
> **Output:**
>
> ```text
> Infinity
> -Infinity
> NaN
> true
> false
> false
> false
> NaN
> NaN
> true
> false
> -Infinity
> Infinity
> RangeError: Division by zero
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

This quiz explores **IEEE 754 double-precision floating-point arithmetic** and how JavaScript's type system handles edge cases. The key challenge is understanding that JavaScript maintains a distinction between `+0` and `-0`, how `Object.is()` performs stricter comparison than `===`, and how different numeric operations handle special values.

### ⚡ Key Spec Rules / Concepts

1. **IEEE 754 Signed Zero**: JavaScript stores both positive zero (`+0`) and negative zero (`-0`) as distinct bit patterns, but they are considered strictly equal (`===`). However, division by these values produces different results (Infinity vs. -Infinity).

2. **Division by Zero (Number Type)**: When dividing numbers by zero, the result follows IEEE 754 semantics: `positive / 0 = Infinity`, `negative / 0 = -Infinity`, `0 / 0 = NaN`.

3. **Object.is() Strict Equality**: Unlike `===`, `Object.is()` distinguishes between `+0` and `-0`, and also treats `NaN` as equal to itself. This makes it useful for detecting signed zero.

4. **NaN (Not-a-Number)**: Any operation involving `NaN` propagates `NaN`. Under `Object.is()`, `NaN === NaN` is true (unlike `===` where it's false).

5. **BigInt Division by Zero**: BigInt does not support `Infinity` or `NaN`. Division by zero with BigInt throws a `RangeError`.

6. **Math.sign() with Signed Zero**: `Math.sign(0)` returns `+0`, while `Math.sign(-0)` returns `-0`, preserving the sign information.

---

### Step-by-Step Execution

#### 1. `1 / 0` → `Infinity`

- **Step A**: Positive number divided by positive zero follows IEEE 754 semantics.
- **Step B**: The result is positive infinity, representing an unbounded positive value.
- **Output**: `Infinity`

#### 2. `-1 / 0` → `-Infinity`

- **Step A**: Negative number divided by positive zero.
- **Step B**: The sign is determined by the dividend; negative dividend yields negative infinity.
- **Output**: `-Infinity`

#### 3. `0 / 0` → `NaN`

- **Step A**: Zero divided by zero is an indeterminate form in mathematics.
- **Step B**: IEEE 754 specifies this case results in `NaN` (Not-a-Number).
- **Output**: `NaN`

#### 4. `0 === -0` → `true`

- **Step A**: The strict equality operator `===` treats `+0` and `-0` as equivalent.
- **Step B**: Despite their different bit representations, the comparison returns true.
- **Output**: `true`

#### 5. `Object.is(0, -0)` → `false`

- **Step A**: `Object.is()` performs a more precise comparison than `===`.
- **Step B**: It distinguishes between positive and negative zero by checking the sign bit.
- **Output**: `false`

#### 6. `Object.is(0, Math.round(-0.5))` → `false`

- **Step A**: `Math.round(-0.5)` rounds to the nearest integer with ties going to even. `-0.5` is equidistant from `0` and `-1`.
- **Step B**: With "banker's rounding" (round to even), `-0.5` rounds to `0` (even).
- **Step C**: `Object.is(0, 0)` would be `true`, but since we started with a negative value being rounded, we still get `+0`.
- **Wait, let me reconsider**: Actually, `Math.round(-0.5)` returns `0` (towards positive). `Object.is(0, 0)` is `true`. But the expected output shows `false`, so `-0.5` must round to `-0`.
- **Step C**: Actually in JavaScript, `Math.round(-0.5)` returns `-0` (negative zero). So `Object.is(0, -0)` is `false`.
- **Output**: `false`

#### 7. `Object.is(0, Math.round(0.5))` → `false`

- **Step A**: `Math.round(0.5)` rounds `0.5` to the nearest integer.
- **Step B**: `0.5` is equidistant between `0` and `1`. JavaScript rounds half away from zero, so `0.5` rounds to `1`.
- **Step C**: `Object.is(0, 1)` is `false`.
- **Output**: `false`

#### 8. `0 * Infinity` → `NaN`

- **Step A**: Multiplying zero by infinity is an indeterminate form.
- **Step B**: IEEE 754 specifies this results in `NaN`.
- **Output**: `NaN`

#### 9. `Infinity / Infinity` → `NaN`

- **Step A**: Infinity divided by itself is indeterminate (like $\frac{\infty}{\infty}$ in calculus).
- **Step B**: IEEE 754 specifies this results in `NaN`.
- **Output**: `NaN`

#### 10. `Object.is(0, Math.sign(0))` → `true`

- **Step A**: `Math.sign(0)` returns the sign of zero, which is `+0`.
- **Step B**: `Object.is(0, 0)` checks strict equality including sign; both are positive zero.
- **Output**: `true`

#### 11. `Object.is(0, Math.sign(-0))` → `false`

- **Step A**: `Math.sign(-0)` returns the sign of negative zero, which is `-0`.
- **Step B**: `Object.is(0, -0)` is false because `0` is positive and `-0` is negative.
- **Output**: `false`

#### 12. `1 / -0` → `-Infinity`

- **Step A**: Positive number divided by negative zero.
- **Step B**: The sign is determined by the divisor; dividing by negative zero yields negative infinity.
- **Output**: `-Infinity`

#### 13. `1 / 0` → `Infinity`

- **Step A**: Positive number divided by positive zero.
- **Step B**: Results in positive infinity.
- **Output**: `Infinity`

#### 14. `1n / 0n` → `RangeError: Division by zero`

- **Step A**: BigInt arithmetic does not support `Infinity` or `NaN`.
- **Step B**: Division by zero with BigInt is not permitted and throws a `RangeError`.
- **Step C**: The error is thrown synchronously during evaluation.
- **Output**: `RangeError` (execution halts)

---

## 💡 Key Takeaway

* **Signed Zero Matters**: JavaScript maintains `+0` and `-0` as distinct values internally. While `===` treats them identically, `Object.is()` correctly distinguishes them. This is crucial for numerical operations involving division.
* **Special Value Semantics**: `Infinity`, `-Infinity`, and `NaN` follow IEEE 754 specifications. Understanding indeterminate forms (0/0, 0*Infinity, Infinity/Infinity) is essential for predicting behavior.
* **BigInt Strictness**: BigInt does not accept infinity or NaN; operations that would produce them throw errors instead, making BigInt safer for exact arithmetic.
* **Object.is() vs. ===**: For production code requiring strict numeric comparison, `Object.is()` is the reliable choice when signed zero matters.

---

## 🛠️ Recommendations & Best Practices

* **Use `Object.is()` for Sign-Sensitive Comparisons**: When you need to detect signed zero or handle NaN correctly, prefer `Object.is()` over `===`.
* **Avoid Division by Zero**: Always guard against zero divisors in mathematical operations.
* **Use BigInt for Exact Arithmetic**: When precision is critical and you can't afford floating-point errors, BigInt provides guaranteed exact arithmetic (with the caveat that division by zero throws).

```javascript
// Good practice: Check for zero divisor before division
function safeDivide(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('Division by zero');
  }
  return numerator / denominator;
}

// Using Object.is() for sign-sensitive zero detection
function hasSignedZero(value) {
  return Object.is(value, 0) || Object.is(value, -0);
}

// With BigInt, the language enforces safety:
try {
  console.log(1n / 0n);
} catch (e) {
  console.log('BigInt division by zero caught:', e.message);
}
```

---

## 🧠 Revision Tips & Cheat Sheet

### Visual Flow of Division by Zero

```mermaid
graph TD
    A["Division Operation"] -->|"Is denominator zero?"| B{Zero Check}
    B -->|"No"| C["Normal Division"]
    B -->|"Yes (Number)"| D{Is numerator zero?}
    B -->|"Yes (BigInt)"| E["RangeError"]
    D -->|"Yes"| F["NaN"]
    D -->|"No, Positive"| G["Infinity"]
    D -->|"No, Negative"| H["-Infinity"]
    C --> I["Result"]
    F --> I
    G --> I
    H --> I
    E --> J["Error"]
```

---

## 🔗 Helpful Resources

- [ECMA-262 Specification - Number Division](https://tc39.es/ecma262/#sec-applying-the-multiplicative-operators)
- [MDN Web Docs - Object.is()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is)
- [MDN Web Docs - Signed Zero](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sign#description)
- [IEEE 754 Double Precision Floating Point](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [BFE.dev - Quiz 25](https://bigfrontend.dev/quiz/zero)

---

## 🏷️ Tags

`#SignedZero` `#IEEE754` `#SpecialValues` `#ObjectIs` `#Infinity` `#NaN` `#BigInt` `#SpecDeepDive`