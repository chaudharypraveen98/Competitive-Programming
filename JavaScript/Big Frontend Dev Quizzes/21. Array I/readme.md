# 📝 [21. Array I](https://bigfrontend.dev/quiz/Array-I)

## 📌 Problem Overview

In JavaScript, arrays are objects. This quiz tests your understanding of array length behavior, sparse arrays, iteration using `for...of`, `Array.prototype.map()`, `Array.prototype.forEach()`, `Object.keys()`, `delete`, and truncating arrays using the `length` property.

```javascript
const a = [0]
console.log(a.length)
a[3] = 3
console.log(a.length)
for (let item of a) {
  console.log(item)
}
a.map(item => {console.log(item)})
a.forEach(item => {console.log(item)})
console.log(Object.keys(a))
delete a[3]
console.log(a.length)
a[2] = 2
a.length = 1
console.log(a[0], a[1], a[2])
```

---

## 🚀 Correct Answer

> [!TIP]
> **Output:**
>
> ```text
> 1
> 4
> 0
> undefined
> undefined
> 3
> 0
> 3
> 0
> 3
> ["0","3"]
> 4
> 0 undefined undefined
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

In JavaScript, arrays are exotic objects that automatically synchronize their `length` property with the largest numeric property key. Sparse arrays contain empty slots, which do not have corresponding property keys on the array object. Iterating over sparse arrays behaves differently depending on the iteration method used (e.g., `for...of` vs. `Array.prototype.map`/`forEach`). Truncating an array by setting its `length` property to a smaller value deletes all property keys that represent indices greater than or equal to the new length.

### ⚡ Key Spec Rules / Concepts

1. **Exotic Array Object & `length` Property (ECMAScript §23.1.4)**:
   The `length` property is an integer-valued property of an Array exotic object that is always numerically greater than the name of every configurable property whose name is an array index. When the `length` property is modified to a value `n` less than its current value, any own property of the array whose name is an array index and whose value is greater than or equal to `n` is deleted.

2. **Sparse Arrays and Property Existence**:
   Setting a value at a index larger than the current length (e.g. `a[3] = 3` when length is 1) creates "empty slots". These empty slots are not properties on the array object. This can be verified using `hasOwnProperty`.

3. **`for...of` Iteration (§23.1.5.1 Array Iterator)**:
   A `for...of` loop uses the array's iterator. The iterator evaluates indices sequentially from `0` to `length - 1` by calling `[[Get]]` on each index. If an index is an empty slot, `[[Get]]` returns `undefined`.

4. **`Array.prototype.map` (§23.1.3.16) and `forEach` (§23.1.3.10)**:
   Both `map` and `forEach` spec steps include checking if the property exists on the array using `HasProperty(O, Pk)`. If the property does not exist (as in empty slots), the callback function is not invoked for that index.

5. **`Object.keys` (§20.1.2.16)**:
   `Object.keys` returns an array of strings representing the enumerable own property keys of the object. Empty slots do not exist as own properties, so they are not included in the returned array.

6. **`delete` Operator (§13.5.1)**:
   The `delete` operator removes a property from an object. For arrays, deleting an index property removes the key-value pair and leaves an empty slot, but does not update the `length` property of the array.

---

### Step-by-Step Execution

#### 1. `const a = [0]` -> `a` initialized
- **Step A**: Creates an array containing a single element `0` at index `0`.
- **Output**: `a` is `[0]`, `a.length` is `1`.

#### 2. `console.log(a.length)` -> `1`
- **Step A**: Accesses the `length` property of `a`, which is `1`.
- **Output**: `1`

#### 3. `a[3] = 3` -> `a` becomes sparse
- **Step A**: Assigns `3` to index `3`.
- **Step B**: Since the index `3` is greater than or equal to the current length `1`, the engine automatically updates the `length` property to `3 + 1 = 4`.
- **Step C**: Indices `1` and `2` remain unassigned (empty slots).
- **Output**: `a` is `[0, <2 empty items>, 3]`, `a.length` is `4`.

#### 4. `console.log(a.length)` -> `4`
- **Step A**: Accesses the `length` property of `a`, which is now `4`.
- **Output**: `4`

#### 5. `for (let item of a) { console.log(item) }` -> logs `0`, `undefined`, `undefined`, `3`
- **Step A**: The `for...of` loop uses the array iterator which visits indices `0`, `1`, `2`, and `3`.
- **Step B**: At index `0`, the value is `0`.
- **Step C**: At index `1` and `2`, since these are empty slots, the iterator returns `undefined`.
- **Step D**: At index `3`, the value is `3`.
- **Output**:
  ```text
  0
  undefined
  undefined
  3
  ```

#### 6. `a.map(item => {console.log(item)})` -> logs `0`, `3`
- **Step A**: `Array.prototype.map` iterates through the array from indices `0` to `3`.
- **Step B**: For each index `i`, it checks `HasProperty(a, ToString(i))`.
- **Step C**: `HasProperty` is `true` for `0` and `3`, but `false` for `1` and `2`.
- **Step D**: The callback is only executed for indices `0` and `3`.
- **Output**:
  ```text
  0
  3
  ```

#### 7. `a.forEach(item => {console.log(item)})` -> logs `0`, `3`
- **Step A**: `Array.prototype.forEach` similarly checks `HasProperty(a, ToString(i))` for indices `0` to `3`.
- **Step B**: It calls the callback only for indices `0` and `3` where the property exists.
- **Output**:
  ```text
  0
  3
  ```

#### 8. `console.log(Object.keys(a))` -> `["0", "3"]`
- **Step A**: `Object.keys` collects all own enumerable property keys of `a`.
- **Step B**: The only own keys present on the object `a` are `"0"` and `"3"`.
- **Output**: `["0", "3"]`

#### 9. `delete a[3]` -> deletes key `"3"`
- **Step A**: The `delete` operator removes the own property `"3"` from `a`.
- **Step B**: The `length` property of the array remains unchanged at `4`.
- **Output**: `a` is `[0, <3 empty items>]`, `a.length` is `4`.

#### 10. `console.log(a.length)` -> `4`
- **Step A**: Accesses the `length` property of `a`.
- **Output**: `4`

#### 11. `a[2] = 2` -> `a` becomes `[0, <1 empty item>, 2, <1 empty item>]`
- **Step A**: Assigns `2` to index `2`.
- **Output**: `a` is `[0, <1 empty item>, 2, <1 empty item>]`, `a.length` is `4`.

#### 12. `a.length = 1` -> truncates array `a`
- **Step A**: Setting `length` to `1` invokes `[[DefineOwnProperty]]` on the array object's `length` property.
- **Step B**: The engine deletes all own properties of `a` whose property names are array indices greater than or equal to `1`.
- **Step C**: This deletes indices `2` and the empty slots.
- **Output**: `a` is truncated to `[0]`.

#### 13. `console.log(a[0], a[1], a[2])` -> `0 undefined undefined`
- **Step A**: Accesses index `0`, which has the value `0`.
- **Step B**: Accesses indices `1` and `2`, which no longer exist on the object, returning `undefined` for both.
- **Output**: `0 undefined undefined`

---

## 💡 Key Takeaway

* **Sparse Arrays Iteration Differences**: Built-in iteration methods (`map`, `forEach`, `filter`, `every`, `some`) skip empty slots using `HasProperty` checks, whereas `for...of` loops, spread operators, and `Array.from()` treat empty slots as `undefined`.
* **Array Length Truncation**: Mutating an array's `length` property to a smaller value is a destructive operation that permanently deletes all elements at indices greater than or equal to the new length.
* **`delete` doesn't affect `length`**: Deleting an element using the `delete` operator only removes the property and leaves an empty slot; it does not change the array's `length`.

---

## 🛠️ Recommendations & Best Practices

* **Avoid Sparse Arrays**: Sparse arrays lead to unpredictable behavior and performance de-optimizations in JavaScript engines. Instead of leaving empty slots, initialize array elements with a default value like `null` or `undefined`.
* **Avoid Using `delete` on Array Indices**: Use `Array.prototype.splice` or `filter` to remove elements from an array rather than `delete`, which leaves holes (`empty` slots).
* **Use `splice` for Truncation**: Although setting `length` works for truncating, `splice` is more explicit and aligns with standard array mutation practices.

```javascript
// Good practice: Initializing arrays with default values
const cleanArray = Array.from({ length: 4 }, () => null); // [null, null, null, null]

// Good practice: Removing elements without leaving empty slots
const fruits = ['apple', 'banana', 'orange'];
fruits.splice(1, 1); // removes 'banana', fruits becomes ['apple', 'orange']

// Good practice: Truncating an array explicitly
fruits.length = 1; // Safely truncates to ['apple']
```

---

## 🧠 Revision Tips & Cheat Sheet

### Visual Coercion Path / Logical Flow

```mermaid
graph TD
    A["Array a = [0]"] -->|a[3] = 3| B["Sparse Array: [0, empty, empty, 3] (length = 4)"]
    B -->|for...of| C["Iterates all indices -> yields 0, undefined, undefined, 3"]
    B -->|map / forEach| D["Checks HasProperty -> invokes callback only for 0, 3"]
    B -->|delete a[3]| E["Deletes index 3 -> [0, empty, empty, empty] (length = 4)"]
    E -->|a.length = 1| F["Truncates indices >= 1 -> [0] (length = 1)"]
```

---

## 🔗 Helpful Resources

- [ECMA-262 Specification - Array Exotic Objects](https://tc39.es/ecma262/#sec-array-exotic-objects)
- [MDN Web Docs - Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [BFE.dev - Quiz 21: Array I](https://bigfrontend.dev/quiz/Array-I)

---

## 🏷️ Tags

`#JavaScript` `#Array` `#SparseArray` `#Iteration` `#SpecDeepDive`