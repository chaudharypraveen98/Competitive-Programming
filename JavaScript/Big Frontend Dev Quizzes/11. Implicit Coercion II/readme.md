## [11. Implicit Coercion II](https://bigfrontend.dev/quiz/Implicit-Conversion-II)
1. If mathematical operator is present, `toNumber` is called.



| Expression | Primary Operator Rule | Coercion Path            | Final Result                            |
|------------|-----------------------|--------------------------|-----------------------------------------|
| [] + {}    | + (String priority)   | "" + "[object Object]"   | "[object Object]"                       |
| {} + {}    | + (Ambiguous Context) | Obj + Obj OR Unary + Obj | "[object Object][object Object]" or NaN |
| {} - {}    | - (Math only)         | NaN - NaN                | NaN                                     |
