## [7. Increment Operator](https://bigfrontend.dev/quiz/Increment-Operator)

### Approach
1. The Mental Model: **"Position is Priority"**. The key to remembering this without a table is the position of the ++ relative to the variable:
   1. **Prefix (++i)**: The operator comes first, so the increment happens first. The "updated" value is returned to the expression.
   2. **Postfix (i++)**: The variable comes first, so the original value is returned first. The increment happens as a hidden side effect immediately afterward.