## [74. Typed Array length](https://bigfrontend.dev/quiz/Typed-Array-length)

### Approach

#### Evaluation 1: arr1.length
1. const arr1 = new MyArray(10) allocates a raw underlying binary ArrayBuffer of 10 bytes in memory.
2. When console.log(arr1.length) executes, the engine looks for a property named length on the arr1 instance. It finds nothing.
3. It moves up the prototype chain to MyArray.prototype.
4. It encounters your explicit getter: get length() { return 3 }.
5. The function fires and returns 3.

#### Evaluation 2: arr2.length
1. const arr2 = new Uint8Array(10) allocates 10 bytes of memory.
2. When evaluating arr2.length, the engine checks the instance, finds nothing, and traverses to Uint8Array.prototype.
3. It hits the native standard getter provided by the environment, which securely reads the internal [[ArrayLength]] slot.
4. It outputs the true allocated buffer size: 10.