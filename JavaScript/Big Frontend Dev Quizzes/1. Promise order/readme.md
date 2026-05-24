# 📝 [1. Promise order](https://bigfrontend.dev/quiz/1-promise-order)

## 📌 Problem Overview

What is the exact output order when running the following script?

```javascript
console.log(1)
const promise = new Promise((resolve) => {
    console.log(2);
    resolve();
    console.log(3);
});

console.log(4)

promise
    .then(() => {
        console.log(5);
    })
    .then(() => {
        console.log(6);
    });

console.log(7)

setTimeout(() => {
  console.log(8)
}, 10)

setTimeout(() => {
  console.log(9)
}, 0)
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
> 3
> 4
> 7
> 5
> 6
> 9
> 8
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

To understand the exact execution order, we must trace how the JavaScript Engine (V8/SpiderMonkey) coordinates the **Call Stack**, **Microtask Queue**, and **Macrotask (Task) Queue** inside the **Event Loop**.

### Step-by-Step Execution

1. **Synchronous Execution begins**:
   - `console.log(1)` is executed synchronously and pushed onto the Call Stack.
     - **Output:** `1`

2. **Promise Constructor Execution**:
   - The executor function passed to `new Promise((resolve) => { ... })` is executed **immediately and synchronously**.
   - `console.log(2)` runs synchronously.
     - **Output:** `2`
   - `resolve()` is called. This transitions the promise state from `pending` to `fulfilled`. However, any attached `.then()` callbacks are asynchronous and are scheduled for later execution (pushed to the Microtask Queue).
   - `console.log(3)` runs synchronously.
     - **Output:** `3`

3. **Synchronous Execution continues**:
   - `console.log(4)` runs synchronously.
     - **Output:** `4`

4. **Promise Reactions (`.then`) Scheduling**:
   - `promise.then(() => { console.log(5); })` is evaluated. Since the promise is already resolved, this callback is queued in the **Microtask Queue** (Microtask #1).
   - *Note:* The second `.then(() => { console.log(6); })` is chained. It is **not** queued yet because the promise returned by the first `.then()` is still pending (it will resolve only after Microtask #1 executes).

5. **Synchronous Execution continues**:
   - `console.log(7)` runs synchronously.
     - **Output:** `7`

6. **Timer Scheduling**:
   - `setTimeout(() => { console.log(8) }, 10)` registers a timer with a `10ms` delay. Once the timer expires, the callback is pushed to the **Macrotask Queue** (Macrotask #1).
   - `setTimeout(() => { console.log(9) }, 0)` registers a timer with a `0ms` (minimum clamp ~1-4ms in browsers/Node). Its callback is queued in the **Macrotask Queue** (Macrotask #2) almost immediately.

7. **Call Stack Empties -> Microtask Phase**:
   - The synchronous script completes. The Call Stack is empty.
   - The Event Loop immediately checks and drains the **Microtask Queue** completely before proceeding to any macrotasks.
   - **Microtask #1** executes: `console.log(5)` runs.
     - **Output:** `5`
     - This completes the first `.then()`, resolving its implicit promise. The second chained `.then(() => { console.log(6); })` is now scheduled and queued in the **Microtask Queue** (Microtask #2).
   - **Microtask #2** executes immediately (since the Event Loop loops until the microtask queue is entirely dry): `console.log(6)` runs.
     - **Output:** `6`

8. **Macrotask Phase**:
   - The Microtask Queue is now empty. The Event Loop processes the **Macrotask Queue**.
   - **Macrotask #2** (the 0ms timer callback) executes first because its delay expired first. `console.log(9)` runs.
     - **Output:** `9`
   - **Macrotask #1** (the 10ms timer callback) executes once its 10ms delay has elapsed and the event loop polls again. `console.log(8)` runs.
     - **Output:** `8`

---

## 💡 Key Takeaway

1. **Promise Executors are Synchronous**: The function passed to `new Promise` runs immediately during the execution of the constructor.
2. **Microtasks > Macrotasks**: Microtasks (Promise callbacks) are prioritized and fully drained before the Event Loop executes the next Macrotask (`setTimeout`, `setInterval`).

---

## 🛠️ Recommendations & Best Practices

- **Avoid Mixing Execution Models**: Avoid mixing heavy synchronous computations with Promises or timers in the same block to prevent freezing the main thread.
- **Microtask starvation**: Be careful not to create recursive promise chains (e.g. infinite microtasks) because they will starve the Macrotask Queue and completely freeze browser rendering or timer processing.

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - **Stack** (Synchronous) -> **Microtask** (Promise `.then`) -> **Macrotask** (`setTimeout`).
  - *Think:* Promises are "VIP guests" who get served as soon as the stack is clear, whereas timers are "regular line guests" who wait for the next event loop tick.

---

## 🔗 Helpful Resources

- [MDN Web Docs - Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
- [MDN Web Docs - In Depth Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)
- [JavaScript.info - Microtasks](https://javascript.info/microtasks)
- [BFE.dev - Quiz 1](https://bigfrontend.dev/quiz/1-promise-order)

---

## 🏷️ Tags

`#EventLoop` `#Promises` `#Google` `#Meta` `#Netflix` `#Microtasks` `#Asynchronous`
