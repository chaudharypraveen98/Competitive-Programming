# 📝 [6. Arrow Function](https://bigfrontend.dev/quiz/6-Arrow-Function)

## 📌 Problem Overview

What is logged to the console when executing each method of `obj` below?

```javascript
const obj = {
  dev: 'bfe',
  a: function() {
    return this.dev
  }, 
  b() {
    return this.dev
  },
  c: () => {
    return this.dev
  },
  d: function() {
    return (() => {
      return this.dev
    })()
  },
  e: function() {
    return this.b()
  },
  f: function() {
    return this.b
  },
  g: function() {
    return this.c()
  },
  h: function() {
    return this.c
  },
  i: function() {
    return () => {
      return this.dev
    }
  }
}

console.log(obj.a())
console.log(obj.b())
console.log(obj.c()) // (Note: commented in raw code but analyzed below)
console.log(obj.d())
console.log(obj.e())
console.log(obj.f()())
console.log(obj.g())
console.log(obj.h()())
console.log(obj.i()())
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> "bfe"
> "bfe"
> undefined
> "bfe"
> "bfe"
> undefined
> undefined
> undefined
> "bfe"
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

The binding of the **`this`** keyword depends entirely on **how** a function is declared (Arrow vs. Normal) and **where/how** it is invoked.

### ⚡ Arrow Functions vs. Normal Functions

1. **Normal Functions**: Have a *dynamic `this`*. The value of `this` is determined at execution time based on *how* they are called (e.g. `obj.a()` binds `this` to `obj`).
2. **Arrow Functions**: Have a *lexical `this`*. They do **not** have their own `this` binding. Instead, `this` is resolved by looking up the scope chain to the enclosing lexical context. Furthermore, their `this` is **immutable** and cannot be changed by `.bind()`, `.call()`, or `.apply()`.

---

### Step-by-Step Method Breakdown

#### 1. `obj.a()` -> `"bfe"`

- `a` is a normal function.
- It is invoked as a method of `obj` (`obj.a()`), so `this` points to `obj`.
- `this.dev` resolves to `obj.dev` which is `"bfe"`.

#### 2. `obj.b()` -> `"bfe"`

- `b` is shorthand syntax for a normal method function.
- Invoked as a method of `obj` (`obj.b()`), so `this` points to `obj`.
- `this.dev` resolves to `"bfe"`.

#### 3. `obj.c()` -> `undefined`

- `c` is an **arrow function** defined directly inside the object literal block.
- *Note:* Curly braces `{}` for object literals do **not** create a new lexical block scope. The lexical surrounding scope of `c` is the global execution context (the file's top level, which maps `this` to the `window` or global object).
- Since `this` points to the global object/`window` where `dev` is not defined, it returns `undefined`.

#### 4. `obj.d()` -> `"bfe"`

- `d` is a normal function. Calling `obj.d()` binds `this` of `d` to `obj`.
- Inside `d`, an **arrow function** is defined and immediately executed (IIFE).
- The arrow function resolves `this` lexically. The surrounding lexical scope is `d`'s function block, where `this` is bound to `obj`.
- Thus, the arrow function successfully reads `this.dev` as `"bfe"`.

#### 5. `obj.e()` -> `"bfe"`

- `e` is a normal function, invoked as `obj.e()`, so `this` inside `e` is bound to `obj`.
- Inside `e`, it returns `this.b()`. Since `this` is `obj`, this is equivalent to invoking `obj.b()`, which evaluates to `"bfe"`.

#### 6. `obj.f()()` -> `undefined` (or throws `TypeError` in strict mode)

- `f` is a normal function, invoked as `obj.f()`, which binds `this` to `obj`.
- It returns the function `this.b` (which is a reference to method `b`) **without invoking it**.
- The returned function is then executed immediately as a **standalone function call**: `obj.f()()`.
- **Dynamic Scoping rule**: A standalone invocation of a normal function loses its method context:
  - In **non-strict mode**: `this` defaults to the global object (`window` or `global`). Since `global.dev` is not defined, it returns `undefined`.
  - In **strict mode** (e.g. inside ES Modules or `"use strict"`): `this` is explicitly set to `undefined`. Attempting to read `this.dev` throws a `TypeError: Cannot read properties of undefined (reading 'dev')`.

#### 7. `obj.g()` -> `undefined`

- `g` is a normal function, so `this` inside `g` is `obj`.
- Inside, it executes `this.c()`. Since `this` is `obj`, it calls `obj.c()`.
- Even though `c` is invoked on `obj` context, `c` is an **arrow function**. Its lexical `this` is immutably set to the global object/`window` at definition time.
- Therefore, `obj.c()` still resolves `this` to the global object, returning `undefined`.

#### 8. `obj.h()()` -> `undefined` (or throws `TypeError` in strict mode)

- `h` returns a reference to the arrow function `this.c` (equivalent to `obj.c`).
- It is then invoked as `obj.h()()`.
- Since it is an arrow function, its `this` context remains bound to the global object/`window` regardless of how or where it is called.
- In both strict and non-strict mode, it successfully accesses the global object as `this` (since arrow functions resolve `this` lexically at creation time when `this` pointed to the global scope).
- Thus, it evaluates to `global.dev` which is `undefined`. It does **not** throw in strict mode because `this` inside the arrow function is not bound to `undefined` at execution, but rather lexically captured as the global context during creation.

#### 9. `obj.i()()` -> `"bfe"`

- `i` is a normal function. `obj.i()` binds `this` inside `i` to `obj`.
- It returns an **arrow function** `() => { return this.dev }`.
- Because this arrow function was *created* inside `i`'s execution scope, its lexical environment captures `i`'s current `this` (which is `obj`).
- When invoked as `obj.i()()`, the returned arrow function retains this lexical enclosure (closure over `this = obj`), correctly returning `"bfe"`.

---

## 💡 Key Takeaway

* **Normal methods capture their caller's context** (`obj.method()`), but standalone calls (`func()`) lose that context.
- **Arrow functions bind `this` lexically at creation time**, making them completely immune to how or where they are invoked later.

---

## 🛠️ Recommendations & Best Practices

* **Avoid Arrow Functions for Object Methods**: Never use arrow functions to define direct object methods if you need access to other object properties via `this`.
- **Use Arrow Functions inside Callbacks**: Use arrow functions inside timers (`setTimeout`) or array helpers (`.map`, `.filter`) inside methods to seamlessly preserve the outer class or object's `this` context without calling `.bind(this)`.

---

## 🧠 Revision Tips & Cheat Sheet

- **Memory Hook**:
  - **Dynamic vs. Lexical**: Normal functions care *who* calls them. Arrow functions only care *where* they were born.
  - Arrow functions have **no `arguments` object**, **no `prototype`**, and **cannot be used with `new` (non-constructible)**.

---

## 🔗 Helpful Resources

- [MDN Web Docs - Arrow Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [MDN Web Docs - Understanding 'this'](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
- [JavaScript.info - Arrow functions revisited](https://javascript.info/arrow-functions)
- [BFE.dev - Quiz 6](https://bigfrontend.dev/quiz/6-Arrow-Function)

---

## 🏷️ Tags

`#ArrowFunctions` `#ThisKeyword` `#LexicalScope` `#DynamicBinding` `#Google` `#Meta` `#Amazon` `#Closures`
