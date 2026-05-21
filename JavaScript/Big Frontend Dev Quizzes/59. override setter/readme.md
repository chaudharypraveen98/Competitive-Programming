## [59. override setter](https://bigfrontend.dev/quiz/override-setter)

### Approach
1. Here, we have two classes defined. A has a property val initialized to 1 and a getter foo defined. B also has a property val and a setter foo
2. Remember that, when we override the get method, it appears that the set method must also be overridden, otherwise undefined is returned and vice-versa See this
3. So, when we create two objects a and b; a.foo will return the value 1 as getter is defined but b.foo returns undefined.
4. Also, when we do b.foo=3, the setter works and val gets updated to 3. However, as there is no getter defined b.foo returns undefined. Note that, accessing b.val directly returns the new value 3 though