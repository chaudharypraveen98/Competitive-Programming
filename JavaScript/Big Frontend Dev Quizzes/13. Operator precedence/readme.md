# 📝 [13. Operator precedence](https://bigfrontend.dev/quiz/operator-precedence)

## 📌 Problem Overview

This quiz tests your understanding of JavaScript **operator precedence**, **operator associativity**, and implicit **type coercion** (specifically boolean-to-number conversion in relational and equality operators).

```javascript
console.log(0 == 1 == 2)
console.log(2 == 1 == 0)
console.log(0 < 1 < 2)
console.log(1 < 2 < 3)
console.log(2 > 1 > 0)
console.log(3 > 2 > 1)
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> false
> true
> true
> true
> true
> false
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

The quiz evaluates expressions with chained operators of equal precedence (e.g., `==`, `<`, and `>`). In JavaScript, these operators are left-associative, meaning they evaluate from left to right. The intermediate boolean results of these operations are then coerced into numbers to be compared with the next numeric operand, leading to counter-intuitive outputs.

### ⚡ Key Spec Rules / Concepts

1. **Operator Precedence & Associativity**: Relational operators (`<`, `>`) have a higher precedence than equality operators (`==`). Both sets of operators are **left-associative** (evaluating from left to right). When expressions are chained, e.g., `a < b < c`, they are grouped and evaluated as `(a < b) < c`.
2. **Abstract Equality Comparison (ECMA-262, Section 7.2.14)**: Under the abstract equality comparison algorithm, if one of the operands is a Boolean, it is coerced to a Number via `ToNumber(x)` before comparison. Specifically, `ToNumber(true)` yields `1` and `ToNumber(false)` yields `0`.
3. **Relational Operators Comparison (ECMA-262, Section 7.2.15)**: Under the abstract relational comparison algorithm, comparing a Boolean value with a Number involves converting both operands to numbers (or primitives) and then comparing their numeric values.

---

### Step-by-Step Execution

For each expression/statement executed in the quiz, trace the evaluation step-by-step:

#### 1. `0 == 1 == 2` -> `false`

- **Step A**: Group the left-most equality first because of left-associativity: `(0 == 1) == 2`.
- **Step B**: Evaluate the first comparison `0 == 1`, which is `false`.
- **Step C**: Evaluate the remaining comparison `false == 2`. Since the left operand is a Boolean, apply the `ToNumber` coercion rule, transforming `false` into `0`.
- **Step D**: Compare `0 == 2`, which evaluates to `false`.
- **Output**: `false`

#### 2. `2 == 1 == 0` -> `true`

- **Step A**: Group and evaluate the left-most equality first: `(2 == 1) == 0`.
- **Step B**: Evaluate `2 == 1`, which is `false`.
- **Step C**: Evaluate the remaining comparison `false == 0`.
- **Step D**: Apply the `ToNumber` coercion rule to the Boolean operand `false`, converting it to `0`.
- **Step E**: Compare `0 == 0`, which evaluates to `true`.
- **Output**: `true`

#### 3. `0 < 1 < 2` -> `true`

- **Step A**: Relational operators are left-associative. Group the expression: `(0 < 1) < 2`.
- **Step B**: Evaluate `0 < 1`, which is `true`.
- **Step C**: Evaluate the remaining comparison `true < 2`.
- **Step D**: Coerce the Boolean `true` to a number via `ToNumber(true)`, yielding `1`.
- **Step E**: Compare `1 < 2`, which evaluates to `true`.
- **Output**: `true`

#### 4. `1 < 2 < 3` -> `true`

- **Step A**: Group the expression: `(1 < 2) < 3`.
- **Step B**: Evaluate `1 < 2`, which is `true`.
- **Step C**: Evaluate the remaining comparison `true < 3`.
- **Step D**: Coerce the Boolean `true` to a number via `ToNumber(true)`, yielding `1`.
- **Step E**: Compare `1 < 3`, which evaluates to `true`.
- **Output**: `true`

#### 5. `2 > 1 > 0` -> `true`

- **Step A**: Group the expression: `(2 > 1) > 0`.
- **Step B**: Evaluate `2 > 1`, which is `true`.
- **Step C**: Evaluate the remaining comparison `true > 0`.
- **Step D**: Coerce the Boolean `true` to a number via `ToNumber(true)`, yielding `1`.
- **Step E**: Compare `1 > 0`, which evaluates to `true`.
- **Output**: `true`

#### 6. `3 > 2 > 1` -> `false`

- **Step A**: Group the expression: `(3 > 2) > 1`.
- **Step B**: Evaluate `3 > 2`, which is `true`.
- **Step C**: Evaluate the remaining comparison `true > 1`.
- **Step D**: Coerce the Boolean `true` to a number via `ToNumber(true)`, yielding `1`.
- **Step E**: Compare `1 > 1`, which evaluates to `false`.
- **Output**: `false`

---

## 💡 Key Takeaway

- **Left-Associativity**: Relational (`<`, `>`) and equality (`==`) operators evaluate from left to right. The intermediate boolean result of the first evaluation becomes the left operand of the next.
- **Implicit Boolean Coercion**: A boolean intermediate output (`true` or `false`) is coerced to a number (`1` or `0` respectively) when compared with a number in a subsequent relational/equality evaluation.

---

## 🛠️ Recommendations & Best Practices

- **Avoid Chained Comparisons**: Do not chain relational/equality comparisons directly. Use logical operators (like `&&`) to connect multiple conditions.
- **Use Strict Equality**: Prefer strict equality `===` over abstract equality `==` to prevent unexpected implicit type coercion.

```javascript
// Avoid:
// if (1 < val < 3) { ... }

// Recommended: Use logical AND for compound comparisons
if (val > 1 && val < 3) {
  console.log("val is strictly between 1 and 3");
}

// Recommended: Use strict equality to prevent implicit coercion
if (val === 2) {
  console.log("val is strictly equal to 2");
}
```

---

## 🧠 Revision Tips & Cheat Sheet

### Visual Coercion Path / Logical Flow

> [!WARNING]
> Always wrap node labels containing brackets, parentheses, or spaces in double quotes to avoid Mermaid parsing errors (e.g. use `A["[] == false"]` instead of `A[[] == false]`).

```mermaid
graph TD
    A["3 > 2 > 1"] -->|Evaluate Left| B["(3 > 2) > 1"]
    B -->|Calculate Left| C["true > 1"]
    C -->|ToNumber(true)| D["1 > 1"]
    D -->|Result| E["false"]
    
    F["2 > 1 > 0"] -->|Evaluate Left| G["(2 > 1) > 0"]
    G -->|Calculate Left| H["true > 0"]
    H -->|ToNumber(true)| I["1 > 0"]
    I -->|Result| J["true"]
```

---

## 🔗 Helpful Resources

- [ECMA-262 Specification - Abstract Equality Comparison](https://tc39.es/ecma262/#sec-abstract-equality-comparison)
- [ECMA-262 Specification - Relational Operators](https://tc39.es/ecma262/#sec-relational-operators)
- [MDN Web Docs - Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
- [BFE.dev - Quiz 13](https://bigfrontend.dev/quiz/operator-precedence)

---

## 🏷️ Tags

`#JavaScript` `#OperatorPrecedence` `#TypeCoercion` `#SpecDeepDive`
