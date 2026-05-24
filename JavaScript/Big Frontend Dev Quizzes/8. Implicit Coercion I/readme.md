# 📝 [8. Implicit Coercion I](https://bigfrontend.dev/quiz/Implicit-Conversion-1)

## 📌 Problem Overview

What is logged to the console when executing the following operations?

```javascript
console.log(Boolean('false'))
console.log(Boolean(false))
console.log('3' + 1)
console.log('3' - 1)
console.log('3' - ' 02 ')
console.log('3' * ' 02 ')
console.log(Number('1'))
console.log(Number('number'))
console.log(Number(null))
console.log(Number(false))
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> true
> false
> "31"
> 2
> 1
> 6
> 1
> NaN
> 0
> 0
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

Implicit Coercion in JavaScript operates according to specific, deterministic algorithms defined in the ECMAScript specification.

### 1. `Boolean('false')` -> `true`

- **Spec Rule**: `Boolean(value)` converts a value to a boolean using the internal `ToBoolean` abstract operation.
- **Evaluation**: The argument `'false'` is a non-empty string. By specification, only the following values are **falsy**: `false`, `0`, `-0`, `0n`, `""` (empty string), `null`, `undefined`, and `NaN`. All other values, including any non-empty string (even `'false'`, `'0'`, or `' '`), are **truthy**.
- **Output**: `true`

### 2. `Boolean(false)` -> `false`

- **Evaluation**: Directly converts boolean `false` to `false`.
- **Output**: `false`

### 3. `'3' + 1` -> `"31"`

- **Spec Rule**: The addition (`+`) operator performs either **String Concatenation** or **Numeric Addition**.
- **Algorithm**: If *either* operand is a string (or evaluates to a string during `ToPrimitive`), the addition operator acts as a string concatenation operator.
- **Evaluation**: The left operand `'3'` is a string, and the right operand `1` is coerced to string `"1"`.
- **Output**: `"31"`

### 4. `'3' - 1` -> `2`

- **Spec Rule**: The subtraction (`-`) operator is strictly a mathematical operator. It coerces both operands to numbers using the internal `ToNumber` operation.
- **Evaluation**: The string `'3'` is converted to the number `3`. Then, `3 - 1` is evaluated.
- **Output**: `2`

### 5. `'3' - ' 02 '` -> `1`

- **Evaluation**: Both operands are strings. Because the subtraction (`-`) operator is strictly numerical, both strings undergo `ToNumber` coercion.
  - `'3'` becomes `3`.
  - `' 02 '` is trimmed of leading/trailing spaces, converting it to the number `2`.
  - The operation becomes `3 - 2`.
- **Output**: `1`

### 6. `'3' * ' 02 '` -> `6`

- **Spec Rule**: The multiplication (`*`) operator is strictly mathematical, coercing both operands to numbers.
- **Evaluation**: `'3'` is coerced to `3`, `' 02 '` is coerced to `2`. The operation is `3 * 2`.
- **Output**: `6`

### 7. `Number('1')` -> `1`

- **Evaluation**: Explicitly casts string `'1'` to number `1`.
- **Output**: `1`

### 8. `Number('number')` -> `NaN`

- **Evaluation**: The string `'number'` contains non-numeric characters. Applying `Number()` on a string that cannot be parsed as a mathematical literal evaluates to `NaN` (Not-a-Number).
- **Output**: `NaN`

### 9. `Number(null)` -> `0`

- **Spec Rule**: According to the ECMAScript specification's `ToNumber(argument)` table:
  - `null` explicitly maps to `+0`.
- **Output**: `0`

### 10. `Number(false)` -> `0`

- **Spec Rule**: According to `ToNumber(argument)`:
  - `false` maps to `+0`.
  - `true` maps to `1`.
- **Output**: `0`

---

## 💡 Key Takeaway

* **Addition vs Other Math Operators**: The `+` operator prefers **string concatenation** if any operand is a string. Other mathematical operators (`-`, `*`, `/`, `%`) are **strictly numeric** and will always force both operands into numbers.
- **Falsy Strings**: Any non-empty string, regardless of its contents (like `'false'`), is inherently `truthy`.

---

## 🛠️ Recommendations & Best Practices

* **Use Explicit Conversion**: Never rely on implicit coercion for math operations. Explicitly convert types beforehand to make your code bulletproof:

  ```javascript
  // Bad
  const total = quantity - '2'; 

  // Good
  const total = Number(quantity) - 2;
  ```

* **Avoid Loose Math**: Avoid mixing types inside arithmetic operations.

---

## 🧠 Revision Tips & Cheat Sheet

### Quick Type Conversion Cheat Sheet

| Value | `Boolean(x)` | `Number(x)` | `String(x)` |
|---|---|---|---|
| `false` | `false` | `0` | `"false"` |
| `true` | `true` | `1` | `"true"` |
| `null` | `false` | `0` | `"null"` |
| `undefined` | `false` | `NaN` | `"undefined"` |
| `""` (empty) | `false` | `0` | `""` |
| `" 42 "` | `true` | `42` | `" 42 "` |
| `"abc"` | `true` | `NaN` | `"abc"` |
| `[]` (empty) | `true` | `0` | `""` |
| `[1, 2]` | `true` | `NaN` | `"1,2"` |
| `{}` (object) | `true` | `NaN` | `"[object Object]"` |

---

## 🔗 Helpful Resources

- [MDN Web Docs - Type Coercion](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion)
- [JavaScript.info - Type Conversions](https://javascript.info/type-conversions)
- [BFE.dev - Quiz 8](https://bigfrontend.dev/quiz/Implicit-Conversion-1)

---

## 🏷️ Tags

`#ImplicitCoercion` `#TypeCasting` `#Google` `#Meta` `#Amazon` `#DoubleEquals` `#JavaScriptEngine`
