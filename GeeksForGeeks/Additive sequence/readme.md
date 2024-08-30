Link ->[Additive sequence](https://www.geeksforgeeks.org/problems/additive-sequence/1)

## Approach
- Observe the pattern carefully, notice that we have string, so we need a way to get the previous two numbers not the index.
- Because `13` can occupy two indexes so we need a way to keep the last two numbers.
- We have used `memo` table to store the last two ways.
- first number can't be more than `len(s)//3`, so we have keep a check and similarly for second number `len(s[i:])//2`
- Continue the recursive function , once we hit the end and we haven't find any `False` condition, then we have found the `Additive sequence`