## [76. const](https://bigfrontend.dev/quiz/const)

### Approach
- In javascript, the assignment happens from right to left. So, const statement is only applicable to a, not b and c. All the other variables are considered Global without the var/let/const identifier, hence b and c will be globally scoped.

- To visualize, think of it like
```
const a = (b = (c = 1));
// which effectively becomes
const a = (window.b = ( window.c = 1))
```