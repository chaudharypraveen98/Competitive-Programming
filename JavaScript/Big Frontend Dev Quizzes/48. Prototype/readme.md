## [48. Prototype](https://bigfrontend.dev/quiz/prototype)

### Approach
1. Prototypes are the mechanism by which JavaScript objects inherit features from one another. Basically, when you try to access a property of an object: if the property can't be found in the object itself, the prototype is searched for the property. If the property still can't be found, then the prototype's prototype is searched, and so on until either the property is found.
2. Here, we have added bar property to the prototype of Foo. However, in the first two instances viz. Foo.prototype.bar = 1 and Foo.prototype.bar = 2 we are just updating this property to a value thus this change affects both previously created objects and newly created objects.
3. In the last instance, we are actually replacing the the Foo.prototype to a new object which will break the prototype chain. Hence, only newly created objects beyond this will have bar as 3

