# 📝 [2. Promise executor](https://bigfrontend.dev/quiz/2-promise-executor)

## 📌 Problem Overview

What value is logged to the console when the following script runs?

```javascript
new Promise((resolve, reject) => {
  resolve(1)
  resolve(2)
  reject('error')
}).then((value) => {
  console.log(value)
}, (error) => {
  console.log('error')
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
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

To understand why only `1` is logged, we must review the **State Machine** model of JavaScript Promises.

### Step-by-Step Execution

1. **State Machine Initialization**:
   - When `new Promise((resolve, reject) => { ... })` is called, a promise object is initialized in the **`pending`** state.
   - The executor function begins executing immediately and synchronously.

2. **First `resolve(1)` Call**:
   - The executor invokes `resolve(1)`.
   - This transitions the promise state from **`pending`** to **`fulfilled`** with the fulfillment value `1`.
   - The promise's fate is now sealed.

3. **Subsequent Calls (`resolve(2)` and `reject('error')`)**:
   - Next, `resolve(2)` is called. The engine checks the promise's internal state. Since the state is already **`fulfilled`** (no longer `pending`), this call is silently ignored.
   - Then, `reject('error')` is called. Similarly, because the promise is already **`fulfilled`**, the rejection call is ignored.
   - The ECMAScript specification ensures that once a promise transitions out of `pending`, its state and settled value/reason become **immutable**.

4. **Promise Reaction Execution**:
   - The Call Stack empties, and the Event Loop processes the Microtask Queue.
   - The promise reaction `.then(onFulfilled, onRejected)` was scheduled.
   - Since the promise resolved to `1`, the `onFulfilled` handler is executed: `(value) => { console.log(value) }`.
   - **Output:** `1`

---

## 💡 Key Takeaway

* **Promise Immutability (Single-Settlement)**: A Promise is a one-way state machine. It can only transition from `pending` to either `fulfilled` or `rejected` **once**. Any subsequent attempts to resolve or reject the promise are completely ignored.

---

## 🛠️ Recommendations & Best Practices

* **Avoid Post-Resolve Statements**: Do not write logic after `resolve()` or `reject()` calls inside executors. If you want execution to stop immediately upon resolution, explicitly use the `return` statement:

  ```javascript
  new Promise((resolve, reject) => {
    return resolve(1); // Explicitly exits the executor
    resolve(2); // Unreachable
  });
  ```

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - *Think of a Promise as a signed contract.* Once signed (resolved/rejected), you cannot modify its terms (re-resolve or reject it).

---

## 🔗 Helpful Resources

- [MDN Web Docs - Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript.info - Promise basics](https://javascript.info/promise-basics)
- [ECMA-262 Specification - Promise Objects](https://tc39.es/ecma262/#sec-promise-objects)
- [BFE.dev - Quiz 2](https://bigfrontend.dev/quiz/2-promise-executor)

---

## 🏷️ Tags

`#Promises` `#PromiseStates` `#Google` `#Meta` `#Uber` `#StateTransition` `#Asynchronous`
