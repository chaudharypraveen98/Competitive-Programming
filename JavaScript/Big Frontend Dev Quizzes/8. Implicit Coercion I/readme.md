## [8. Implicit Coercion I](https://bigfrontend.dev/quiz/Implicit-Conversion-1)

### Approach

To master Implicit Coercion, you must look past the "magic" and follow the internal rules of the ECMAScript Specification. These rules act as the engine's "decision tree" when it encounters mismatched types during operations like addition or loose equality.

1. **The Logical NOT Rule (Truthiness)**
   1. The logical NOT (!) operator is the simplest form of coercion. It does not use math or string rules; it only cares about an item's Truthiness.
   2. The Rule: Any object (including [] or {}) is inherently truthy.
   3. The Action: !object always results in false.
   4. Key Distinction: This operator never triggers ToPrimitive conversion.
2. **The Arithmetic Rules (ToNumber)**
   1. When using math operators (except + with strings), JavaScript forces operands into numbers.
   2. null becomes 0: Treated as an intentional numerical "empty".
   3. undefined becomes NaN: Treated as a missing value that cannot be quantified.
   4. Booleans: true becomes 1 and false becomes 0.
   5. Strings: Leading/trailing whitespace is ignored; an empty string "" becomes 0.
3. **The Object-to-Primitive Rule (ToPrimitive)**
   1. When an object (like an array) meets a primitive in a comparison or math operation, the engine must "flatten" it.
   2. Check Symbol.toPrimitive: If it exists, use it.
   3. Default Order: The engine typically tries .valueOf() first.
   4. Fallback: If valueOf returns an object (which it usually does for arrays/objects), it calls .toString().
   5. [] → "" 
   6. [1, 2] → "1,2" 
4. **The Loose Equality (==) Hierarchy**
   1. This is where the rules combine. The engine follows a specific priority list to make the types match:
      1. **Rule A** (Booleans First): If either side is a boolean, convert that boolean to a number (0 or 1) first.
      2. **Rule B** (Null/Undefined): null and undefined are equal to each other but equal to nothing else.
      3. **Rule C (Object vs. Primitive)**: Use the ToPrimitive rules above to convert the object to a string or number.
      4. **Rule D (BigInt vs. Number)**: Compare their direct mathematical values.
