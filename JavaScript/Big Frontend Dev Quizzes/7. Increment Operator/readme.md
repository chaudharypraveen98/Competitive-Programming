# 📝 [7. Increment Operator](https://bigfrontend.dev/quiz/Increment-Operator)

## 📌 Problem Overview

What is printed to the console when executing the following script?

```javascript
let a = 1
const b = ++a
const c = a++
console.log(a)
console.log(b)
console.log(c)
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> 3
> 2
> 2
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

This quiz evaluates your understanding of the **Increment Operator (`++`)** under two different evaluation modes: **Prefix (`++x`)** and **Postfix (`x++`)**.

### Step-by-Step Execution

1. **Initialization**:
   - `let a = 1`: Declares mutable variable `a` initialized with value `1`.

2. **Prefix Increment (`const b = ++a`)**:
   - The operator `++` is positioned **before** the variable `a` (Prefix).
   - **Step A**: The variable `a` is immediately incremented by `1`. The value of `a` in memory changes from `1` to `2`.
   - **Step B**: The *updated* value (`2`) is returned and assigned to constant `b`.
   - **Status**: `a = 2`, `b = 2`.

3. **Postfix Increment (`const c = a++`)**:
   - The operator `++` is positioned **after** the variable `a` (Postfix).
   - **Step A**: The *current* value of `a` (`2`) is captured and returned to the expression, to be assigned to constant `c`.
   - **Step B**: Immediately afterward, as a side-effect of the postfix operation, `a` is incremented by `1` in memory. The value of `a` changes from `2` to `3`.
   - **Status**: `a = 3`, `b = 2`, `c = 2`.

4. **Console Logs**:
   - `console.log(a)` prints the final value of `a` which is **`3`**.
   - `console.log(b)` prints the value of `b` which is **`2`**.
   - `console.log(c)` prints the value of `c` which is **`2`**.

---

## 💡 Key Takeaway

* **Prefix (`++i`)**: Increments the variable first, then evaluates to the **new** value.
- **Postfix (`i++`)**: Evaluates to the **current** value first, then increments the variable as a side effect.

---

## 🛠️ Recommendations & Best Practices

* **Avoid In-Expression Increments**: Do not combine variable incrementing with assignments or checks in a single statement. It makes code difficult to read and prone to subtle bugs.

  ```javascript
  // Bad & Hard to read
  const nextValue = array[index++]; 

  // Good & Explicit
  const nextValue = array[index];
  index += 1;
  ```

* **Use explicit additions**: Instead of relying heavily on `++` side-effects in complex math expressions, explicitly write `+ 1`.

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - **Position is Priority**:
    - `++a` (Operator first): Increment **first**, read second.
    - `a++` (Variable first): Read **first**, increment second.

---

## 🔗 Helpful Resources

- [MDN Web Docs - Increment (++) Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
- [JavaScript.info - Basic operators, maths](https://javascript.info/operators)
- [BFE.dev - Quiz 7](https://bigfrontend.dev/quiz/Increment-Operator)

---

## 🏷️ Tags

`#Operators` `#IncrementOperator` `#Meta` `#Google` `#Syntax` `#EvaluationOrder`
