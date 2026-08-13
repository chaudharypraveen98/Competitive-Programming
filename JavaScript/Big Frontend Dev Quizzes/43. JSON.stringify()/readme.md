# 📝 [43. JSON.stringify()](https://bigfrontend.dev/quiz/json-stringify)

## 📌 Problem Overview

This quiz tests how `JSON.stringify` serializes arrays and objects containing special numeric and undefined values (e.g. `NaN`, `Infinity`, `undefined`, `null`) and how it treats string and boolean elements.

```javascript
console.log(JSON.stringify(['false', false]))
console.log(JSON.stringify([NaN, null, Infinity, undefined]))
console.log(JSON.stringify({a: null, b: NaN, c: undefined}))
```

---

## 🚀 Correct Answer
>
> [!TIP]
> **Output:**
>
> ```text
> "[\"false\",false]"
> "[null,null,null,null]"
> "{\"a\":null,\"b\":null}"
> ```

---

## 🔍 Detailed Explanation & Spec-Accurate Trace

`JSON.stringify` follows the ECMAScript specification's algorithm for converting JavaScript values to JSON text. Key behaviors relevant to this quiz:

### ⚡ Key Spec Rules / Concepts

1. **`JSON.stringify` Algorithm**: The specification defines how each value type is converted to JSON text, including special-case handling for `undefined`, functions, `Symbol`, `NaN`, and `Infinity`.
2. **Numbers Serialization**: `NaN` and `Infinity` (and `-Infinity`) are serialized as `null` in JSON output.
3. **`undefined` Handling**: When encountered in arrays, `undefined` becomes `null`; when encountered as an object property value, the property is omitted entirely.
4. **Strings & Booleans**: Strings and booleans are serialized to their JSON equivalents (`"..."` and `true`/`false`).
5. **Object Property Enumeration Order**: Own enumerable string-keyed properties are processed in insertion order for serialization.

---

### Step-by-Step Execution

#### 1. `JSON.stringify(['false', false])` -> `"[\"false\",false]"`

- **Step A**: `JSON.stringify` iterates array elements in order.
- **Step B**: Element 0: the string `'false'` is serialized to the JSON string `"false"`.
- **Step C**: Element 1: the boolean `false` is serialized to the JSON literal `false`.
- **Output**: The array becomes the JSON text `["false",false]`, returned as a JavaScript string (shown here with surrounding quotes).

#### 2. `JSON.stringify([NaN, null, Infinity, undefined])` -> `"[null,null,null,null]"`

- **Step A**: Process each array element in sequence.
- **Step B**: `NaN` -> per spec becomes `null` when serializing numbers that are not finite.
- **Step C**: `null` -> remains `null` in JSON.
- **Step D**: `Infinity` -> becomes `null` (non-finite number rule).
- **Step E**: `undefined` in an array slot -> becomes `null` (arrays represent missing/undefined as `null` in JSON text).
- **Output**: All four positions produce `null`, giving `[null,null,null,null]` as the JSON text.

#### 3. `JSON.stringify({a: null, b: NaN, c: undefined})` -> `"{\"a\":null,\"b\":null}"

- **Step A**: Serialize own enumerable string-keyed properties in insertion order: `a`, `b`, `c`.
- **Step B**: Property `a` value `null` -> serialized as `null` and included as `"a":null`.
- **Step C**: Property `b` value `NaN` -> non-finite number serialized as `null`, included as `"b":null`.
- **Step D**: Property `c` value `undefined` -> in objects, properties with `undefined` values are omitted from the resulting JSON text (the property is dropped).
- **Output**: Only `a` and `b` appear: `{"a":null,"b":null}` (returned as a JS string).

---

## 💡 Key Takeaway

* **`NaN`/`Infinity` become `null`**: Non-finite numeric values are not represented as numbers in JSON; they are serialized as `null`.
* **`undefined` differs by container**: `undefined` becomes `null` in arrays but is omitted from objects.

---

## 🛠️ Recommendations & Best Practices

* **Use explicit normalization**: Convert values you want preserved (e.g., `NaN`) to explicit placeholders before stringifying, or provide a `replacer` to control serialization.
* **Prefer explicit checks**: When sending data to external systems, ensure you normalize `undefined`/`NaN` cases to avoid accidental omissions.

```javascript
// Example: normalize before stringify
const payload = { a: null, b: Number.isFinite(x) ? x : null };
const json = JSON.stringify(payload);
```

---

## 🧠 Revision Tips & Cheat Sheet

### Visual Coercion Path / Logical Flow

```mermaid
graph TD
   A["['false', false]"] -->|"string -> \"false\""| B["[\"false\",false]"]
   C["[NaN,null,Infinity,undefined]"] -->|"NaN -> null"| D["[null,null,null,null]"]
   E["{a:null,b:NaN,c:undefined}"] -->|"omit undefined"| F["{\"a\":null,\"b\":null}"]
```

---

## 🔗 Helpful Resources

- [ECMA-262 Specification - JSON.stringify](https://tc39.es/ecma262/#sec-json.stringify)
- [MDN Web Docs - JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
- [BFE.dev - Quiz 43](https://bigfrontend.dev/quiz/json-stringify)

---

## 🏷️ Tags
`#JSON` `#serialization` `#NaN` `#undefined` `#SpecDeepDive`