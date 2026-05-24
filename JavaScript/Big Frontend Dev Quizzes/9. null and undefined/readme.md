# 📝 [9. null and undefined](https://bigfrontend.dev/quiz/null-and-undefined)

## 📌 Problem Overview

What is logged to the console when running the following operations on `null` and `undefined`?

```javascript
console.log(JSON.stringify([1,2,null,3]))
console.log(JSON.stringify([1,2,undefined,3]))
console.log(null === undefined)
console.log(null == undefined)
console.log(null == 0)
console.log(null < 0)
console.log(null > 0)
console.log(null <= 0)
console.log(null >= 0)
console.log(undefined == 0)
console.log(undefined < 0)
console.log(undefined > 0)
console.log(undefined <= 0)
console.log(undefined >= 0)
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> "[1,2,null,3]"
> "[1,2,null,3]"
> false
> true
> false
> false
> false
> true
> true
> false
> false
> false
> false
> false
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

The differences between **`null`** (representing the intentional absence of any object value) and **`undefined`** (representing an uninitialized variable or missing property) are strictly defined by the ECMAScript spec across equality, math, and JSON serialization.

---

### 1. JSON Serialization (`JSON.stringify`)

- `JSON.stringify([1, 2, null, 3])` -> **`"[1,2,null,3]"`**
- `JSON.stringify([1, 2, undefined, 3])` -> **`"[1,2,null,3]"`**
  - **Spec Rule**: `JSON.stringify` handles `undefined` in three ways depending on where it is encountered:
    1. Inside an **Array**: `undefined` is serialized as `null` to preserve index positions.
    2. Inside an **Object**: Properties with `undefined` values are completely omitted.
    3. As a **Standalone** value: `JSON.stringify(undefined)` returns `undefined` (not a string).

---

### 2. Strict & Loose Equality (`===` and `==`)

- `null === undefined` -> **`false`**
  - They are of different types (`Null` vs. `Undefined`).
- `null == undefined` -> **`true`**
  - **Loose Equality Algorithm Rule**: The spec states: *If x is null and y is undefined, return true.* They are loosely equal to each other and **only** to each other.
- `null == 0` -> **`false`**
  - `null` is *not* coerced to a number during loose equality comparison. It is only equal to `null` and `undefined`.
- `undefined == 0` -> **`false`**
  - Similarly, `undefined` is only loosely equal to `undefined` and `null`.

---

### 3. Relational Comparisons (`<`, `>`, `<=`, `>=`)

When performing relational comparisons (`<`, `>`, `<=`, `>=`), JavaScript coerces both values to numbers using the `ToNumber` abstract operation.

#### Relational Comparisons for `null` (`ToNumber(null) === 0`)

- `null < 0` -> `0 < 0` -> **`false`**
- `null > 0` -> `0 > 0` -> **`false`**
- `null <= 0` -> `0 <= 0` -> **`true`**
- `null >= 0` -> `0 >= 0` -> **`true`**
  - *Note:* This explains the famous JavaScript gotcha: `null == 0` is `false`, but `null >= 0` is `true`. They use two completely different internal spec algorithms (Equality vs. Relational Comparison)!

#### Relational Comparisons for `undefined` (`ToNumber(undefined) === NaN`)

- `undefined < 0` -> `NaN < 0` -> **`false`**
- `undefined > 0` -> `NaN > 0` -> **`false`**
- `undefined <= 0` -> `NaN <= 0` -> **`false`**
- `undefined >= 0` -> `NaN >= 0` -> **`false`**
  - **Spec Rule**: Any comparison involving `NaN` (even `NaN == NaN` or `NaN <= NaN`) **always** evaluates to `false`.

---

## 💡 Key Takeaway

1. **JSON Array Rules**: `undefined` inside JSON arrays is serialized to `null` to maintain structural alignment.
2. **Equality vs Relational Coercion**:
   - Under loose equality (`==`), `null` and `undefined` only equal each other. They do *not* coerce to numbers.
   - Under relational operators (`<`, `<=`, etc.), they *do* coerce to numbers: `null` becomes `0`, and `undefined` becomes `NaN` (which always compares as `false`).

---

## 🛠️ Recommendations & Best Practices

* **Use Strict Equality (`===`)**: Never use `==` for comparisons unless you are specifically checking for both `null` or `undefined` simultaneously (`x == null`).
- **Handle Null/Undefined before Math**: Always perform defensive nullish checks before doing arithmetic or comparisons:

  ```javascript
  // Bad
  const isEligible = value >= 0; // If value is undefined, it is false!

  // Good
  const isEligible = value !== undefined && value !== null && value >= 0;
  ```

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - **`null` is `0` in math, but stubborn in equality**: It behaves like `0` with `<` and `>`, but refuses to equal `0` with `==`.
  - **`undefined` is `NaN`**: Anything numerical or relational involving `undefined` immediately turns to dust (`NaN`) and returns `false`.

---

## 🔗 Helpful Resources

- [MDN Web Docs - null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
- [MDN Web Docs - undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
- [JavaScript.info - Comparisons](https://javascript.info/comparison)
- [BFE.dev - Quiz 9](https://bigfrontend.dev/quiz/null-and-undefined)

---

## 🏷️ Tags

`#Null` `#Undefined` `#Equality` `#Coercion` `#JSON` `#Google` `#Meta` `#ByteDance` `#JavaScriptSpec`
