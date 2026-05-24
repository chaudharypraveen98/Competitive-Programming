# 📝 [4. Promise then callbacks II](https://bigfrontend.dev/quiz/4-Promise-then-callbacks-II)

## 📌 Problem Overview

What is the exact output order when running the following promise chain?

```javascript
Promise.resolve(1)
  .then((val) => {
    console.log(val)
    return val + 1
  }).then((val) => {
    console.log(val)
  }).then((val) => {
    console.log(val)
    return Promise.resolve(3)
      .then((val) => {
        console.log(val)
      })
  }).then((val) => {
    console.log(val)
    return Promise.reject(4)
  }).catch((val) => {
    console.log(val)
  }).finally((val) => {
    console.log(val)
    return 10
  }).then((val) => {
    console.log(val)
  })
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> 1
> 2
> undefined
> 3
> undefined
> 4
> undefined
> undefined
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

This quiz explores several advanced aspects of promises: **value passing, returning promises in `.then()`, `.catch()` recovery, and `.finally()` execution mechanics.**

### Step-by-Step Execution

1. **`Promise.resolve(1)` initiates the chain**:
   - Pushes first `.then((val) => { ... })` onto the microtask queue.
   - Executes with `val = 1`.
   - `console.log(val)` prints **`1`**.
   - Returns `val + 1` which is `2`. This wraps into a resolved promise of value `2`.

2. **Second `.then((val) => { ... })`**:
   - Executes with `val = 2`.
   - `console.log(val)` prints **`2`**.
   - Returns nothing implicitly (`return undefined`). This wraps into a resolved promise of value `undefined`.

3. **Third `.then((val) => { ... })`**:
   - Executes with `val = undefined`.
   - `console.log(val)` prints **`undefined`**.
   - It returns a **nested promise**:

     ```javascript
     return Promise.resolve(3).then((val) => {
       console.log(val)
     })
     ```

   - **Important Spec Rule**: When a promise callback returns a promise, the outer chain "pauses" and waits for this inner promise to settle.
   - The inner `.then()` receives `val = 3`.
   - `console.log(val)` prints **`3`**.
   - The inner promise completes, resolving with `undefined`. Thus, the outer `.then()` resolves with `undefined`.

4. **Fourth `.then((val) => { ... })`**:
   - Executes with `val = undefined` (the resolution of the previous step).
   - `console.log(val)` prints **`undefined`**.
   - Returns `Promise.reject(4)`. The chain now enters a **rejected** state with the reason `4`.

5. **`.catch((val) => { ... })`**:
   - The engine skips any subsequent `.then()` blocks and jumps to the nearest rejection handler.
   - The `.catch()` callback receives `val = 4`.
   - `console.log(val)` prints **`4`**.
   - Since the `.catch()` finishes executing successfully without throwing a new error or returning a rejected promise, it **recovers** the chain. It returns `undefined` implicitly. This wraps into a resolved promise of value `undefined`.

6. **`.finally((val) => { ... })`**:
   - **Key Spec Rule #1**: The `.finally()` callback **receives no arguments**. Thus, `val` is **`undefined`**.
   - `console.log(val)` prints **`undefined`**.
   - **Key Spec Rule #2**: `.finally()` is transparent. It executes clean-up code and, by default, passes the *previous resolution* or *rejection* straight through. It ignores any return values (like `return 10`), **unless** it explicitly throws an error or returns a rejected promise.
   - Since the previous resolution was `undefined` and `.finally` completed successfully, it passes `undefined` forward.

7. **Final `.then((val) => { ... })`**:
   - Receives the forwarded value `undefined`.
   - `console.log(val)` prints **`undefined`**.

---

## 💡 Key Takeaway

1. **Implicit Returns**: Functions without an explicit `return` return `undefined`, resolving the promise chain with `undefined`.
2. **Nested Promises**: Returning a promise inside a `.then()` blocks the outer chain's resolution until the inner promise settles.
3. **Catch Recovery**: A `.catch()` block catches the error and recovers the chain to a resolved state returning `undefined` (unless it throws a new error).
4. **Finally Mechanics**: `.finally()` receives no arguments, and is transparent—its return value is ignored, forwarding the previous settled state.

---

## 🛠️ Recommendations & Best Practices

- **Do Not Rely on Finally Arguments**: Never declare parameters inside a `.finally()` callback as they will always be `undefined`.
- **Always Return Values**: Ensure every `.then()` block has a clear, explicit return statement to avoid passing accidental `undefined` down the chain.

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - **`.finally()` is a ghost**: It sees no incoming arguments, and its return value is invisible to the next chain links!
  - **`.catch()` is a healer**: It catches errors and heals the promise chain back into a resolved state.

---

## 🔗 Helpful Resources

- [MDN Web Docs - Promise.prototype.finally()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)
- [MDN Web Docs - Promise.prototype.catch()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
- [BFE.dev - Quiz 4](https://bigfrontend.dev/quiz/4-Promise-then-callbacks-II)

---

## 🏷️ Tags

`#Promises` `#PromiseChaining` `#PromiseFinally` `#PromiseCatch` `#Google` `#Meta` `#Apple` `#Asynchronous`
