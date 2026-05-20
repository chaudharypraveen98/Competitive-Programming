## [95. number format](https://bigfrontend.dev/quiz/number-format)

### Approach
1. Historically, in early versions of JavaScript (and inherited from C/C++), a leading 0 on an unquoted number literal was the syntactic signal for an Octal integer (Base-8 system).
2. The mathematical system of Base-8 only contains digits from 0 through 7. Therefore, the compiler uses a strict fallback rule when scanning these literals:
3. The Base-8 Path: If a number starts with 0 and all subsequent digits are between 0 and 7, the engine compiles it as an octal value.
4. The Base-10 Fallback: If the number contains an 8 or a 9—which are mathematically invalid in Base-8—the compiler realizes it cannot be an octal. It aborts the octal tracking and treats the leading 0 as completely meaningless, parsing the number as a standard Decimal (Base-10) integer.
5. Value = `(1 * 8^1) + (7 * 8^0)` = 8 + 7 = 15