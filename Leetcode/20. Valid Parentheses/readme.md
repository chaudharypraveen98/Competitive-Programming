Link -> [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

## Approach

**Stack Data Structure**: The stack is used to store opening parentheses as we encounter them in the string.

**Mapping Parentheses**: We maintain a dictionary pairs that maps each closing parenthesis to its corresponding opening parenthesis. This helps in checking matches.

**Traversal**: As we traverse the string:
If the character is an opening parenthesis ('(', '{', '['), we push it onto the stack.
If the character is a closing parenthesis (')', '}', ']'), we check if the top of the stack holds the matching opening parenthesis:
1. If it matches, we pop the top of the stack.
2. If it doesn't match or the stack is empty (i.e., no corresponding opening parenthesis), the string is invalid.
3. Final Check: After the string traversal, if the stack is empty, the parentheses are balanced and valid; otherwise, it is invalid.
Complexity

**Time complexity:**
The time complexity is 𝑂(𝑛)
O(n), where n is the length of the input string. This is because we process each character once by either pushing or popping from the stack.

**Space complexity:**
The space complexity is 𝑂(𝑛)
O(n) because, in the worst case, all opening parentheses will be stored in the stack before encountering their corresponding closing parentheses.