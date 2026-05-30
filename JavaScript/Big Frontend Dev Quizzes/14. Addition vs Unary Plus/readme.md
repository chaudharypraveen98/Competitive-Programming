# 📝 [14. Addition vs Unary Plus](https://bigfrontend.dev/quiz/Addition-vs-Unary-Plus)

## 📌 Problem Overview

This quiz tests your understanding of JavaScript's addition operators, specifically the difference between the **binary addition operator** (`+`) and the **unary plus operator** (`+`). It deep dives into operator precedence, type coercion, and how different primitive values (booleans, `null`, `undefined`, and strings) are coerced under these operations.

```javascript
console.log(1 + 2)
console.log(1 + + 2)
console.log(1 + + + 2)
console.log(1 + '2')
console.log(1 + + '2')
console.log('1' + 2)
console.log('1' + + 2)
console.log(1 + true)
console.log(1 + + true)
console.log('1' + true)
console.log('1' + + true)
console.log(1 + null)
console.log(1 + + null)
console.log('1' + null)
console.log('1' + + null)
console.log(1 + undefined)
console.log(1 + + undefined)
console.log('1' + undefined)
console.log('1' + + undefined)
console.log('1' + + + undefined)
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> 3
> 3
> 3
> "12"
> 3
> "12"
> "12"
> 2
> 2
> "1true"
> "11"
> 1
> 1
> "1null"
> "10"
> NaN
> NaN
> "1undefined"
> "1NaN"
> "1NaN"
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

The quiz explores the dual nature of JavaScript's addition operations: the **unary plus** and the **binary addition** operators.
Unary plus always coerces its operand to a number. Binary addition performs string concatenation if either operand is a string; otherwise, it performs numeric addition by converting non-number operands to numbers.

### ⚡ Key Spec Rules / Concepts

1. **Unary Plus Operator (`+`) (ECMA-262, Section 13.5.3)**:
   - Performs the `ToNumber` abstract operation on its operand, forcing it to a numeric value.
   - It has higher precedence than the binary addition operator.
2. **Binary Addition Operator (`+`) (ECMA-262, Section 13.8.1)**:
   - First, both operands are converted to primitive values using `ToPrimitive` (with no preferred type hint).
   - If either primitive value is a **String**, it converts the other to a String using `ToString` and returns the concatenated result.
   - Otherwise, it converts both operands to Numbers using `ToNumber` and performs standard mathematical addition.
3. **ToNumber Conversions (ECMA-262, Section 7.1.3)**:
   - `ToNumber(true)` yields `1`
   - `ToNumber(false)` yields `0`
   - `ToNumber(null)` yields `0`
   - `ToNumber(undefined)` yields `NaN`
   - `ToNumber(string)` yields the parsed number, or `NaN` if the string cannot be parsed as a valid numeric literal.

---

### Step-by-Step Execution

For each expression/statement executed in the quiz, trace the evaluation step-by-step:

#### 1. `1 + 2` -> `3`

- **Step A**: Both operands `1` and `2` are numbers.
- **Step B**: Perform numeric addition: `1 + 2`.
- **Output**: `3`

#### 2. `1 + + 2` -> `3`

- **Step A**: Evaluate the unary plus `+ 2` on the right first due to higher precedence. `ToNumber(2)` evaluates to `2`.
- **Step B**: Evaluate binary addition: `1 + 2`.
- **Output**: `3`

#### 3. `1 + + + 2` -> `3`

- **Step A**: Evaluate the unary pluses right-to-left: `+ (+ 2)`.
- **Step B**: `+ 2` is `2`, and the second unary plus `+ 2` is also `2`.
- **Step C**: Evaluate binary addition: `1 + 2`.
- **Output**: `3`

#### 4. `1 + '2'` -> `"12"`

- **Step A**: Evaluate binary addition. Since the right operand `'2'` is a string, trigger string concatenation.
- **Step B**: Convert `1` to a string via `ToString(1)`, yielding `"1"`.
- **Step C**: Concatenate `"1"` and `"2"`.
- **Output**: `"12"`

#### 5. `1 + + '2'` -> `3`

- **Step A**: Evaluate unary plus `+ '2'` first. `ToNumber("2")` coerces the string to the number `2`.
- **Step B**: Evaluate binary addition: `1 + 2`.
- **Output**: `3`

#### 6. `'1' + 2` -> `"12"`

- **Step A**: The left operand `'1'` is a string, triggering string concatenation.
- **Step B**: Convert `2` to a string via `ToString(2)`, yielding `"2"`.
- **Step C**: Concatenate `"1"` and `"2"`.
- **Output**: `"12"`

#### 7. `'1' + + 2` -> `"12"`

- **Step A**: Evaluate unary plus `+ 2`, yielding the number `2`.
- **Step B**: Evaluate binary addition `'1' + 2`. Since `'1'` is a string, coerce `2` to `"2"`.
- **Step C**: Concatenate `"1"` and `"2"`.
- **Output**: `"12"`

#### 8. `1 + true` -> `2`

- **Step A**: Neither operand is a string. Apply `ToNumber(true)` to the right operand, yielding `1`.
- **Step B**: Perform numeric addition: `1 + 1`.
- **Output**: `2`

#### 9. `1 + + true` -> `2`

- **Step A**: Evaluate unary plus `+ true`. `ToNumber(true)` coerces `true` to `1`.
- **Step B**: Perform numeric addition: `1 + 1`.
- **Output**: `2`

#### 10. `'1' + true` -> `"1true"`

- **Step A**: The left operand `'1'` is a string, triggering string concatenation.
- **Step B**: Convert `true` to a string via `ToString(true)`, yielding `"true"`.
- **Step C**: Concatenate `"1"` and `"true"`.
- **Output**: `"1true"`

#### 11. `'1' + + true` -> `"11"`

- **Step A**: Evaluate unary plus `+ true` to the number `1` via `ToNumber(true)`.
- **Step B**: Evaluate `'1' + 1`. Since `'1'` is a string, convert `1` to `"1"`.
- **Step C**: Concatenate `"1"` and `"1"`.
- **Output**: `"11"`

#### 12. `1 + null` -> `1`

- **Step A**: Neither operand is a string. Coerce `null` to a number via `ToNumber(null)`, yielding `0`.
- **Step B**: Perform numeric addition: `1 + 0`.
- **Output**: `1`

#### 13. `1 + + null` -> `1`

- **Step A**: Evaluate unary plus `+ null` to the number `0` via `ToNumber(null)`.
- **Step B**: Perform numeric addition: `1 + 0`.
- **Output**: `1`

#### 14. `'1' + null` -> `"1null"`

- **Step A**: The left operand is a string. Coerce `null` to a string via `ToString(null)`, yielding `"null"`.
- **Step B**: Concatenate `"1"` and `"null"`.
- **Output**: `"1null"`

#### 15. `'1' + + null` -> `"10"`

- **Step A**: Evaluate unary plus `+ null` to the number `0`.
- **Step B**: Evaluate `'1' + 0`. Coerce `0` to `"0"` and concatenate.
- **Output**: `"10"`

#### 16. `1 + undefined` -> `NaN`

- **Step A**: Neither operand is a string. Coerce `undefined` to a number via `ToNumber(undefined)`, yielding `NaN`.
- **Step B**: Perform numeric addition: `1 + NaN`. Any numeric operation with `NaN` yields `NaN`.
- **Output**: `NaN`

#### 17. `1 + + undefined` -> `NaN`

- **Step A**: Evaluate unary plus `+ undefined` to `NaN` via `ToNumber(undefined)`.
- **Step B**: Perform numeric addition: `1 + NaN`, which yields `NaN`.
- **Output**: `NaN`

#### 18. `'1' + undefined` -> `"1undefined"`

- **Step A**: The left operand is a string. Coerce `undefined` to a string via `ToString(undefined)`, yielding `"undefined"`.
- **Step B**: Concatenate `"1"` and `"undefined"`.
- **Output**: `"1undefined"`

#### 19. `'1' + + undefined` -> `"1NaN"`

- **Step A**: Evaluate unary plus `+ undefined` to `NaN`.
- **Step B**: Evaluate `'1' + NaN`. Since `'1'` is a string, coerce `NaN` to `"NaN"` and concatenate.
- **Output**: `"1NaN"`

#### 20. `'1' + + + undefined` -> `"1NaN"`

- **Step A**: Evaluate unary pluses right-to-left: `+ (+ undefined)` yields `+ NaN` which is `NaN`.
- **Step B**: Evaluate `'1' + NaN`. Coerce `NaN` to `"NaN"` and concatenate.
- **Output**: `"1NaN"`

---

## 💡 Key Takeaway

- **Unary Plus Precedence**: Unary plus (`+`) is executed *before* binary addition (`+`) because unary operators have higher precedence. It acts as an immediate type-coercion mechanism to numbers.
- **Dual Nature of Binary Add**: The binary addition operator prefers string concatenation if *either* operand is a string. If not, it falls back to numeric addition by converting other types to numbers.
- **Special Type Rules**: Remember that `ToNumber(null)` evaluates to `0`, while `ToNumber(undefined)` evaluates to `NaN`.

---

## 🛠️ Recommendations & Best Practices

- **Use Explicit Conversion**: Relying on implicit coercion (especially unary plus or binary plus) can be confusing and error-prone. Always perform explicit type conversions for clarity.
- **Prefer Template Literals**: For string interpolation or concatenation, use template literals instead of the binary plus operator.

```javascript
// Avoid:
const val = 1 + + '2'; // Implicitly gets 3
const label = 'Value: ' + val;

// Recommended:
const val = 1 + Number('2'); // Explicit conversion
const label = `Value: ${val}`; // Template literal
```

---

## 🧠 Revision Tips & Cheat Sheet

### Visual Coercion Path / Logical Flow

> [!WARNING]
> Always wrap node labels containing brackets, parentheses, or spaces in double quotes to avoid Mermaid parsing errors (e.g. use `A["[] == false"]` instead of `A[[] == false]`).

```mermaid
graph TD
    subgraph "Example A: 1 + + '2'"
        A["1 + + '2'"] -->|Evaluate Unary Plus| B["1 + ToNumber('2')"]
        B -->|ToNumber('2') yields 2| C["1 + 2"]
        C -->|Both operands are numbers| D["3"]
    end
    
    subgraph "Example B: '1' + + true"
        E["'1' + + true"] -->|Evaluate Unary Plus| F["'1' + ToNumber(true)"]
        F -->|ToNumber(true) yields 1| G["'1' + 1"]
        G -->|One operand is string| H["'1' + ToString(1)"]
        H -->|ToString(1) yields '1'| I["'1' + '1'"]
        I -->|String Concatenation| J["'11'"]
    end
```

---

## 🔗 Helpful Resources

- [ECMA-262 Specification - Unary Plus Operator](https://tc39.es/ecma262/#sec-unary-plus-operator)
- [ECMA-262 Specification - The Addition Operator](https://tc39.es/ecma262/#sec-addition-operator-lhsobject-rhsobject)
- [MDN Web Docs - Unary plus (+)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
- [MDN Web Docs - Addition (+)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
- [BFE.dev - Quiz 14](https://bigfrontend.dev/quiz/Addition-vs-Unary-Plus)

---

## 🏷️ Tags

`#JavaScript` `#TypeCoercion` `#UnaryPlus` `#BinaryAddition` `#SpecDeepDive`
