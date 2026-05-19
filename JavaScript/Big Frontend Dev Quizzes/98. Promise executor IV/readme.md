## [98. Promise executor IV](https://bigfrontend.dev/quiz/Promise-executor-IV)

### Approach
1. Here, for promise the executor function is executed immediately by the Promise implementation. Since promise2 is a rejected promise, the 2nd callback to then gets executed and 2 is logged to the console. However, since no value is returned explicitly, the fulfilled value for promise2 remains undefined
2. promise then ultimately resolves with the value returned from promise2 i.e. undefined which gets logged to the console when promise.then gets invoked

### The Two-Argument Structure of .then()
The .then() method naturally accepts up to two separate callback functions as arguments:
1. onFulfilled (First Argument): Triggered if the preceding promise resolves successfully.
2. onRejected (Second Argument): Triggered if the preceding promise fails or rejects.

```
// What your code actually looks like:
Promise.reject('error').then(
  () => { console.log(1) }, // Position 1: Bypassed on error
  () => { console.log(2) }  // Position 2: Invoked on error
);
```

### Why .catch() is Syntactic Sugar
Under the hood of the JavaScript engine, calling .catch(onRejected) is strictly equivalent to calling .then(null, onRejected).

If you were to rewrite the code using a separate .catch() block instead of the second argument, the internal routing would handle it similarly, but the structural chain would look like this:

```
// Syntactically different, architecturally identical routing:
Promise.reject('error')
  .then(() => {
    console.log(1);
  })
  .catch(() => {
    console.log(2); // Still catches the rejection and implicitly returns undefined
  });
```