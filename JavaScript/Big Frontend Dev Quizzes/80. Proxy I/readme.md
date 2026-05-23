## [80. Proxy I](https://bigfrontend.dev/quiz/proxy-i)

### Approach
1. Proxy does not work well with built-in objects, for example Map, Set, Date, Promise and others make use of so-called “internal slots”.
2. The Proxy object allows you to create an object that can be used in place of the original object, but which may redefine fundamental Object operations like getting, setting, and defining properties.
3. If a handler has not been defined, the default behavior is to forward the operation to the target, however that only applies to standard behaviors like property access, and not the internal slots of exotic objects.