## [10. Equal](https://bigfrontend.dev/quiz/Equal-1)

### Approach
1. **! (Logical NOT)**: Converts its operand to a boolean immediately based on truthiness rules.
2. **== (Loose Equality)**: Only triggers ToPrimitive when comparing an object to a primitive (like a string, number, or boolean).
3. **Big Int (like 1n)** Implicit coercion: Happens automatically (e.g., "5" * 2 → 10 because "5" is coerced to a number).Explicit conversion: Done manually (e.g., Number("5") → 5).
   1. BigInt avoids accidental coercion with Number to prevent precision loss.
4. If one side is Boolean, then it is always converted to number
5. If there is object then toPrimitive is called (valueOf then toString())