## [114. constructor](https://bigfrontend.dev/quiz/constructor)

### Approach
1. When a function is called with the new keyword, the function will be used as a constructor. This means, first a new object is created, that new object is prototype linked, and the new object is set as this binding.
2. Lastly, a copy of this object is returned if no explicit return is present.
3. However, in this case, since we are returning an object from A(), this return value becomes the result of the whole new expression. Hence, a.dev1 is actually bigfrontend and not BFE. Also, since returned object doesn't contain dev2 property, it logs undefined