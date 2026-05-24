# 📝 [5. scope](https://bigfrontend.dev/quiz/block-scope-1)

## 📌 Problem Overview

What is the exact output when running the following two loops?

```javascript
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 0)
}

for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 0)
}
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> 5
> 5
> 5
> 5
> 5
> 0
> 1
> 2
> 3
> 4
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

This is a classic question that tests your understanding of **Scoping Rules (`var` vs. `let`)**, **Closures**, and the **Event Loop**.

### Part 1: The `var` Loop

```javascript
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 0)
}
```

1. **Scoping**: Variables declared with `var` are **function-scoped** or **globally-scoped**. They are *not* block-scoped.
2. **Loop Steps**:
   - The loop runs from `i = 0` to `i = 5`.
   - In each iteration, `setTimeout` registers a callback to the Macrotask Queue.
   - The callbacks create a **closure** over the variable `i`. Since `var` is function/globally scoped, **there is only one shared `i` variable** in memory.
   - When the loop terminates, `i` has been incremented to `5`.
3. **Execution**:
   - The synchronous script completes, and the Event Loop processes the Macrotask Queue (timer callbacks).
   - Each of the 5 callbacks executes and prints the *current* value of the shared `i` variable.
   - Since `i` is currently `5` in memory, the output is `5` five times.

---

### Part 2: The `let` Loop

```javascript
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 0)
}
```

1. **Scoping**: Variables declared with `let` (and `const`) are **block-scoped** (scoped to the nearest curly braces `{}`).
2. **Loop Steps**:
   - The ES6 specification mandates a special behavior for `let` in `for` loops: **a new scope and a new `i` binding are created for every single iteration of the loop**.
   - For iteration 0, a block-scoped `i_0 = 0` is created. `setTimeout` registers a callback closing over `i_0`.
   - For iteration 1, a block-scoped `i_1 = 1` is created. `setTimeout` registers a callback closing over `i_1`.
   - This repeats up to `i_4 = 4`.
   - Each callback creates a **closure** over its own separate, immutable iteration-specific variable `i`.
3. **Execution**:
   - Once the stack is clear, the Event Loop executes the timer callbacks.
   - Each callback prints the value of its own private, iteration-scoped `i` binding.
   - **Output:** `0`, `1`, `2`, `3`, `4`.

---

## 💡 Key Takeaway

* **`var` has Function/Global Scope**: Loop iterations share a single, mutable variable.
- **`let`/`const` have Block Scope**: Each iteration in a `for` loop gets a completely new lexical environment binding, preserving the value inside asynchronous callbacks.

---

## 🛠️ Recommendations & Best Practices

* **Never use `var`**: Always default to `const` or `let`. Using `var` introduces bugs related to hoisting and unexpected global leakage.
- **Old ES5 Workaround**: If you ever write in an old ES5 environment where `let` is unsupported, use an **Immediately Invoked Function Expression (IIFE)** to create a new functional scope for each iteration:

  ```javascript
  for (var i = 0; i < 5; i++) {
    (function(currentI) {
      setTimeout(() => console.log(currentI), 0);
    })(i);
  }
  ```

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - **`var` is a single shared whiteboard**: Everyone writes over it, and at the end, only the last number remains.
  - **`let` is a stack of separate post-it notes**: Each iteration writes on its own separate piece of paper and saves it.

---

## 🔗 Helpful Resources

- [MDN Web Docs - Block scoping with let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [MDN Web Docs - Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [BFE.dev - Quiz 5](https://bigfrontend.dev/quiz/block-scope-1)

---

## 🏷️ Tags

`#Scope` `#Closures` `#ES6` `#BlockScope` `#Google` `#Meta` `#Microsoft` `#Asynchronous`
