# 📝 [3. Promise then callbacks](https://bigfrontend.dev/quiz/3-promise-then-callbacks)

## 📌 Problem Overview

What is printed to the console when the following promise chain executes?

```javascript
Promise.resolve(1)
  .then(() => 2)
  .then(3)
  .then((value) => value * 3)
  .then(Promise.resolve(4))
  .then(console.log)
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> 6
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

This quiz tests the concept of **Promise Fallthrough**. The key specification rule is: **`Promise.prototype.then()` expects functions as arguments. If you pass a non-function argument (like a number or a Promise object) to `.then()`, it is treated as if it were `null`, allowing the previous resolved value to pass straight through (fallthrough).**

### Step-by-Step Execution

1. **`Promise.resolve(1)`**:
   - Creates a resolved promise with the value `1`.

2. **`.then(() => 2)`**:
   - The argument is a function `() => 2`.
   - It executes when the microtask runs and returns `2`.
   - The returned value is wrapped in a new resolved promise with the value `2`.

3. **`.then(3)`**:
   - The argument `3` is a primitive number (not a function).
   - According to the ECMAScript spec, if `onFulfilled` is not a function, it is replaced internally with an identity function `(x) => x`.
   - Therefore, the resolved value `2` **falls through** this block untouched.
   - The returned promise is still resolved with `2`.

4. **`.then((value) => value * 3)`**:
   - The argument is a function that receives the incoming value `2`.
   - It computes `2 * 3 = 6` and returns it.
   - The returned promise is resolved with `6`.

5. **`.then(Promise.resolve(4))`**:
   - The argument is `Promise.resolve(4)`. This is a **Promise object**, not a function!
   - This is a common trap. Since it is not a function, this is treated as a non-function argument.
   - The resolved value `6` **falls through** this block untouched.
   - The returned promise is resolved with `6`.

6. **`.then(console.log)`**:
   - The argument `console.log` is a valid function.
   - It receives the incoming value `6` and prints it.
   - **Output:** `6`

---

## 💡 Key Takeaway

* **Promise Fallthrough**: If a non-function argument is passed to `.then()`, JavaScript replaces it internally with the identity function, causing the previous resolved value to "pass through" (fall through) to the next handler in the chain.

---

## 🛠️ Recommendations & Best Practices

* **Always Pass Functions to `.then()`**: Never pass a direct value or another Promise object straight into `.then()`. Instead, wrap it in a callback function:

  ```javascript
  // Bad (triggers fallthrough and resolves asynchronously elsewhere)
  .then(Promise.resolve(4)) 

  // Good (properly chains the promise)
  .then(() => Promise.resolve(4))
  ```

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - *No Function? No Change!* If the argument of `.then()` doesn't start with a function signature `(...) =>` or a function identifier, it is skipped and the value passes right through.

---

## 🔗 Helpful Resources

- [MDN Web Docs - Promise.prototype.then()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
- [JavaScript.info - Promise chaining](https://javascript.info/promise-chaining)
- [BFE.dev - Quiz 3](https://bigfrontend.dev/quiz/3-promise-then-callbacks)

---

## 🏷️ Tags

`#Promises` `#PromiseFallthrough` `#Google` `#Meta` `#Amazon` `#Asynchronous` `#CleanCode`
