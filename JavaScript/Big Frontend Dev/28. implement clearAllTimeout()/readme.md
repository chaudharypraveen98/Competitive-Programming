## [28. implement clearAllTimeout()](https://bigfrontend.dev/problem/implement-clearAllTimeout)

### Approach
1. Use monkey patching
2. settimeout always returns id
3. Delete timer once done
4. Hurray done