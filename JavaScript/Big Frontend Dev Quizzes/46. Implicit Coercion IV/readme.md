# 📝 [46. Implicit Coercion IV](https://bigfrontend.dev/quiz/implicit-coersion-2)

## 📌 Problem Overview

This quiz tests object truthiness and the coercion rules used by the loose equality operator (`==`). The array `[0]` is an object, so it is truthy in the `if` condition. The selected comparison is therefore `foo == true`.

```javascript
const foo = [0]
if (foo) {
	console.log(foo == true)
} else {
	console.log(foo == false)
}
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> false
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

The evaluation has two distinct parts: the `if` statement first applies `ToBoolean` to `foo`, and the selected `console.log` then evaluates `foo == true` using the Abstract Equality Comparison algorithm. Arrays are objects and objects are truthy, but loose equality may convert an object to a primitive value before comparing it with a boolean.

### ⚡ Key Spec Rules / Concepts

1. **ToBoolean for Objects**: `ToBoolean` converts every object, including an empty array or an array containing `0`, to `true`; an object's contents do not determine its truthiness.
2. **Abstract Equality Comparison**: When one operand is a boolean, `==` converts that boolean with `ToNumber`. It then compares the resulting number with the other operand.
3. **ToPrimitive for Arrays**: When an array is compared with a primitive, its default primitive conversion uses its string representation. `[0].toString()` produces the primitive string `"0"`.
4. **String-to-Number Conversion**: The abstract equality algorithm converts the string `"0"` to the number `0` before comparing it with the number `1`.

---

### Step-by-Step Execution

#### 1. `const foo = [0]` -> an array object

- **Step A**: The array literal creates an Array object with one element, the number `0`.
- **Step B**: `foo` is initialized with a reference to that array object.
- **Output**: No console output.

#### 2. `if (foo)` -> `true`

- **Step A**: The `if` condition evaluates `foo` and applies `ToBoolean`.
- **Step B**: `foo` is an object. Objects are truthy, regardless of whether an array is empty or contains a falsy value such as `0`.
- **Output**: The `if` branch executes.

#### 3. `foo == true` -> `false`

- **Step A**: The left operand is an object and the right operand is a boolean, so Abstract Equality Comparison converts `true` to the number `1`.
- **Step B**: Because the left operand is still an object and the right operand is a number, the array is converted with `ToPrimitive`.
- **Step C**: The array's default primitive conversion produces the string `"0"`.
- **Step D**: The comparison is now `"0" == 1`. Since one operand is a string and the other is a number, `"0"` is converted to the number `0`.
- **Step E**: The numeric comparison becomes `0 == 1`, which is false.
- **Output**: `false`

#### 4. `console.log(foo == true)` -> prints `false`

- **Step A**: The comparison result from the previous step is passed to `console.log`.
- **Output**: `false`

#### 5. `console.log(foo == false)` -> not executed

- **Step A**: The `else` branch is skipped because `ToBoolean(foo)` returned `true`.
- **Output**: No console output.

---

## 💡 Key Takeaway

* **Object truthiness is independent of contents**: `[0]` is truthy because it is an object, even though its only element is the falsy number `0`.
* **Loose equality can perform several conversions**: `foo == true` becomes `[0]` -> `"0"` -> `0`, while `true` becomes `1`, resulting in `0 == 1` and therefore `false`.

---

## 🛠️ Recommendations & Best Practices

* **Prefer strict equality**: Use `===` when comparing values so JavaScript does not silently apply Abstract Equality coercions.
* **Check collection contents explicitly**: Use a direct condition such as `foo.length > 0` or inspect the relevant element instead of relying on an array's truthiness.

```javascript
const foo = [0]

if (foo.length > 0) {
	console.log(foo[0] === 1)
}
```

---

## 🧠 Revision Tips & Cheat Sheet

### Visual Coercion Path / Logical Flow

> [!WARNING]
> Always wrap node labels containing brackets, parentheses, or spaces in double quotes to avoid Mermaid parsing errors.

```mermaid
graph TD
		A["foo = [0]"] -->|"ToBoolean for if"| B["Object is truthy"]
		B -->|"Select if branch"| C["foo == true"]
		C -->|"ToNumber(true)"| D["1"]
		C -->|"ToPrimitive([0])"| E["0"]
		E -->|"ToNumber(\"0\")"| F["0"]
		D -->|"Compare"| G["0 == 1 -> false"]
		F -->|"Compare"| G
```

### Quick Conversion Table

| Expression | Result | Reason |
|---|---:|---|
| `Boolean([0])` | `true` | Arrays are objects and objects are truthy |
| `String([0])` | `"0"` | Array stringification joins its elements |
| `Number("0")` | `0` | Numeric string conversion |
| `[0] == true` | `false` | `0` is not equal to `1` |

---

## 🔗 Helpful Resources

- [ECMA-262 Specification - ToBoolean](https://tc39.es/ecma262/#sec-toboolean)
- [ECMA-262 Specification - Abstract Equality Comparison](https://tc39.es/ecma262/#sec-islooselyequal)
- [ECMA-262 Specification - ToPrimitive](https://tc39.es/ecma262/#sec-toprimitive)
- [MDN Web Docs - Truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
- [MDN Web Docs - Equality comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)
- [BFE.dev - Quiz 46](https://bigfrontend.dev/quiz/implicit-coersion-2)

---

## 🏷️ Tags

`#ImplicitCoercion` `#AbstractEquality` `#ArrayTruthiness` `#ToPrimitive` `#SpecDeepDive`